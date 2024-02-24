[![Python app test with Github Actions](https://github.com/RKAnonymous/currency-fastapi/actions/workflows/ci.yml/badge.svg?branhc=master)](https://github.com/RKAnonymous/currency-fastapi/actions/workflows/ci.yml)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg?logo=Python&logoColor=yellow)](https://www.python.org/downloads/release/python-360/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.85.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)

# Simple Currency conversion app with FastAPI


### Initial setup
#### Update .env file with your own environment variable values

    SQL_USER={YOUR_DB_USER}
    SQL_PASSWORD={YOUR_DB_PASSWORD}
    SQL_DB={YOUR_DB_NAME}

#### Run docker compose

    docker compose -f docker-compose.yaml up --build -d


### Predefined data

Initial data was set in the first alembic migration file.
As soon as docker compose runs the seeded data is being inserted into database.


### Endpoints

    +-----------------+------------+------------------------------------------------------------+
    |       URL       |   METHOD   |                           DESCRIPTION                      |
    +-----------------+------------+------------------------------------------------------------+
    |  /update-rates  |     GET    |  Save last updated currency exchange rates into database   |
    +-----------------+------------+------------------------------------------------------------+
    |  /last-update   |     GET    |  Return last updated datetime from database                |
    +-----------------+------------+------------------------------------------------------------+
    |  /convert       |     GET    |  Convert given value from source currency to target        |
    +-----------------+------------+------------------------------------------------------------+