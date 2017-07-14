# coding=utf-8
import os
import random
from yaml import load
config_path=os.path.join(os.path.dirname(__file__),'conf.yaml')

with open(config_path,'r') as code:
    conf=code.read()

config=load(conf)

def get_db_args():
    return config.get('mysql')

