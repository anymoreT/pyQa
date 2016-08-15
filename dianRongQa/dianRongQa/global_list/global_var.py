# -*- coding:utf-8 -*-
import yaml
from os import path

class Global_factory(object):
    Driver = None
    @staticmethod    
    def get_driver():
        if Global_factory.Driver is None:
            raise("driver is None")
        return Global_factory.Driver
    
    @staticmethod  
    def set_driver(driver): 
        Global_factory.Driver = driver
    
#     @staticmethod  
#     def get_global_config():
#         #global_config_file = path.join(path.abspath('.'), "config", "global.ymal")
#         global_config_file = path.join(path.dirname(__file__), "global.ymal")
#         return yaml.load(open(global_config_file,'r')) 