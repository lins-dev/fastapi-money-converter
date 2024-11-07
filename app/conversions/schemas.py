from pydantic import BaseModel, Field, field_validator
from typing import List
import re

class ConversionInput(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]

    @field_validator('to_currencies')
    def validate_to_currencies(cls, to_currencies):
        for currency in to_currencies:
            if not re.match('^[A-Z]{3}$', currency):
                raise ValueError(f'Invalid  currency: {currency}')
        return to_currencies
    

class ConversionOutput(BaseModel):
    data: List[dict]