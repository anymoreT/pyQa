# -*- coding:utf-8 -*-
import requests
import json
from dianRongQa.log.log import Log
import pdb
   
class HttpHandle(object):
    #数据类型定义
    TYPES = {"STRING" : str, "HASH" : dict, "INT" : int, "FLOAT" : float, "LIST" : list, "BOOL" : bool}
    def __init__(self):
        self.http_hander = requests.session()
        self.http_response = None
        self.status_code = None
        self.http_response_body = None
        self.http_payload = None
        self.http_request= None
      
     #获得正在处理的http session实例    
    def get_http_hanlder(self):
        return self.http_hander
    
     #设置正在处理的http session实例   
    def set_http_hanlder(self, http_handler):
        self.http_hander = http_handler

    def do_post_with_header(self, url, form_data=None, headers=None):
        pass
    
    #发送post请求，带data数据
    def do_post(self, url, form_data=None,):
        self.http_payload  = form_data
        self.http_request = url
        self.http_response = self.http_hander.post(self.http_request, data = self.http_payload) 
        return self.http_response
    
    #发送post请求，带json格式数据
    def do_post_with_json_payload(self, url, playload = None):
        json_data = playload
        #json_data =  json.dumps(playload)
        self.http_payload  = json_data
        self.http_request = url
        self.http_response = self.http_hander.post(self.http_request, json = self.http_payload) 
        return self.http_response
    
    #发送post请求，带json格式字符串数据
    def do_post_with_json_string_payload(self, url, playload = None):
        json_data =  json.loads(playload)
        self.http_payload  = json_data
        self.http_request = url
        self.http_response = self.http_hander.post(self.http_request, json = self.http_payload) 
        return self.http_response
    
    #get 请求
    def do_get(self, url):
        self.http_response = self.http_hander.get(url)
        return self.http_response
   
    #设置header　 
    def set_header(self, header_dic = None):
        self.http_hander.headers = header_dic
    
    #得到header　
    def get_header(self):
        return self.http_hander.headers 
    
    #更新header
    def update_header(self, header_dic):
        self.http_hander.headers.update(header_dic)
    
    #删除header    
    def delete_header(self, header_list):
        for key in header_list:
            del self.http_hander.headers[key]  
    
    #无参数get请求
    def do_get_with_no_paramter(self, request):
        self.http_response = self.http_hander.get(request) 
        return self.http_response
     
     #有参数get请求  
    def do_get_with_with_paramter(self, request, param):
        self.http_response = self.http_hander.get(request + "?%s"%(param))   
        return self.http_response
    
    #得到请求结果状态码
    def get_response_status_code(self):
        return self.http_response.status_code
     
      
    #得到响应文本 
    def get_response_body(self):
        if  isinstance(self.http_response.content, bytes):
            self.http_response_body = self.http_response.content.decode()
        else:
            self.http_response_body = self.http_response.content     
        return  self.http_response_body
    
    #打印结果
    def print_response_body(self): 
        Log.log_info(self.get_response_body())
        
    #将响应内容转换成python结构 
    def  conver_response_body_to_struct(self):
        #去除null,用None代替null,否则eval 不能处理
        response = None
        try :
            response = self.get_response_body().replace("null", "None")
            response = eval(response)       
        except :
            response = self.conver_json_str_response_to_struct()
        return   response 
    
    #将json格式文本响应内容转换成python结构 
    def  conver_json_str_response_to_struct(self):
        response = self.get_response_body()
        response =  json.loads(response)
        return response  
    
    #将response装换成dic,list等结构,并返回
    def get_response_struct(self):         
        return self.conver_response_body_to_struct()
     
    #检查状态码是指定的状态码
    def response_code_status_should_be(self, status_code):
        if status_code != self.get_response_status_code():
            Log.log_error_info("status  code should be %d, but the  real value is %d"%(status_code,self.get_response_status_code()))
        else:
            Log.log_info("Verify..., status code is ok.")    
         
    #检查响应文本是一个list格式     
    def response_body_should_be_list_struct(self):   
        if not isinstance(self.conver_response_body_to_struct(),  HttpHandle.TYPES['LIST']):
            Log.log_error_info("status code should be list")
        else:
            Log.log_info("Verify..., response struct is ok.")    
    
    #检查响应文本是一个dict格式  
    def response_body_should_be_dictionary_struct(self):   
        if not isinstance(self.conver_response_body_to_struct(), HttpHandle.TYPES['HASH']):
            Log.log_error_info("Verify..., response struct is not dictionary.")
        else:    
            Log.log_info("Verify..., response struct is ok.")  
    
    #只能比对第一层的dic
    #检查响应里面有指定字段
    def  response_dictionary_should_have_key(self, key): 
        dic =  self.conver_response_body_to_struct()
        if key not in dic:
            Log.log_error_info("Verify..., response key has no key: %s"%(key))
        else:
            Log.log_info("Verify..., response key is ok.")  
            
    #只能比对第一层的dic
     #检查响应里面有指定的list里面的字段
    def  response_dictionary_should_have_keys(self, key_list = []): 
        dic =  self.conver_response_body_to_struct()
        for key in key_list:
            if key not in dic:
                Log.log_error_info("Verify..., response key has no key: %s"%(key))
        else:
            Log.log_info("Verify..., response keys is ok.")     
            
                 
   
    #只能比对第一层的dic
    #检查响应里面有指定字段和内容
    def  response_dictionary_should_have_key_value(self, key, value): 
        dic =  self.conver_response_body_to_struct()
        if dic.get(key) != value:
            Log.log_error_info("Verify..., the response dictionary  value is %s, not %s"%(dic.get(key), value))
        else:
            Log.log_info("Verify..., response key,value is ok.")     
   
   
    #将response看出一串字符串  
    #响应文本包含指定的字符串
    def response_string_should_include(self, sub_string):
        if sub_string not in self.get_response_body():
            Log.log_error_info("Verify..., response string does no  inclue string: %s, real response is: %s"%(sub_string, self.get_response_body()))
        else:
            Log.log_info("Verify..., response content is ok.")  
     
    #可以检查检查响应的深层级字段的类型
    #kwargs: target_struct={}
    #e.g response_deep_key_is_struct("content", "list", 0,  target_struct = {"name" : "STRING", "type" :"HASH", "index" : "INT", "verify" : "BOOL"})
    def response_deep_key_is_struct(self, *args, **kwargs):
        target_struct = kwargs["target_struct"]
        content =  self.conver_response_body_to_struct()
        for key in args:
            content = content[key]
        for key,value in target_struct.items():
            if not  isinstance(content[key], HttpHandle.TYPES[value]):
                Log.log_error_info("Verify..., the type of key %s is not %s "%(key, value))
        Log.log_info("Verify..., response deep key type is ok.")  
    
    
    