# fastapi-money-converter

This is a simple FastAPI project designed to convert an amount in a given currency to a list of other selected currencies. The project uses FastAPI to create the API endpoints and managed with [uv](https://github.com/astral-sh/uv) .

Features
Accepts a currency name (e.g., "USD") and amount.
Converts the given amount to other user-selected currencies.
Provides real-time currency conversion rates.
Simple and extendable FastAPI project structure.

# Requirements
python = ">=3.13"
dependencies = [
    "aiohttp>=3.10.10",
    "fastapi[standard]>=0.115.4",
    "pydantic-settings>=2.6.1",
    "python-dotenv>=1.0.1",
    "requests>=2.32.3",
]


## License

MIT

