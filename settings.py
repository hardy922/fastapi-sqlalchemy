# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/4 18:43
# @File: settings.py
# @Software: PyCharm


import os.path


class Config(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_DIR = os.path.join(BASE_DIR, 'logs')

