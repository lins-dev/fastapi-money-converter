from fastapi import APIRouter
from .actions import get_sync_list_of_currencies_and_call_covert_action
from .actions import get_async_list_of_currencies_and_call_covert_action

router = APIRouter(
    prefix="/conversions",
    tags=["conversions"],
    responses={404: {"description": "Not found"}},
)


@router.get('/')
async def index():
    return {"msg": "find many convertions"}

@router.get('/async/{from_currency}')
async def show(from_currency: str, to_currencies: str, price: float):
    res = await get_async_list_of_currencies_and_call_covert_action.handle(from_currency, to_currencies, price)
    return {"data" : res}

@router.get('/sync/{from_currency}')
def show(from_currency: str, to_currencies: str, price: float):
    res = get_sync_list_of_currencies_and_call_covert_action.handle(from_currency, to_currencies, price)
    return {"data" : res}