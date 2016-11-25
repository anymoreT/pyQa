import unittest
import sys
from pyQa.log.log import Log
class ReportTest(unittest.TestCase):
    def setUp(self):
        print("setup")
     
    def tearDown(self):
        print("tearDown")
        

    def test_report(self):
        Log.log_case_desc("TC001:这个case是生产报告")
        print(sys.stdout,"<STEP_BEGIN>%s<STEP_END>"%("点击元素: //a['登陆']1"))
        print(sys.stdout,"<STEP_BEGIN>%s<STEP_END>"%("等待元素://a['登陆']1"))

        
        
    def test_report1(self):
        Log.log_case_desc("TC002:/api/test/case/10001:8080/news")
        print(sys.stdout,"<STEP_BEGIN>%s<STEP_END>"%("等待元素:(xpath: //div/html/div[1]/a[contains(text(),'点击上传')]//a['登陆'])"))
 