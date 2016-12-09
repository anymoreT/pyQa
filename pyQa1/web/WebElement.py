# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from pyQa.globalFactory.globalVars import GlobalFactory
# -*- coding:utf-8 -*-
from unittest import TestCase
from pyQa.log.log import Log
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement
import time
import pdb

class WebElement(object):
    def __init__(self, element_type, locator):
        '''
        element_type: "id","name","class","xpath"
        locator:选择元素的表达式
        '''
        self.type = element_type
        self.locator = locator
        self.driver = GlobalFactory.get_driver()
        self.action = ActionChains(self.driver)
        self.web_element = self.element()
        self.class_name = str(self.__class__)
      
    def element(self): 
        '''
        通过指定的方式，查找元素，没有查找到,返回None
        '''
        if self.type == "id":
            type = By.ID
        elif self.type == "xpath": 
            type = By.XPATH
        elif self.type == "name": 
            type = By.NAME   
        elif self.type == "class": 
            type = By.CLASS_NAME  
        elif self.type == "link_text":
            type = By.LINK_TEXT     
        else:
            type = By.XPATH 
        try:                                         
            self.web_element  =  self.driver.find_element(type, self.locator)
        except:
            self.web_element = None
        return self.web_element   
            #Log.log_error_info("Couldn't find element %s \n" % ( self.__locator))
    
    def get_element(self):
        '''
        返回元素
        '''
        return  self.web_element   
     
    #input_type:  None, js 
    def input(self, str="", input_type = None):
        '''
        输入文本．
        str：输入文本
        
        input_type：＇js＇,使用js直接进行赋值
        '''
        try:
            if (input_type == "js") or (input_type == "JS"):
                self.driver.execute_script("arguments[0].value='%s'"%  (str), self.get_element())
            else:    
                self.clear()
                self.web_element.send_keys(str)
            Log.log_step("向元素输入文本：%s.(元素位置：%s)"%(str, self.locator))
        except:
            Log.log_error_info("Couldn't input %s for %s\n" % (str, self.class_name))
    
    def clear(self):
        '''
        清空文本框
        '''
        try:
            self.web_element.clear()
            Log.log_step("清空元素文本.(元素位置：%s)"%(self.locator))
        except:
            Log.log_error_info("Couldn't clear %s\n" % (self.class_name))
            
    #click_type: None, js   
    def click(self, click_type = None):
        '''
        点击元素．
        click_type：　'js'　通过js直接操作元素
        '''
        try:
            if (click_type == "js") or (click_type == "JS"):
                self.driver.execute_script("arguments[0].click()", self.get_element())
            else:    
                self.web_element.click()
            Log.log_step("点击元素.(元素位置：%s)"%(self.locator))    
        except:
            Log.log_error_info("fail to  click %s\n" % (self.class_name))

    def send_tab_key(self):
        '''
        在元素上，按Tab键
        '''
        try:
            self.web_element.send_keys(Keys.TAB)
            Log.log_step("元素上按TAB键.(元素位置：%s)"%(self.locator))
        except:
            Log.log_error_info("fail to  send tab key for %s\n" % (self.class_name))   
     
    def send_enter_key(self):
        '''
        在元素上，按Enter键
        '''
        try:
            self.web_element.send_keys(Keys.ENTER)
            Log.log_step("元素上按ENTER键.(元素位置：%s)"%(self.locator))
        except:
            Log.log_error_info("fail to  send tab key for %s\n" % (self.class_name))         
    
    def is_exist(self):
        '''
        元素存在，返回真；元素存在，返回假
        '''
        try:
            Log.log_step("返回元素是否存在标示.(元素位置：%s)"%(self.locator))
            return self.web_element.is_displayed()
        except:
            return False 
    
    def should_not_enable(self):
        '''
        判断元素是不可用
        '''
        if self.get_element().is_enabled():
            Log.log_error_info("%s should not be enable\n" % (self.class_name))   
        Log.log_step("通过判断，元素不可用.(元素位置：%s)"%(self.locator))
        
    def should_enable(self):
        '''
        判断元素是可用
        '''
        if not self.get_element().is_enabled():
            Log.log_error_info("%s should be enable\n" % (self.class_name))   
        Log.log_step("通过判断，元素可用.(元素位置：%s)"%(self.locator))
        
    def wait_element_enable(self, timeout =  30, interval = 2):
        '''
        等待元素变成可用
        '''
        frequence  =  int(timeout/interval)
        for i in range(frequence):
            self.web_element = self.element()
            if self.web_element.is_enabled(): 
                if interval > 0:
                    time.sleep(interval)
                return
            time.sleep(int(interval)) 
        else:
            Log.log_error_info("fail to wait element %s enable\n" % (self.class_name))           
        Log.log_step("等待元素出现.(元素位置：%s)"%(self.locator))
         
    def get_text(self, time_interval = 2):
        '''
        获得元素文本
        '''
        try:
            #实际使用中发现，需要等待2秒才能稳定得到文本
            if time_interval > 0 :
                time.sleep(int(time_interval)) 
            Log.log_step("获取元素文本.(元素位置：%s)"%(self.locator))    
            return self.web_element.text 
        except:
            Log.log_error_info("fail to get text for %s\n" % (self.class_name))  
            
    def wait_element_present(self, timeout =  30, interval = 2):
        '''
        在设定的时间里，等待元素的出现；超过时间间隔，报错．
        timeout:  指定的时间
        interval：轮询的间隔时间
        '''
        frequence = int(timeout/interval)
        for i in range(frequence):
            self.web_element = self.element()
            if self.web_element is not None:
                if interval > 0:
                    time.sleep(int(interval))
                return
            time.sleep(int(interval)) 
        else:
            Log.log_error_info("fail to wait element %s present.locator is %s\n" % (self.class_name,self.locator))  
        Log.log_step("等待元素出现.(元素位置：%s)"%(self.locator))
    
    def should_exist(self):
        '''
        判断元素是否存在
        '''
        try:
            is_displayed = self.web_element.is_displayed()
            if not is_displayed:
                Log.log_error_info("%s is not existed\n" % (self.class_name))   
        except:
            Log.log_error_info("%s is has not display method\n" % (self.class_name))   
        Log.log_step("通过判断，元素存在.(元素位置：%s)"%(self.locator))
         
    def should_not_exist(self):
        '''
        判断元素不存在
        '''
        element = self.element()
        if element is None:
            Log.log_step("通过判断，元素不存在.(元素位置：%s)"%(self.locator))
            return True
        else:
            is_displayed = element.is_displayed()
            if is_displayed:
                Log.log_error_info("%s is existed\n" % (self.class_name))   
            else:
                Log.log_step("通过判断，元素不存在.(元素位置：%s)"%(self.locator))
                return True

    def should_include_text(self, include_text):   
        '''
        判断元素的文本包含指定的字符串
        '''
        text = self.get_text()
        index = text.find(include_text)
        if -1 == index:
            Log.log_error_info("%s  is not include %s, the real text is %s\n" % (self.class_name, include_text, text))   
        Log.log_step("通过判断，元素包含文本:%s.(元素位置：%s)"%(include_text,self.locator))
                  
    def should_not_include_text(self, include_text):
        '''
        判断元素不包含指定的字符串
        '''
        text = self.get_text()
        index = text.find(include_text)
        if -1 != index:
            Log.log_error_info("%s include %s, the real text is %s\n" % (self.class_name, include_text, text)) 
        Log.log_step("通过判断，元素不包含文本:%s.(元素位置：%s)"%(include_text,self.locator))
        
    def should_equal_text(self, expected_text):   
        '''
        判断字符串等于指定的字符串
        '''
        text = self.get_text()
        if text != expected_text:
            Log.log_error_info("%s  is not equal  %s, the real text is %s\n" % (expected_text, text, self.class_name))   
        Log.log_step("通过判断，元素等于文本:%s.(元素位置：%s)"%(expected_text,self.locator)) 
         
    def mouse_over(self, interval_time =2):
        '''
        模拟鼠标放到元素上面
        '''
        self.action.move_to_element(self.get_element())   
        self.action.perform()  
        time.sleep(interval_time)             
        Log.log_step("鼠标放在元素上.(元素位置：%s)"%(self.locator))
        
    def wait_element_disappear(self, timeout =  30, interval = 2):
        '''
        在指定的时间里面，等待页面元素消失．
        '''
        frequence = int(timeout/interval)
        for i in range(frequence):
            self.web_element = self.element()
            if self.web_element is  None:
                time.sleep(1)  
                return
            time.sleep(int(interval)) 
        else:
            Log.log_error_info("fail to wait element %s present.locator is %s\n" % (self.class_name,self.locator))  
        Log.log_step("等待元素消失．(元素位置：%s)"%(self.locator))
     
    def set_attribute(self, attribute, vaule):
        '''
        设置属性
        '''
        el = self.element()       
        self.driver.execute_script("arguments[0].setAttribute('%s' ,'%s)"%(attribute, vaule), el)
        Log.log_step("设置元素属性%s=%s.(元素位置：%s)"%(attribute,vaule,self.locator))             