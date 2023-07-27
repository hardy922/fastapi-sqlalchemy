# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/4 18:27
# @File: __init__.py.py
# @Software: PyCharm

from fastapi import APIRouter
from .area import area_router
from app.model import session


v1 = APIRouter(prefix="/v1")
v1.include_router(area_router)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
