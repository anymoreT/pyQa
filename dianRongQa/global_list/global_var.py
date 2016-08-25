# -*- coding:utf-8 -*-
import yaml
from os import path

class Global_factory(object):
    Driver = None
    
    #得到驱动
    @staticmethod    
    def get_driver():
        if Global_factory.Driver is None:
            raise("driver is None")
        return Global_factory.Driver
    
    #设置驱动
    @staticmethod  
    def set_driver(driver): 
        Global_factory.Driver = driver
