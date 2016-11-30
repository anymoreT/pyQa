from .WebElement import *
from selenium.webdriver.support.select import Select
from pyQa.log.log import Log

class SelectElement(WebElement):
    def __init__(self, element_type, locator):
        WebElement.__init__(self, element_type, locator)
        self.select_instance = None
    
    def bind(self):
        if self.select_instance == None:
            self.select_instance = Select(self.get_element())  
         
    def get_options(self):
        self.bind()
        try:    
            return self.select_instance.options()   
        except:
            Log.log_error_info("Couldn't get option %s \n")
         
    def get_selected_option(self):
        '''
        获得当前选中的条目
        '''     
        self.bind()
        try:    
            return self.select_instance.first_selected_option
        except:
            Log.log_error_info("Couldn't get selected option %s \n")
    
    def selected_option_should_equal(self, option):
        '''
        比对选中的条目符合特定的选项
        '''
        selected_option =  self.get_selected_option().text.strip()
        if option != selected_option:
            Log.log_error_info("selected option  is %s, not %s \n"%(selected_option, option))
        Log.log_step("下拉框元素当前选中为: %s．(元素位置：%s)"%(option, self.locator))
          
    def select_by_value(self, value):
        '''
        选中指定的内容项
        '''
        self.bind()
        try:
            self.select_instance.select_by_value(value)
        except:
            Log.log_error_info("Couldn't select option %s \n" % (value))
        Log.log_step("下拉框元素选中: %s．(元素位置：%s)"%(value, self.locator))

                
    def select_by_index(self,index =  1):
        '''
        选中指定的index项
        '''
        self.bind()
        self.select_instance.select_by_index(index) 
        Log.log_step("下拉框元素选中位置为%d的选项．(元素位置：%s)"%(index, self.locator))
         
    def select_by_option(self,option):
        '''
        选中指定的文本项目
        '''
        self.bind()
        self.select_instance.select_by_visible_text(option)  
        Log.log_step("下拉框元素选中: %s．(元素位置：%s)"%(option, self.locator))