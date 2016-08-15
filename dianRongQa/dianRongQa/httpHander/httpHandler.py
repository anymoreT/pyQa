# -*- coding:utf-8 -*-
import requests
import json
from dianRongQa.log.log import Log
   
class HttpHandle(object):
    def __init__(self):
        self.http_hander = requests.session()
        self.http_response = None
        self.status_code = None
        self.http_response_body = None
        self.http_payload = None
        self.http_request= None
        
    def get_http_hanlder(self):
        return self.http_hander
    
    def set_http_hanlder(self, http_handler):
        self.http_hander = http_handler

    def do_post_with_header(self, url, form_data=None, headers=None):
        pass
    
    def do_post(self, url, form_data=None,):
        self.http_payload  = form_data
        self.http_request = url
        self.http_response = self.http_hander.post(self.http_request, data = self.http_payload) 
        return self.http_response
    
    def do_post_with_json_payload(self, url, playload = None):
        json_data = playload
        #json_data =  json.dumps(playload)
        self.http_payload  = json_data
        self.http_request = url
        self.http_response = self.http_hander.post(self.http_request, json = self.http_payload) 
        return self.http_response
    
    def do_post_with_json_string_payload(self, url, playload = None):
        json_data =  json.loads(playload)
        self.http_payload  = json_data
        self.http_request = url
        self.http_response = self.http_hander.post(self.http_request, json = self.http_payload) 
        return self.http_response
    
    def do_get(self, url):
        self.http_response = self.http_hander.get(url)
        return self.http_response
    
    def set_header(self, header_dic = None):
        self.http_hander.headers = header_dic
    
  
    def get_header(self):
        return self.http_hander.headers 
    
    def update_header(self, header_dic):
        self.http_hander.headers.update(header_dic)
        
    def delete_header(self, header_dic):
        for key in header_dic.keys():
            del self.http_hander.headers[key]  
    
    def do_get_with_no_paramter(self, request):
        self.http_response = self.http_hander.get(request) 
        return self.http_response
       
    def do_get_with_with_paramter(self, request, param):
        self.http_response = self.http_hander.get(request + "?%s"%(param))   
        return self.http_response
    
    def get_resonse_status_code(self):
        return self.http_response.status_code
     
    #得到响应文本 
    def get_resonse_body(self):
        if  isinstance(self.http_response.content, bytes):
            self.http_response_body = self.http_response.content.decode()
        else:
            self.http_response_body = self.http_response.content     
        return  self.http_response_body
    
    #打印结果
    def print_response_body(self): 
        Log.log_info(self.get_resonse_body())
        
    #将响应内容转换成python结构 
    def  conver_response_body_to_struct(self):
        #去除null,用None代替null,否则eval 不能处理
        response = self.get_resonse_body().replace("null", "None")
        return eval(response)       
    
    #将response装换成dic,list等结构,并返回
    def get_response_struct(self):         
        return self.conver_response_body_to_struct()
     
    def reponse_code_status_should_be(self, status_code):
        if status_code != self.get_resonse_status_code():
            Log.log_error_info("status  code should be %d, but the  real value is %d"%( status_code),self.get_resonse_status_code())
        else:
            Log.log_info("Verify..., status code is ok.")    
         
    def response_body_should_be__list_struct(self):   
        if not isinstance(self.conver_response_body_to_struct(), dict):
            Log.log_error_info("status  code should be dictionary")
        else:
            Log.log_info("Verify..., response struct is ok.")    
    
    def response_body_should_be_dictionary_struct(self):   
        if not isinstance(self.conver_response_body_to_struct(), dict):
            Log.log_error_info("Verify..., response struct is not dictionary.")
        else:    
            Log.log_info("Verify..., response struct is ok.")  
    
    #只能比对第一层的dic
    def  response_dictionary_should_have_key(self, key): 
        dic =  self.conver_response_body_to_struct()
        if key not in dic:
            Log.log_error_info("Verify..., response key has no key: %s"%(key))
        else:
            Log.log_info("Verify..., response key is ok.")  
            
    #只能比对第一层的dic
    def  response_dictionary_should_have_keys(self, key_list = []): 
        dic =  self.conver_response_body_to_struct()
        for key in key_list:
            if key not in dic:
                Log.log_error_info("Verify..., response key has no key: %s"%(key))
        else:
            Log.log_info("Verify..., response keys is ok.")     
            
                 
   
    #只 能比对第一层的dic
    def  response_dictionary_should_have_key_value(self, key, value): 
        dic =  self.conver_response_body_to_struct()
        if dic.get(key) != value:
            Log.log_error_info("Verify..., the response dictionary  value is %s, not %s"%(dic.get(key), value))
        else:
            Log.log_info("Verify..., response key,value is ok.")     
   
   
    #将response看出一串字符串  
    def response_string_should_include(self, sub_string):
        if sub_string not in self.get_resonse_body():
            Log.log_error_info("Verify..., response string does no  inclue string: %s, real response is: %s"%(sub_string, self.get_resonse_body()))
        else:
            Log.log_info("Verify..., response content is ok.")  
             
    def resonse_body_equal(self,  right_response):
        if right_response != self.get_resonse_body():
            Log.log_error_info("Verify..., response string does no  equal string: %s"%(right_response))
        else:
            Log.log_info("Verify..., response content is ok.")  
    
    
    
    
    
    