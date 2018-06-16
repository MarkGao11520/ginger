"""
create by gaowenfeng on 
"""
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

__author__ = "gaowenfeng"

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm(request).validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()

    return Success()


def __register_user_by_email():
    form = UserEmailForm(request).validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)
