# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/5 9:58
# @File: schemas.py
# @Software: PyCharm

from enum import Enum
from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel, Field


class AreaZoneBase(BaseModel):
    area_number: str


class AreaZoneModify(BaseModel):
    id: int
    area_number: str


class AreaInfoBase(BaseModel):
    area_id: int
    vmid: str
    ip: str
    label: str
    area_type: str


class AreaInfoModify(BaseModel):
    id: int
    vmid: str = None
    ip: str = None
    label: str = None
    area_type: str = None
    mgr_state: str = None
    os_state: str = None


class AreaOut(BaseModel):
    id: int
    area: str
    vmid: str
    ip: str
    label: str
    area_type: str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
        exclude = {'created_at', 'updated_at'}


class PackageType(Enum):
    mobile = "mobile"
    client = "client"
    aic = "aic"


class Package(BaseModel):
    types: PackageType = Field(
        title="Package Type",
        description="The type of package",
        enum=[m.value for m in PackageType.__members__.values()]
    )
