# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/4 18:32
# @File: crud_area.py
# @Software: PyCharm

from sqlalchemy.sql.schema import ForeignKey
from app.model import Base, TimeStampMiXin
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship


class AreaZone(Base, TimeStampMiXin):
    __tablename__ = 'area_zone'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True, comment='id')
    area_number = Column(String(50), unique=True, nullable=False, comment='区域编号')
    area_name = relationship('AreaInfo', backref='area_zone')

    def __str__(self):
        return self.area


class AreaInfo(Base, TimeStampMiXin):
    __tablename__ = 'area_info'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True, comment="id")
    vmid = Column(String(50), nullable=False, comment='实例')
    ip = Column(String(50), comment='ip地址')
    label = Column(String(10), comment='标记')
    area_type = Column(String(10), comment='类型')
    area_id = Column(Integer, ForeignKey('area_zone.id'))
    mgr_state = Column(String(50), comment='管理状态')
    os_state = Column(String(50), comment='OS状态')

    def __str__(self):
        return self.area
