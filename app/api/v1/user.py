"""
create by gaowenfeng on 
"""

from app.libs.redprint import Redprint

__author__ = "gaowenfeng"

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'i am gwf'
