# -*- coding:utf-8 -*-
from pyQa.web.webElement import *
import pdb
class TextInputElement(WebElement):
    def __init__(self, element_type, locator):
      WebElement.__init__(self, element_type, locator)