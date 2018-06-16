"""
create by gaowenfeng on 
"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db

__author__ = "gaowenfeng"


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)
    nickname = Column(String(24), nullable=False)
    _password = Column('password', String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 从面向对象的角度考虑，在一个对象中创建一个对象本身这个是不合理的。
    # 但是如果将他声明为一个静态方法，那么就是合理的
    @staticmethod
    def register_by_email(nikename, account, secert):
        with db.auto_commit():
            user = User()
            user.nickname = nikename
            user.email = account
            user.password = secert
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        return {'uid': user.id}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
