from fastapi import APIRouter

router = APIRouter(
    prefix="/conversions",
    tags=["conversions"],
    responses={404: {"description": "Not found"}},
)


@router.get('/')
async def index():
    return {"msg": "find many convertions"}