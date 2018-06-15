"""
create by gaowenfeng on 
"""
import json

from flask import request
from werkzeug.exceptions import HTTPException

__author__ = "gaowenfeng"


class APIException(HTTPException):
    code = 500
    error_code = 999
    msg = 'sorry, we make a mistake'

    def __init__(self, msg=None, code=None, error_code=None,
                 headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(self.msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method+' '+self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = request.full_path
        main_path = full_path.split('?')
        return main_path[0]
