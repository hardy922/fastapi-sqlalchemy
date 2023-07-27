# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/5 11:01
# @File: create_db.py
# @Software: PyCharm


from app.model import engine
from app.model import area
from app.model import user


def create_table():
    area.Base.metadata.create_all(bind=engine)
    user.Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_table()
