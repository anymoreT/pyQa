from .webElement import *
from selenium.webdriver.support.select import Select
from dianRongQa.log.log import Log

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
        self.bind()
        try:    
            return self.select_instance.first_selected_option
        except:
            Log.log_error_info("Couldn't get selected option %s \n")
    
    def selected_option_should_equal(self, option):
        selected_option =  self.get_selected_option().text.strip()
        if option != selected_option:
            Log.log_error_info("selected option  is %s, not %s \n"%(selected_option, option))
          
    def select_by_value(self, value):
        self.bind()
        try:
            self.select_instance.select_by_value(value)
        except:
            Log.log_error_info("Couldn't select option %s \n" % (value))

                
    def select_by_index(self,index =  1):
        self.bind()
        self.select_instance.select_by_index(index) 
        
    def select_by_option(self,option):
        self.bind()
        self.select_instance.select_by_visible_text(option)  