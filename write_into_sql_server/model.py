from typing import Annotated
from datetime import datetime

from sqlmodel import SQLModel, Field
from sqlalchemy.dialects.mssql import DATETIME2

class BaseParticleModel(SQLModel):
    id: int|None = Field(default=None, primary_key=True)
    d_time: datetime|None = Field(sa_type=DATETIME2)
    field: str = Field(exclude=True)

class YL_200(BaseParticleModel, table=True):
    value: Annotated[float, Field(alias='溢流200目粒度', gt=0, nullable=False)]
    field: str = Field("溢流200目粒度", exclude=True)

