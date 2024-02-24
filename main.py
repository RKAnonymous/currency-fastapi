import requests
from fastapi import FastAPI, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from config.settings import get_settings
from config.database import get_session
from models import Currency, Meta
from utils import to_thread

settings = get_settings()

app = FastAPI()


@app.get("/")
async def index(db: AsyncSession = Depends(get_session)):
    currency = await db.execute(
        select(Meta)
        .filter(Currency.base == "USD")
        .join(Currency, Meta.currency_id == Currency.id)
        .order_by(Currency.last_update.desc())
    )
    return [d.__dict__ for d in currency.scalars().all()]


@app.get("/update-rates", status_code=status.HTTP_200_OK)
async def update_rates(db: AsyncSession = Depends(get_session)):
    based_on = settings.CURRENCY_CODES[
        : settings.BASE_CURRENCY_LIMIT
    ]  # Request limit 10/min
    url = settings.SOURCE_URL

    for base_currency in based_on:
        params = {
            "apikey": settings.API_KEY,
            "base_currency": base_currency,
            "currencies": ",".join(settings.CURRENCY_CODES),
        }
        response = await to_thread(requests.get, url, params, timeout=5, delay=0.5)

        if response.status_code != 200:
            return JSONResponse(
                content={"message": "Source is not responding."}, status_code=500
            )

        data = response.json()["data"]

        # Save header currency data
        currency = Currency(**dict(base=base_currency))
        db.add(currency)
        await db.commit()
        await db.refresh(currency)

        metas = []
        for code, rate in data.items():
            obj = dict(
                name=settings.CURRENCY_NAMES.get(code),
                currency_id=currency.id,
                code=code,
                rate=rate,
            )
            metas.append(Meta(**obj))

        # Save currency meta data
        db.add_all(metas)
        await db.commit()

    return JSONResponse(
        content={"message": "Rates updated."},
        status_code=status.HTTP_200_OK,
    )


@app.get("/last-update")
async def last_update(db: AsyncSession = Depends(get_session)):
    currency = await db.execute(
        select(Currency).order_by(Currency.last_update.desc()).limit(1)
    )
    updated_at = currency.scalar_one().last_update
    return JSONResponse(
        content={"last_update": updated_at.strftime("%D-%m-%y %H:%M:%S")},
        status_code=status.HTTP_200_OK,
    )


@app.get("/convert")
async def conversion(
    target: str,
    amount: float,
    source: str = "USD",
    db: AsyncSession = Depends(get_session),
):
    source = source.upper()
    target = target.upper()

    rate_query = await db.execute(
        select(Meta)
        .filter(Currency.base == source, Meta.code == target)
        .join(Currency, Meta.currency_id == Currency.id)
        .order_by(Currency.last_update.desc())
        .limit(1)
    )

    rate = rate_query.scalar_one_or_none()

    if not rate:
        base_currencies = await db.execute(
            select(Currency)
            .order_by(Currency.last_update.desc())
            .limit(settings.BASE_CURRENCY_LIMIT)
        )
        available_options = [cur.base for cur in base_currencies.scalars().all()]

        return JSONResponse(
            content={
                "message": "Data not found. Try with another currency",
                "option": available_options,
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return JSONResponse(
        content={
            "from": source,
            "to": target,
            "value": amount,
            "converted_value": rate.rate * amount,
        },
        status_code=status.HTTP_200_OK,
    )
