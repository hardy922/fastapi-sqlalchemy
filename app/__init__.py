# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/4 18:27
# @File: __init__.py.py
# @Software: PyCharm

from fastapi import FastAPI
from aioredis import create_redis
from fastapi.middleware.cors import CORSMiddleware
from app.routes import v1
from read_yaml import read_yaml_config


def create_app():
    app = FastAPI(title="管理后台API")
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(v1, prefix='/api')
    register_redis(app)
    return app


def register_redis(app: FastAPI):
    redis_info = read_yaml_config()['redis']

    @app.on_event('startup')
    async def startup_event():
        app.state.redis = await create_redis(
            address=(redis_info['host'], int(redis_info['port'])),
            password=redis_info['password'], db=3, encoding="utf-8"
        )

    @app.on_event('shutdown')
    async def showdown_event():
        app.state.redis.close()
        await app.state.redis.wait_closed()
