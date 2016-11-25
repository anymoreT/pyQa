# -*- coding:utf-8 -*-
from pyQa.web.webElement import *
import pdb
class FileTextInputElement(WebElement):
    def __init__(self, element_type, locator):
        WebElement.__init__(self, element_type, locator)
     
    def set_display_property(self):
        el = self.element()
        self.driver.execute_script("arguments[0].setAttribute('style' ,'display:inline')", el)     