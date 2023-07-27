# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/6 10:01
# @File: user.py
# @Software: PyCharm

from sqlalchemy.sql.schema import ForeignKey
from app.model import Base, TimeStampMiXin
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship


class User(Base, TimeStampMiXin):
    __tablename__ = 'user'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    nickname = Column(String(50))
    password = Column(String(500))
    department = Column(String(50))
    is_delete = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('role.id'))

    def __str__(self):
        return self.nickname


class Role(Base, TimeStampMiXin):
    __tablename__ = 'role'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String(50))
    role_name = relationship('User', backref='role')

    def __str__(self):
        return self.role
