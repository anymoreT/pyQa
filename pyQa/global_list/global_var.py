# -*- coding:utf-8 -*-
import yaml
from os import path

class Global_factory(object):
    Driver = None
    ErrorCount = 0
    
    #获到驱动
    @staticmethod    
    def get_driver():
        if Global_factory.Driver is None:
            raise("driver is None")
        return Global_factory.Driver
    
    #设置驱动
    @staticmethod  
    def set_driver(driver): 
        Global_factory.Driver = driver

    #增加error统计
    @staticmethod
    def add_error_count():
        Global_factory.ErrorCount += 1

        # 增加error统计

    @staticmethod
    def get_error_count():
        return Global_factory.ErrorCount
