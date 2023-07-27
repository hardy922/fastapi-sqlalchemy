# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/4 19:08
# @File: schemas.py
# @Software: PyCharm

from datetime import datetime
from typing import Union
from fastapi import status
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder


def format_time(obj: datetime, mapping=None):
    """
    格式化时间
    :param obj:
    :param mapping:
    :return:
    """
    stamp = "%Y-%m-%d %H:%M:%S"
    return obj.strftime(stamp)


class HttpCode(object):

    Ok = 200
    NotModified = 304
    ParameterError = 400
    Unauthorized = 401
    NonExist = 404
    MethodError = 405
    ServerError = 500
    NoPermission = 505


class RequestInfo(HttpCode):

    @classmethod
    def restful_result(cls, code, data, message):
        """
        响应结构
        :param code:
        :param message:
        :param data:
        :return:
        """
        structure = {"code": code, "data": data, "message": message}
        return structure

    @classmethod
    def successful(cls, data, message="success"):
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=jsonable_encoder(
                                cls.restful_result(200, data, message),
                                custom_encoder={datetime: format_time}
                            ))

    @classmethod
    def paras_error_400(cls, data, message="parameter error"):
        """
        参数错误
        :param data:
        :param message:
        :return:
        """
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content=jsonable_encoder(
                                cls.restful_result(400, data, message))
                            )

    @classmethod
    def unauthorized_error_401(cls, data, message="authentication failed"):
        """
        登录校验失败
        :param data:
        :param message:
        :return:
        """
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=jsonable_encoder(
                                cls.restful_result(401, data, message))
                            )

    @classmethod
    def non_existent_404(cls, data, message="not exist"):
        """
        未找到文件
        :param data:
        :param message:
        :return:
        """
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content=jsonable_encoder(
                                cls.restful_result(404, data, message)
                            ))

    @classmethod
    def server_error_500(cls, data, message="internal server error"):
        """
        服务出错
        :param data:
        :param message:
        :return:
        """
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content=jsonable_encoder(
                                cls.restful_result(500, data, message)
                            ))

    @classmethod
    def no_permission_505(cls, data, message="no permission"):
        """
        无权限
        :param data: 
        :param message: 
        :return: 
        """
        return JSONResponse(status_code=status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED,
                            content=jsonable_encoder(
                                cls.restful_result(505, data, message)
                            ))

    @classmethod
    def method_error_405(cls, data, message='request type not supported'):
        """
        请求类型错误
        :return:
        """
        return JSONResponse(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            content=jsonable_encoder(
                                cls.restful_result(405, data, message)
                            ))

    @classmethod
    def not_modified_304(cls, data, message):
        """
        重复请求
        :param data:
        :param message:
        :return:
        """
        return JSONResponse(status_code=status.HTTP_304_NOT_MODIFIED,
                            content=jsonable_encoder(
                                cls.restful_result(304, data, message)
                            ))



