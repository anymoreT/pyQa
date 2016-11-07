# -*- coding:utf-8 -*-

from .webElement import *
import pdb
from dianRongQa.log.log import Log
import time
from curses.ascii import NUL

class TableElement(WebElement):
    def __init__(self, element_type, locator):
        WebElement.__init__(self, element_type, locator)
    
    #表格中某一行列的文本
    def row_column_text_should_include(self, row, column, include_text):    
        cell_text = self.__find_element_by_row_column(row, column).text
        index = cell_text.find(include_text)
        if -1 == index:
            Log.log_error_info("%s  is not include %s, the real text is %s\n" % (self.class_name, include_text, cell_text))   
        Log.log_step("通过判断，表的%d行第%d列，包含文本:%s.(元素位置：%s)"%(row, column,include_text,self.locator)) 
 
   #判断表格中某一行列的文本不为空
    def row_column_text_should_not_null(self, row, column):    
        cell_text = self.__find_element_by_row_column(row, column).text
        if cell_text is not NUL:
            return True
        else:
            Log.log_error_info("未根据自动分配规则分配任务给电销")
   
    #返回整个表文本
    def get_table_text(self):
        return self.element().text
    
    #表包含特定文本
    def table_should_inculde_text(self,expected_text):
        table_text = self.get_table_text()
        index = table_text.find(expected_text)
        if -1 == index:
            Log.log_error_info("%s  is not include %s, the real text is %s\n" % (self.class_name, expected_text, table_text))   
        Log.log_step("通过判断，表的包含文本:%s.(元素位置：%s)"%(expected_text,self.locator)) 

    
    def get_row_text(self,row):
        return self.__find_element_by_row(row).text
    
    def get_row_column_text(self,row,column):  
        return self.__find_element_by_row_column(row, column).text
         
    def row_column_text_should_equal(self, row, column, text):    
        cell_text = self.get_row_column_text(row, column)
        if cell_text != text:
            Log.log_error_info("text  is not equal %s, the real text is %s\n" % (text,cell_text))   
        Log.log_step("通过判断，表的%d行第%d列，等于文本:%s.(元素位置：%s)"%(row, column,text,self.locator)) 

  
    def __find_element_by_row_column(self, row = 1, column = 1):
        return self.element().find_element_by_xpath(".//tbody//tr[%d]//td[%d]" % (row, column ))
    
    def __find_element_by_row(self, row = 1):
        return self.element().find_element_by_xpath(".//tbody//tr[%d]" % (row))
              
    def row_text_should_include(self,row, include_text):    
        cell_text = self.__find_element_by_row(row).text
        index = cell_text.find(include_text)
        if -1 == index:
            Log.log_error_info("%s  is not include %s, the real text is %s\n" % (self.class_name, include_text, cell_text))   
        Log.log_step("通过判断，表的%d行，包含文本:%s.(元素位置：%s)"%(row,include_text,self.locator)) 

    def row_text_should_equal(self,row,text):    
        cell_text = self.__find_element_by_row(row).text
        if cell_text != text:
            Log.log_error_info("%s  is not equal %s, the real text is %s\n" % (self.class_name,text, cell_text))   
        Log.log_step("通过判断，表的%d行等于文本:%s.(元素位置：%s)"%(row,text,self.locator)) 
   
            