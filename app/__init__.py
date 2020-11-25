# -*- coding: UTF-8 -*-
"""
@Author  : LJ
@Time    : 2020/11/25 16:31
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.apis.test import test
    app.register_blueprint(test, url_prefix="/test")

    return app