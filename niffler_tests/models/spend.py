from datetime import datetime

from sqlmodel import SQLModel

class Category(SQLModel, table=True):
    id: int
    name: str
    description: str

class Spend(SQLModel, table=True):
    id: str
    amount: float
    desciption: str
    category: str
    spendDate: datetime
    currency: str