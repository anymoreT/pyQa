# -*- coding:utf-8 -*-
from .webElement import WebElement

class ButtonElement(WebElement):
    def __init__(self, element_type, locator):
        WebElement.__init__(self, element_type, locator)