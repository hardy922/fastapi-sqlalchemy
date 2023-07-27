# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/4 19:07
# @File: crud_area.py
# @Software: PyCharm

import asyncio
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session
from app.res_status import RequestInfo
from app.db import get_db
from app.db import crud_area
from app.model import schemas
from app.utils import log


area_router = APIRouter(tags=["区域相关"])


@area_router.get('/areas', summary="查询所有区域")
async def get_areas(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=50),
                    db: Session = Depends(get_db)):
    offset = (page - 1) * page_size
    total = await crud_area.area_count(db)
    areas = await crud_area.get_limit_areas(db, offset=offset, limit=page_size)
    areas_out = []
    for area in areas:
        count = await crud_area.area_info_count(db, area.id)
        areas_out.append({"id": area.id, "area": area.area_number, "count": count})
    total_pages = (total + page_size - 1) // page_size
    data = {"total": total, "page": page, "page_size": page_size, "total_pages": total_pages, "page_info": areas_out}
    log.info(f'get——>/areas, res:{jsonable_encoder(data)}')
    return RequestInfo.successful(data=data)


@area_router.post('/area', summary="添加区域")
async def add_area(area: schemas.AreaZoneBase, db: Session = Depends(get_db)):
    create_zone = await crud_area.create_area_zone(db, area)
    if create_zone is False:
        log.error(f'post-->/area， 添加{area}失败')
        return RequestInfo.server_error_500(data=None)
    else:
        log.info(f'post-->/area, res:{jsonable_encoder(create_zone)}')
        return RequestInfo.successful(data=create_zone)


@area_router.put('/area', summary="修改指定区域")
async def modify_area(info: schemas.AreaZoneModify, db: Session = Depends(get_db)):
    res = await crud_area.modify_area_info(db, info)
    if res is None:
        log.warning(f'put-->/area, res:{res}')
        return RequestInfo.non_existent_404(data=None)
    elif res is False:
        log.error(f'put-->/area, res:{res}')
        return RequestInfo.server_error_500(data=None)
    else:
        log.info(f'put-->/area, res:{res}')
        return RequestInfo.successful(data=res)


@area_router.delete('/area/{id}', summary="删除指定区域")
async def delete_area(id: str, db: Session = Depends(get_db)):
    area = await crud_area.delete_area(db, id)
    if area is None:
        log.warning(f'delete-->/area/{id}，未找到区域id')
        return RequestInfo.non_existent_404(data=None)
    else:
        log.info(f'delete-->/area/{id}, res:{jsonable_encoder(area)}')
        return RequestInfo.successful(data=area)
