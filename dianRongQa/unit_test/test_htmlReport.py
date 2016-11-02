import unittest
import sys
import logging
class ReportTest(unittest.TestCase):
    def setUp(self):
        print("setup")
     
    def tearDown(self):
        print("tearDown")
        

    def test_report(self):
        print(sys.stdout,"<STEP_BEGIN>%s<STEP_END>"%("点击元素: //a['登陆']"))
        print(sys.stdout,"<STEP_BEGIN>%s<STEP_END>"%("等待元素://a['登陆']"))

        
        
    def test_report1(self):
        print(sys.stdout,"<STEP_BEGIN>%s<STEP_END>"%("等待元素:(xpath: //div/html/div[1]/a[contains(text(),'点击上传')]//a['登陆'])"))
 