# coding=utf-8
from sqlalchemy import Table,Column,INTEGER,String
from db.basic_db import metadata
keywords=Table('keywords',metadata,
                 Column("id", INTEGER, primary_key=True, autoincrement=True),
                 Column("keyword", String(200), unique=True),
                 Column("enable", INTEGER, default=1, server_default='1'),
               )
