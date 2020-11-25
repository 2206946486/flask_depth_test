# -*- coding: UTF-8 -*-
"""
@Author  : LJ
@Time    : 2020/11/25 16:31
"""
from app import create_app


app = create_app()


@app.route('/')
def test():
    return '测试一次啊'


if __name__ == "__main__":
    app.run()