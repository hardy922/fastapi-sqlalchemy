# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2022/12/2 9:46
# @File: sqlalchemy_utils.py
# @Software: PyCharm

from app.utils.logger import Log
from settings import Config
from sqlalchemy import create_engine, Table, MetaData, text
from sqlalchemy.orm import Session
from urllib.parse import quote_plus as urlquote
from read_yaml import read_yaml_config


class DataBase(object):

    def __init__(self, username, password, host, port, database):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.database_connection = (
            f"mysql+pymysql://{self.username}:{urlquote(self.password)}@{self.host}:{self.port}/{self.database}?charset=utf8&autocommit=true"
        )
        self.engine = create_engine(self.database_connection, pool_pre_ping=True, pool_recycle=180)
        self.session = Session(self.engine)

    def tables(self, table):
        metadata = MetaData()
        metadata.reflect(bind=self.engine)
        return Table(table, metadata)

    def commit(self):
        return self.session.commit()


class MySqlDB(object):

    @staticmethod
    def init():
        mysql = read_yaml_config()['mysql']
        database = DataBase(
            username=mysql['username'],
            password=mysql['password'],
            host=mysql['uri'],
            port=mysql['port'],
            database=mysql['database'],
        )
        return database

    @classmethod
    def insert_data(cls, table, **kwargs):
        """
        插入数据
        :param table:
        :param kwargs:
        :return:
        """
        db = cls.init()
        try:
            tb = db.tables(table)
            sql = tb.insert().values(**kwargs)
            db.session.execute(sql)
            db.session.commit()
            db.session.close()
            return True
        except Exception as e:
            Log.get_logger().error(f'插入表{table}数据：{kwargs}出错-->{str(e)}')
            return e

    @classmethod
    def delete_data(cls, table, field, value):
        """
        删除数据
        :param table:
        :param field:
        :param value:
        :return:
        """
        db = cls.init()
        try:
            tb = db.tables(table)
            sql = tb.delete().where(getattr(tb.c, field) == value)
            db.session.execute(sql)
            db.session.commit()
            db.session.close()
            return True
        except Exception as e:
            Log.get_logger().error(f'删除表{table}数据：条件({field}={value})出错-->{str(e)}')

    @classmethod
    def truncate_table(cls, table):
        """
        重置表
        :param table:
        :return:
        """
        db = cls.init()
        try:
            db.tables(table)
            sql = text(f"TRUNCATE TABLE {table}")
            db.session.execute(sql)
            db.session.commit()
            db.session.close()
            return True
        except Exception as e:
            Log.get_logger().error(f'重置表{table}出错-->{str(e)}')
            return e
