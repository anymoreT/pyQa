# -*- coding:utf-8 -*-
import sys
import time


class Log(object):
    #打印错误日志，抛出异常
    @staticmethod
    def log_error_info(info):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S:")
        sys.stdout.write(timestamp + info + "\n")
        raise Exception("Assert error:", info)
  
    #打印日志  
    @staticmethod
    def log_info(info):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S:")    
        print(timestamp + info + "\n")