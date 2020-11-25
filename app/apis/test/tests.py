# -*- coding: UTF-8 -*-
"""
@Author  : LJ
@Time    : 2020/11/25 17:51
"""
from . import test


@test.route('/', methods=["GET"])
def test():
    return "测试案例"
