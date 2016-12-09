# -*- coding:utf-8 -*-
from pyQa.web.WebElement import WebElement
from pyQa.log.log import Log

class CheckBoxElement(WebElement):
    def __init__(self, element_type, locator):
        WebElement.__init__(self, element_type, locator)
    
    def is_selected(self):
        return self.get_element().is_selected()   
        
    
    def make_un_selected(self): 
        if self.is_selected():
            self.click()  
        if self.is_selected():
            Log.log_error_info("couldn't make %s un-select"%(self.class_name))  
        Log.log_step("不选中复选框元素．(元素位置：%s)"%(self.locator))   
            
    def make_selected(self): 
        if not self.is_selected():
            self.click()  
        if not self.is_selected():
            Log.log_error_info("couldn't make %s select"%(self.class_name))  
        Log.log_step("不选中复选框元素．(元素位置：%s)"%(self.locator))             