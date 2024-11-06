import requests
from ...config import settings
from fastapi import HTTPException
from . import sync_convert_currency_action

def handle(from_currency: str, to_currencies: str, price: float) -> float:
    currencies_list = to_currencies.split(',')
    result = []
    for currency in currencies_list:
        response = sync_convert_currency_action.handle(from_currency, currency, price)
        result.append(response)
    return result