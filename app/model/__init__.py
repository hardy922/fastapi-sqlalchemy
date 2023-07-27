# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/4 18:27
# @File: __init__.py.py
# @Software: PyCharm

from urllib.parse import quote_plus as urlquote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from sqlalchemy import Column, DateTime
from read_yaml import read_yaml_config

mysql = read_yaml_config()['mysql']

DATABASE_URL = f'{mysql["data"]}+{mysql["driver"]}://{mysql["username"]}:' \
               f'{urlquote(mysql["password"])}@{mysql["uri"]}:{mysql["port"]}/{mysql["database"]}?charset=utf8'


Base = declarative_base()

# pool_pre_ping参数用于启用或禁用连接池中的连接预检查功能
engine = create_engine(DATABASE_URL, pool_size=50, max_overflow=10, echo=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class TimeStampMiXin(object):
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
