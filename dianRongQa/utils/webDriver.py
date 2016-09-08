# -*- coding:utf-8 -*-
from selenium import webdriver
from dianRongQa.global_list.global_var import Global_factory
#from sqlalchemy.sql.sqltypes import Interval
import time
from selenium.webdriver.chrome.options import Options
from dianRongQa.log.log import Log

class WebDriver(object):
    driver = None
    @staticmethod
    def start_driver(brower = 'chrome' ):
        '''
        启动driver，默认是chrome
        '''
        if brower  == 'chrome' :
#             chromeOptions = Options()
#             prefs = {'profile.default_content_settings.multiple-automatic-downloads': 1, 'download.prompt_for_download' : False, 'download.default_directory' : "d:"}
#             chromeOptions.add_experimental_option("prefs", prefs)
#             WebDriver.driver = webdriver.Chrome(chrome_options = chromeOptions)
            WebDriver.driver = webdriver.Chrome()
        else:   
            profile = webdriver.FirefoxProfile() 
            #bug造成每次访问firefox必须访问Mozilla网站．等待其他版本
            #profile.set_preference("xpinstall.signatures.required", False);
#             profile.set_preference("app.support.baseURL", "https://www.baidu.com")
#             profile.set_preference("app.update.url.manual", "https://www.baidu.com")
#             profile.set_preference("app.update.url.details", "https://www.baidu.com")

#             profile.set_preference( "startup.homepage_welcome_url",  "about:startpage")
#             profile.set_preference( "browser.startup.homepage",  "about:startpage")
           # profile.set_preference()
            WebDriver.driver = webdriver.Firefox(firefox_profile=profile)
     
        WebDriver.driver.maximize_window()
        Global_factory.set_driver(WebDriver.driver)
     

            
    @staticmethod
    def go_to_url(url):
        '''
        进入指定网页
        '''
        WebDriver.driver.get(url)
        
    @staticmethod    
    def wait_page_load(timeout = 30, interval = 3):
        times = int(timeout/interval)
        for i in range(times):
            if "complete" == WebDriver.driver.execute_script('return document.readyState'):
                time.sleep(2)
                return True
            else:
                time.sleep(interval)  
        else:
            raise("page is still loading")           
        #WebDriver.driver.wait_for_page_to_load()
        
    @staticmethod
    def refresh_page():
        '''
        刷新页面
        '''
        WebDriver.driver.refresh()
        
    @staticmethod
    def quit():
        '''
        关闭driver
        '''
        try :
            WebDriver.driver.quit()
        except:
            Log.log_error_info("+++++close driver meet error" )     
        
    @staticmethod
    def get_cookie():
        pass
    
    @staticmethod
    def del_all_cookie():
        '''
        删除所有的cookies
        '''
        WebDriver.driver.delete_all_visible_cookies()
    
    @staticmethod
    def back(self):
        '''
        回退到上一页
        '''
        WebDriver.driver.go_back()
    
    @staticmethod
    def switch_to_frame(frame_name):
        """
         :Usage:
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        """
        WebDriver.driver.switch_to_frame(frame_name)
     
    @staticmethod   
    def get_window_handles():
        '''
        获得当前driver打开的所有tab
        '''
        return WebDriver.driver.window_handles
    
    @staticmethod     
    def switch_to_window(window):
        '''
        切换到指定的tab窗口
        '''
        WebDriver.driver.switch_to.window(window)    