# coding=utf-8
from db.basic_db import Base
from db.tables import *
class KeyWords(Base):
    # 关键词搜索表 keywords
    __table__ = keywords