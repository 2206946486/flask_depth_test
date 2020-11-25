# -*- coding: UTF-8 -*-
"""
@Author  : LJ
@Time    : 2020/11/25 17:50
"""
from flask import Blueprint

test = Blueprint("test", __name__)


from . import tests
