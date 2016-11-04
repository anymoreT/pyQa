# -*- coding:utf-8 -*-
from unittest import TestSuite,TestLoader
import sys
import os
import dianRongQa
print(os.getcwd())
from dianRongQa.HTMLTestRunnerNB import  HTMLTestRunnerNB




 
def run_all_cases():
    current_dir = os.path.dirname(__file__)
    testSuit_path = os.path.join(current_dir, "dianRongQa", "unit_test")
    all_suits = TestLoader().discover(testSuit_path)
    run_suit(all_suits)
  
def run_suit(suit):
    root_path = os.path.dirname(".")
    root_path = os.path.join(root_path)
    filename = 'result.html'
    report_path = os.path.join(root_path, filename)
    file_handle= open(report_path, 'wb')
    runner = get_runner(file_handle)
    runner.run(suit)
   
def get_runner(file_handle):
    runner = HTMLTestRunnerNB(stream= file_handle, title="Demotesting result")    
    return runner
   
run_all_cases()    
  
    
# if __name__ == "main":
#     print("test")
