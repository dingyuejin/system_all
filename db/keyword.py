# coding=utf-8
from db.models import KeyWords
from db.basic_db import db_session


def insert_keyword(keyword):
    db_session.add(keyword)
    db_session.commit()