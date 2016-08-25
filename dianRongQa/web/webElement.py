# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from dianRongQa.global_list.global_var import Global_factory
# -*- coding:utf-8 -*-
from unittest import TestCase
from dianRongQa.log.log import Log
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement
import time
import pdb
class WebElement(object):
    def __init__(self, element_type, locator):
        self.type = element_type
        self.locator = locator
        self.driver = Global_factory.get_driver()
        self.action = ActionChains(self.driver)
        self.web_element = self.element()
        self.class_name = str(self.__class__)
      
    def element(self): 
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
        return  self.web_element   
     
    #input_type:  None, js 
    def input(self, str="", input_type = None):
        try:
            if (input_type == "js") or (input_type == "JS"):
                self.driver.execute_script("arguments[0].value='%s'"%  (str), self.get_element())
            else:    
                self.clear()
                self.web_element.send_keys(str)
        except:
            Log.log_error_info("Couldn't input %s for %s\n" % (str, self.class_name))
    
    def clear(self):
        try:
            self.web_element.clear()
        except:
            Log.log_error_info("Couldn't clear %s\n" % (self.class_name))
    #click_type: None, js   
    def click(self, click_type = None):
        try:
            if (click_type == "js") or (click_type == "JS"):
                self.driver.execute_script("arguments[0].click()", self.get_element())
            else:    
                self.web_element.click()
        except:
            Log.log_error_info("fail to  click %s\n" % (self.class_name))

    def send_tab_key(self):
        try:
            self.web_element.send_keys(Keys.TAB)
        except:
            Log.log_error_info("fail to  send tab key for %s\n" % (self.class_name))   
     
    def send_enter_key(self):
        try:
            self.web_element.send_keys(Keys.ENTER)
        except:
            Log.log_error_info("fail to  send tab key for %s\n" % (self.class_name))         
    
    def is_exist(self):
        try:
            return self.web_element.is_displayed()
        except:
            return False 
    
    def should_not_enable(self):
        if self.get_element().is_enabled():
            Log.log_error_info("%s should not be enable\n" % (self.class_name))   
 
    def should_enable(self):
        if not self.get_element().is_enabled():
            Log.log_error_info("%s should be enable\n" % (self.class_name))   
    
    def wait_element_enable(self, timeout =  30, interval = 2):
        frequence  =  int(timeout/interval)
        for i in range(frequence):
            self.web_element = self.element()
            if self.web_element.is_enabled(): 
                time.sleep(int(interval))
                return
            time.sleep(int(interval)) 
        else:
            Log.log_error_info("fail to wait element %s enable\n" % (self.class_name))           
    
    def get_text(self):
        try:
            #实际使用中发现，需要等待2秒才能稳定得到文本
            time.sleep(2) 
            return self.web_element.text 
        except:
            Log.log_error_info("fail to get text for %s\n" % (self.class_name))  
            
    def wait_element_present(self, timeout =  30, interval = 2):
        frequence = int(timeout/interval)
        for i in range(frequence):
            self.web_element = self.element()
            if self.web_element is not None:
                time.sleep(1)  
                return
            time.sleep(int(interval)) 
        else:
            Log.log_error_info("fail to wait element %s present.locator is %s\n" % (self.class_name,self.locator))  
    
    def should_exist(self):
        try:
            is_displayed = self.web_element.is_displayed()
            if not is_displayed:
                Log.log_error_info("%s is not existed\n" % (self.class_name))   
        except:
            Log.log_error_info("%s is has not display method\n" % (self.class_name))   


    def should_not_exist(self):
        element = self.element()
        if element is None:
            return True
        else:
            is_displayed = element.is_displayed()
            if is_displayed:
                Log.log_error_info("%s is existed\n" % (self.class_name))   
            else:
                return True

    def should_include_text(self, include_text):   
        text = self.get_text()
        index = text.find(include_text)
        if -1 == index:
            Log.log_error_info("%s  is not include %s, the real text is %s\n" % (self.class_name, include_text, text))   
       
                  
    def should_not_include_text(self, include_text):
        text = self.get_text()
        index = text.find(include_text)
        if -1 != index:
            Log.log_error_info("%s include %s, the real text is %s\n" % (self.class_name, include_text, text)) 
    
    def should_equal_text(self, expected_text):   
        text = self.get_text()
        if text != expected_text:
            Log.log_error_info("%s  is not equal  %s, the real text is %s\n" % (expected_text, text, self.class_name))   
         
    def mouse_over(self):
        self.action.move_to_element(self.get_element())   
        self.action.perform()  
        time.sleep(2)             
        
    def wait_element_disappear(self, timeout =  30, interval = 2):
        frequence = int(timeout/interval)
        for i in range(frequence):
            self.web_element = self.element()
            if self.web_element is  None:
                time.sleep(1)  
                return
            time.sleep(int(interval)) 
        else:
            Log.log_error_info("fail to wait element %s present.locator is %s\n" % (self.class_name,self.locator))  
            
                