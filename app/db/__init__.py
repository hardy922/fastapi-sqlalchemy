# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/5 19:44
# @File: __init__.py.py
# @Software: PyCharm

from app.model import session


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
