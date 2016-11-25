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
      
    #记录日志到report里面  
    @staticmethod   
    def log_step(step_info):
        print(sys.stdout,"<STEP_BEGIN>%s<STEP_END>"%(step_info))    
        
    #记录日志到case里面  
    @staticmethod   
    def log_case_desc(step_info):
        print(sys.stdout,"<DESC_BEGIN>%s<DESC_END>"%(step_info))
