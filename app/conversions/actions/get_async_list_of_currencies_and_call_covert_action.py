import requests
from ...config import settings
from fastapi import HTTPException
from . import async_convert_currency_action
from asyncio import gather

async def handle(from_currency: str, to_currencies: str, price: float):
    currencies_list = to_currencies.split(',')
    coroutines = []
    for currency in currencies_list:
        coroutine = async_convert_currency_action.handle(
            from_currency, 
            currency, 
            price
        )
        coroutines.append(coroutine)
    
    result  = await gather(*coroutines)
    return result