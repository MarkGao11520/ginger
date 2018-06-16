"""
create by gaowenfeng on 
"""
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from datetime import date

from app.libs.error_code import ServerError

__author__ = "gaowenfeng"


class JSONEncoder(_JSONEncoder):

    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        # 兼容其他的序列化
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder




