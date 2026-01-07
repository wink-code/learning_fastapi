from typing import Annotated
from datetime import datetime

from sqlmodel import SQLModel, Field
from sqlalchemy.dialects.mssql import DATETIME2


class YL(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    d_time: datetime|None = Field(sa_type=DATETIME2)
    yl_200: Annotated[float, Field(alias='溢流200目粒度', gt=0, nullable=False)]
    yl_80: Annotated[float, Field(alias='溢流80目粒度', gt=0, nullable=False)]

