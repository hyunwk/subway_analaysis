from typing import Optional

from sqlmodel import SQLModel, Field


class Store(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    store_type: str
    line : int
    name: str
    store_no: str
    square_meter: float
    start_date: Optional[str]
    end_date: Optional[str]
    price: Optional[int]
