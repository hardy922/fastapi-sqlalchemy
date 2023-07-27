# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/7 14:28
# @File: celery.py
# @Software: PyCharm

from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
from urllib.parse import quote_plus as urlquote
from read_yaml import read_yaml_config

red = read_yaml_config()['redis']
red_psd = red['password']

celery_app = Celery("tasks",
                    broker=f"redis://:{urlquote(red_psd)}@{red['host']}:6379/1",
                    backend=f"redis://:{urlquote(red_psd)}@{red['host']}:6379/2",
                    include=[
                        "tasks.beat_demo"
                        ]
                    )

celery_app.conf.timezone = 'Asia/Shanghai'
celery_app.conf.broker_connection_retry_on_startup = True

celery_app.conf.beat_schedule = {
    "es_statistics": {
        "task": "tasks.beat_task_demo",
        "schedule": crontab(minute='22', hour='16', day_of_week='*'),
        "args": ""
    }
}
