"""
create by gaowenfeng on 
"""
from werkzeug.exceptions import MethodNotAllowed, HTTPException
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = "gaowenfeng"


class BaseForm(Form):
    def __init__(self, request):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

