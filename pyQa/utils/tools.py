# -*- coding:utf-8 -*-
import yaml
import time
import random
import platform
import datetime
import sys
import pdb

class Tools(object):
    
    #读取指定的yaml文件
    @staticmethod
    def get_config(path):
        return yaml.load(open(path,'r')) 
    
    #随机得到电话号码
    @staticmethod
    def get_random_phone_number():
        phone_pre = ["139",'131','132','133','158','156','134','155','153','151','159','170','177','179']
        random_index = random.randrange(len(phone_pre))-1
        phone =   phone_pre[random_index] + time.strftime("%m%d%H%S")
        return phone 
    
    #随机得到一串字符串
    @staticmethod 
    def get_random_person_id():
        person_id =  "id" + time.strftime("%y%m%d%H%M%S")
        return person_id   
    
    @staticmethod 
    def get_random_chinese_name():
        person_name =  u"测试" + time.strftime("%y%m%d%H%S")
        return person_name 
    
    @staticmethod
    def get_random_title():
        title = "autotest" + time.strftime("%y%m%d%H%S")
        return title
    

    @staticmethod
    def get_random_email():
        email_suffix = ["@qq.com",'@163.com','@gmail.com','@sina.com','@sohu.com','@china.com','@163.com','@126.com','@dianrong.com']
        random_index = random.randrange(len(email_suffix))-1
        email =   time.strftime("%m%d%H%S") + email_suffix[random_index]
        return email
    
    @staticmethod
    def get_random_account():
        account_pre = ["cdu",' test', 'jack',' mick', 'ben','marry', 'lorry','patty','wen']
        random_index = random.randrange(len(account_pre))-1
        account_name =   account_pre[random_index] + time.strftime("%d%H%S") 
        return account_name
    
    @staticmethod
    #Linux or Window
    def get_current_os():
        return  platform.system()
    
    @staticmethod
    def get_random_actor_id():
        random_id = random.randrange(600000000, 700000000, 9)
        return random_id
    
    
    @staticmethod
    def get_today_uc_second(year_offset = 0, mon_offset = 0, day_offset=0):
        local_time =  time.localtime()
        year = local_time.tm_year - year_offset
        mon = local_time.tm_mon - mon_offset
        day =  local_time.tm_mday - day_offset
        d1 = datetime.date(year, mon, day)
        d2 = d1.timetuple()
        uc_second = time.mktime(d2) * 1000
        return uc_second
     
    @staticmethod 
    def get_current_date():
        return  time.strftime("%Y-%m-%d")      
    
    @staticmethod 
    def get_yesterday_date():
       #2016-07-03 17:13:59
       yearerday = time.time() - 24*60*60
       yearerday_time = time.localtime(yearerday)
       return time.strftime("%Y-%m-%d %H:%M:%S", yearerday_time)
     

    #获取命令行启动，输入的测试集参数
    #第一个参数是运行环境，第二个运行的测试集
    #eg python debug_test Demo Smoke
    @staticmethod
    def get_test_suit_paramter():  
            if len(sys.argv) > 2:
                return  sys.argv[2].strip() 
            else:
                return "regression"   
      
    #获得测试环境,从命令行获得       
    @staticmethod
    def get_test_suit_env():  
            if len(sys.argv) > 1:
                return  sys.argv[1].strip() 
            else:
                return "Demo"           
      
    #获取命令行启动，输入参数,从命令行获得       
    @staticmethod
    def get_paramters():  
        return  sys.argv
          
    @staticmethod 
    #使用方式： @unittest.skipUnless(runTagIn("smoke","regression"),"skip case if not in tags") 　
    #可以设置某个测试案例属于那个测试案例集合，便于过滤测试案例
    def runCaseIn(*tags):
        run_testSuit =  Tools.get_test_suit_paramter()
        if run_testSuit in tags:
            return True
        else:
            return False  