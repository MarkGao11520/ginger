"""
create by gaowenfeng on 
"""
from app.libs.redprint import Redprint

__author__ = "gaowenfeng"

api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    return 'get book'


@api.route('', methods=['POST'])
def create():
    return 'create book'
