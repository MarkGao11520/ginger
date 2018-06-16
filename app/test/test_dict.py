"""
create by gaowenfeng on 
"""

__author__ = "gaowenfeng"


class Person:
    name = 'gwf'
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ('name', 'age', 'gender')

    def __getitem__(self, item):
        return getattr(self, item)


o = Person()
print(dict(o))
