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

    @staticmethod
    def add_error_count():
        '''
        获取error统计
        '''
        GlobalFactory.ErrorCount += 1



    @staticmethod
    def get_error_count():
        '''
        获取error统计
        '''
        return GlobalFactory.ErrorCount
