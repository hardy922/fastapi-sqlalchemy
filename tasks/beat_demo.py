# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/7 14:30
# @File: beat_demo.py
# @Software: PyCharm

import time
from app.utils import log
from tasks.celery import celery_app


@celery_app.task
def beat_task_demo():
    """
    定时任务demo
    :return:
    """
    # 需要实现的功能
    pass
    return 'done'



