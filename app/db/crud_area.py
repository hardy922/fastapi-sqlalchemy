# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/5 19:44
# @File: crud_area.py
# @Software: PyCharm

from sqlalchemy.orm import Session
from app.model.schemas import  AreaZoneModify
from app.model.area import AreaInfo, AreaZone
from app.utils import log
from typing import List, Dict


async def area_count(db: Session):
    return db.query(AreaZone).count()


async def area_info_count(db: Session, area):
    count = db.query(AreaInfo).filter(AreaInfo.area_id == area).count()
    return count


async def get_limit_areas(db: Session, offset: int = 0, limit: int = 10):
    return db.query(AreaZone).offset(offset).limit(limit).all()


async def create_area_zone(db: Session, zone: AreaZone):
    zone_info = AreaZone(**zone.dict())
    try:
        db.add(zone_info)
        db.commit()
        db.refresh(zone_info)
        log.info(f'创建区域{zone}成功')
        return zone_info
    except Exception as e:
        log.error(f'添加区域{zone_info}出错-->{str(e)}')
        return False


async def modify_area_info(db: Session, info: AreaZoneModify):
    try:
        info = info.dict()
        area = db.query(AreaZone).filter(AreaZone.id == info['id']).first()
        if area is not None:
            area.area_number = info['area_number']
            db.commit()
            log.info(f"修改区域{info}成功")
            return info
        else:
            log.warning(f'修改区域时未找到{info["id"]}')
            return None
    except Exception as e:
        log.error(f'修改区域{info}出错-->{str(e)}')
        return False


async def delete_area(db: Session, id):
    area = db.query(AreaZone).filter(AreaZone.id == id).first()
    if area is not None:
        db.delete(area)
        db.commit()
        log.info(f'删除区域{id}成功')
        return area
    else:
        log.warning(f'删除区域{id}未找到数据')
        return None



