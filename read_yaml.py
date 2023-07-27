# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/10 17:29
# @File: read_yaml.py
# @Software: PyCharm

import yaml
from settings import Config


def read_yaml_config():
    with open(f"{Config.BASE_DIR}/config.yaml", "r") as f:
        config = yaml.safe_load(f)
        return config


if __name__ == '__main__':
    yl = read_yaml_config()
    print(yl)
    