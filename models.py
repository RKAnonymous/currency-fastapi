from config.database import Base
from sqlalchemy import String, Integer, Float, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


NOW = datetime.now()


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, autoincrement=True)
    base = Column(String, nullable=False, index=True)
    last_update = Column(DateTime, default=NOW)
    metas = relationship("Meta")


class Meta(Base):
    __tablename__ = "meta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    currency_id: int = Column(Integer, ForeignKey("currency.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    code = Column(String, nullable=False, index=True)
    rate = Column(Float, nullable=False)
