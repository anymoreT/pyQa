# -*- coding:utf-8 -*-
from unittest import TestSuite,TestLoader
try:
    from dianRongQa.HTMLTestRunnerNB import HTMLTestRunnerNB
except ImportError:
    from HTMLTestRunnerNB import  HTMLTestRunnerNB
import os

def run_all_cases():
    current_dir = os.path.dirname(__file__)
    testSuit_path = os.path.join(current_dir, "unit_test")
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
    runner = HTMLTestRunnerNB(stream= file_handle, title="Demo123 testing result")    
    return runner
  
run_all_cases()    
 
   

