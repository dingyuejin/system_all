# coding=utf-8
from sqlalchemy import Column,String,create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.db.get_conf import get_db_args
def get_engine():
    args=get_db_args()
    connect_str="mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(args['user'], args['password'],
                                                             args['host'], args['port'], args['db_name'])
    engine=create_engine(connect_str,encoding="utf-8",echo=True)
    return engine

eng=get_engine()
Base=declarative_base()
Session =sessionmaker(bind=eng)
db_session=Session()
metadata=MetaData(eng)