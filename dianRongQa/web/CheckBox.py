# -*- coding:utf-8 -*-
from dianRongQa.web.webElement import WebElement
from dianRongQa.log.log import Log

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
            
    def make_selected(self): 
        if not self.is_selected():
            self.click()  
        if not self.is_selected():
            Log.log_error_info("couldn't make %s select"%(self.class_name))             