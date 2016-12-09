# -*- coding:utf-8 -*-
import yaml
from os import path

class GlobalFactory(object):
    Driver = None
    ErrorCount = 0

    #获到驱动
    @staticmethod    
    def get_driver():
        return GlobalFactory.Driver
    
    #设置驱动
    @staticmethod  
    def set_driver(driver):
        GlobalFactory.Driver = driver

    #增加error统计
    @staticmethod
    def add_error_count():
        GlobalFactory.ErrorCount += 1

        # 增加error统计

    @staticmethod
    def get_error_count():
        return GlobalFactory.ErrorCount
