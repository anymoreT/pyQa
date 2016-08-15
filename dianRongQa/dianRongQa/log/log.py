# -*- coding:utf-8 -*-
import sys
import time


class Log(object):
    @staticmethod
    def log_error_info(info):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S:")
        #info = unicode(info, 'utf-8')
        sys.stdout.write(timestamp + info + "\n")
        #raise NotImplementedError(info) 
        raise Exception("Assert error:", info)
  
    
    @staticmethod
    def log_info_for_console(info):  
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S:")  
        sys.stdout.write(timestamp + str(info) + "\n")
        
    @staticmethod
    def log_info_for_result(info):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S:")    
        print(info + "\n")
        
    @staticmethod
    def log_info(info):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S:")    
        print(info + "\n")