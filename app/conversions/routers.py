from fastapi import APIRouter
from fastapi import Path
from fastapi import Query
from .actions import get_sync_list_of_currencies_and_call_covert_action
from .actions import get_async_list_of_currencies_and_call_covert_action
from .schemas import ConversionInput, ConversionOutput

router = APIRouter(
    prefix="/conversions",
    tags=["conversions"],
    responses={404: {"description": "Not found"}},
)


@router.get('/')
async def index():
    return {"msg": "find many convertions"}

@router.get('/async/{from_currency}')
async def show(
    from_currency: str = Path(regex='^[A-Z]{3}$'), 
    to_currencies: str = Query(max_length=150, regex='^[A-Z]{3}(,[A-Z]{3})+$'), 
    price: float = Query(gt=0)
):
    res = await get_async_list_of_currencies_and_call_covert_action.handle(from_currency, to_currencies, price)
    return {"data" : res}

@router.get('/sync/{from_currency}')
def show(
    from_currency: str = Path(regex='^[A-Z]{3}$'), 
    to_currencies: str = Query(max_length=150, regex='^[A-Z]{3}(,[A-Z]{3})+$'), 
    price: float = Query(gt=0)
):
    res = get_sync_list_of_currencies_and_call_covert_action.handle(from_currency, to_currencies, price)
    return {"data" : res}

@router.post('/async/{from_currency}', response_model=ConversionOutput)
async def show(
    body: ConversionInput,
    from_currency: str = Path(regex='^[A-Z]{3}$')
):
    to_currencies = ",".join(map(str, body.to_currencies))
    res = await get_async_list_of_currencies_and_call_covert_action.handle(from_currency, to_currencies, body.price)
    return ConversionOutput(data=res)