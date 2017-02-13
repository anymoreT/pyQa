# -*- coding:utf-8 -*-
import requests
import json
from pyQa.log.log import Log
import pdb
from unittest import TestCase
   
class HttpHandle(object):
    '''
    集成TestCase，主要是为了能够使用各种assert判定
    系统定义如下格式转意：
    TYPES = {"STRING" : str, "HASH" : dict, "INT" : int, "FLOAT" : float, "LIST" : list, "BOOL" : bool, "NULL": None}
    '''
    TYPES = {"STRING" : str, "HASH" : dict, "INT" : int, "FLOAT" : float, "LIST" : list, "BOOL" : bool, "NULL": None}
 
    def __init__(self):
        '''
        该类主要用户发送http请求，得到响应值，检查各种响应内容
        '''
        self.http_hander = requests.session()
        self.http_response = None
        self.status_code = None
        self.http_response_body = None
        self.http_payload = None
        self.http_request= None
      
    #获得正在处理的http session实例    
    def get_http_hanlder(self):
        '''
        当该类提供的方法不能满足实际的测试情况下，可以通过此方法，
        获得正在处理的http session实例，然后再进行自定义处理 
        '''
        return self.http_hander
    
    #更改URL,将指定参数替换{0},{1}
    def replace_paramter_for_url(self, url, *paramters):
        '''
        用参数替换url中的编号，生成正式的url
        eg.   url = "http://{0}/new/{2}?{3}", 该方法会用传入的参数替换{0} {1} {3}
        url最多支持３个可替换
        '''
        request_str = ""
        if len(paramters) == 1:
            request_str = url.format(paramters[0])
        elif  len(paramters) == 2:
            request_str = url.format(paramters[0],paramters[1])
        elif  len(paramters) == 3:
            request_str = url.format(paramters[0],paramters[1],paramters[2])    
        else:
            return request_str
        return request_str
    
    #设置正在处理的http session实例   
    def set_http_hanlder(self, http_handler):
        '''
        将外部的request.session(),设置到类里，供类使用
        '''
        self.http_hander = http_handler

    #发送post请求，带data数据
    def do_post(self, url,  data=None, **kwargs):
        '''
        发送post请求，且使用data作为playload参数
        '''
        self.http_payload  = data
        self.http_request = url
        self.http_response = self.http_hander.post(self.http_request, data = self.http_payload,**kwargs) 
        Log.log_step("发送post请求，请求是:%s"%(url))     
        return self.http_response
    
    #发送post请求，带json格式数据
    def do_post_with_json_payload(self, url, json = None,  **kwargs):
        #json_data =  json.dumps(playload)
        '''
        发送json格式post请求
        '''
        self.http_payload  = json
        self.http_request = url
        self.http_response = self.http_hander.post(self.http_request, json = self.http_payload, **kwargs)
        Log.log_step("发送post请求，请求是:%s" % (url))
        return self.http_response
    
    #发送post请求，带json格式字符串数据
    def do_post_with_json_string_payload(self, url, playload = None, **kwargs):
        '''
        发送json格式字符串post请求
        '''
        self.http_payload  =  json.loads(playload)
        self.http_request = url
        self.http_response = self.http_hander.post(self.http_request, json = self.http_payload, **kwargs)
        Log.log_step("发送post请求，请求是:%s" % (url))
        return self.http_response

    #get 请求
    def do_get(self, url, **kwargs):
        '''
        发送get请求
        '''
        self.http_response = self.http_hander.get(url, **kwargs)
        Log.log_step("发送get请求，请求是:%s"%(url))   
        return self.http_response
   
    #设置header　 
    def set_header(self, header_dic = None):
        '''
        设置请求header,header是一个hash格式
        '''
        self.http_hander.headers = header_dic
    
    #得到header　
    def get_header(self):
        '''
        得到请求header
        '''
        return self.http_hander.headers 
    
    #更新header
    def update_header(self, header_dic):
        '''
        更新header,更新的是一个dictionary格式
        '''
        self.http_hander.headers.update(header_dic)
    
    #删除header    
    def delete_header(self, header_list):
        '''
        删除header,heder_list是一个list
        '''
        for key in header_list:
            del self.http_hander.headers[key]  
    
#     #无参数get请求
#     def do_get_with_no_paramter(self, request):
#         self.http_response = self.http_hander.get(request) 
#         return self.http_response
     
     #有参数get请求  
    def do_get_with_with_paramter(self, request, param, **kwargs):
        '''
        发送get请求，可以带参数字符串
        eg. url="http://baidu.com" param=new
        发送实际的
        '''
        self.http_response = self.http_hander.get(request + "?%s"%(param), **kwargs)   
        return self.http_response
    
    #得到请求结果状态码
    def get_response_status_code(self):
        '''
        得到请求结果码
        '''
        return self.http_response.status_code
     
      
    #得到响应文本 
    def get_response_body(self):
        '''
        得到发送请求的结果
        '''
        if  isinstance(self.http_response.content, bytes):
            self.http_response_body = self.http_response.content.decode()
        else:
            self.http_response_body = self.http_response.content     
        return  self.http_response_body
    
    #打印原始数据结果
    def print_response_body(self):
        '''
        打印结果
        '''
        Log.log_info(self.get_response_body())

    #打印转换成python结构的结果
    def print_response_python_strcut_body(self):
        '''
        打印转换成python结构的结果
        '''
        Log.log_info(str(self.get_response_struct()))
        
    #将响应内容转换成python结构 
    def  conver_response_body_to_struct(self):
        '''
        #去除null,用None代替null,否则eval 不能处理
        将响应文本结果，转换成python的数据格式
        注意：如果返回的结果是null,这转换后用None代替；如果结果是true,那么会变成True
        '''
        response = None
        try :
            response = self.get_response_body().replace("null", "None")
            response = eval(response)       
        except :
            response = self.conver_json_str_response_to_struct()
        return   response 
    
    #将json格式文本响应内容转换成python结构 
    def  conver_json_str_response_to_struct(self):
        '''
        将响应是json字符串的文本转换成python格式
        '''
        response = self.get_response_body()
        response =  json.loads(response)
        return response  
    
    #将response装换成dic,list等结构,并返回
    def get_response_struct(self):    
        '''
        获得响应问题的python格式．就是将字符串转成python格式
        '''     
        return self.conver_response_body_to_struct()
    
    
     #将response装换成json结构,并返回
    def get_response_json_struct(self):     
        '''
        获得json格式的响应
        '''    
        return self.conver_json_str_response_to_struct()
     
    #检查状态码是指定的状态码
    def response_code_status_should_be(self, status_code):
        '''
        判断响应的状态码是否是指定的状态码，不是就报错
        '''
        if status_code != self.get_response_status_code():
            Log.log_error_info("status code should be %d, but the  real value is %d"%(status_code,self.get_response_status_code()))
        else:
            Log.log_info("Verify..., status code is ok.")
        Log.log_step("检查状态码是:%d" % (status_code))

    #检查响应文本是一个list格式     
    def response_body_should_be_list_struct(self):   
        '''
        判断响应是list格式，否则报错
        '''
        if not isinstance(self.conver_response_body_to_struct(),  HttpHandle.TYPES['LIST']):
            Log.log_error_info("status code should be list")
        else:
            Log.log_info("Verify..., response struct is ok.")
        Log.log_step("检查响应是list结构")

    
    #检查响应文本是一个dict格式  
    def response_body_should_be_dictionary_struct(self):   
        '''
        判断响应是dictionary格式，否则报错
        '''
        if not isinstance(self.conver_response_body_to_struct(), HttpHandle.TYPES['HASH']):
            Log.log_error_info("Verify..., response struct is not dictionary.")
        else:    
            Log.log_info("Verify..., response struct is ok.")
        Log.log_step("检查响应是HASH结构")
    
    #只能比对第一层的dic
    #检查响应里面有指定字段
    def  response_dictionary_should_have_key(self, key): 
        '''
        判断响应的格式有指定字段
        '''
        dic =  self.conver_response_body_to_struct()
        if key not in dic:
            Log.log_error_info("Verify..., response key has no key: %s"%(key))
        else:
            Log.log_info("Verify..., response key is ok.")
        Log.log_step("检查响应含有字段:%s"%(key))
            
    #只能比对第一层的dic
    #检查响应里面有指定字段
    def  response_dictionary_should_not_have_key(self, key): 
        '''
        判断响应的格式有指定字段
        '''
        dic =  self.conver_response_body_to_struct()
        if key  in dic:
            Log.log_error_info("Verify..., response key has  key: %s"%(key))
        else:
            Log.log_info("Verify...,ok, response has not key..")
        Log.log_step("检查响应不含有字段:%s" % (key))
                        
    #只能比对第一层的dic
     #检查响应里面有指定的list里面的字段
    def  response_dictionary_should_have_keys(self, key_list = []): 
        '''
        判断响应的格式有指定的字段集合
        '''
        dic =  self.conver_response_body_to_struct()
        for key in key_list:
            if key not in dic:
                Log.log_error_info("Verify..., response key has no key: %s"%(key))
        else:
            Log.log_info("Verify..., response keys is ok.")
        Log.log_step("检查响应含有这些字段:%s" % (key_list))

    #只能比对第一层的dic
     #检查响应里面有指定的list里面的字段
    def  response_dictionary_should_have_not_keys(self, key_list = []): 
        '''
        判断响应的格式有指定的字段集合
        '''
        dic =  self.conver_response_body_to_struct()
        for key in key_list:
            if key  in dic:
                Log.log_error_info("Verify..., response key has  key: %s"%(key))
        else:
            Log.log_info("Verify..., ok, response has not keys .")
        Log.log_step("检查响应不含有这些字段:%s" % (key_list))
   
    #只能比对第一层的dic
    #检查响应里面有指定字段和内容
    def  response_dictionary_should_have_key_value(self, key, value): 
        '''
        判断响应的指定字段的内容是指定的内容
        '''
        dic =  self.conver_response_body_to_struct()
        if dic.get(key) != value:
            Log.log_error_info("Verify..., the response dictionary  value is %s, not %s"%(dic.get(key), value))
        else:
            Log.log_info("Verify..., response key,value is ok.")
        Log.log_step("检查响应含有字段:%s,值为%s" % (key,value))
   
    #将response看出一串字符串  
    #响应文本包含指定的字符串
    def response_string_should_include(self, sub_string):
        '''
        判断响应字符串是否包含指定的字符串
        '''
        if sub_string not in self.get_response_body():
            Log.log_error_info("Verify..., response string does no  inclue string: %s, real response is: %s"%(sub_string, self.get_response_body()))
        else:
            Log.log_info("Verify..., response content is ok.")
        Log.log_step("检查响应含有字符串:%s" % ( sub_string))
   
     #将response看出一串字符串  
    #响应文本不包含指定的字符串
    def response_string_should_not_include(self, sub_string):
        '''
        判断响应字符串不包含指定的字符串
        '''
        if sub_string  in self.get_response_body():
            Log.log_error_info("Verify..., response string does   inclue string: %s, real response is: %s"%(sub_string, self.get_response_body()))
        else:
            Log.log_info("Verify..., response content is ok.")
        Log.log_step("检查响应不含有字符串:%s" % (sub_string))
     
    #检查响应的各个层级字段的类型
    #kwargs: target_struct={}
    #e.g response_keys_type_check("content", "list", 0,  target_struct = {"name" : "STRING", "type" :"HASH", "index" : "INT", "verify" : "BOOL"})
    #e.g response_keys_type_check(target_struct = {"name" : "STRING", "type" :"HASH", "index" : "INT", "verify" : "BOOL"})
    def response_keys_type_is_right(self, *args, **kwargs):
        '''
        判断响应的python格式的指定字段格式如target_struct指定的格式．
        eg.  response_keys_type_check("content", "list", 0,  target_struct = {"name" : "STRING", "type" :"HASH", "index" : "INT", "verify" : "BOOL"})
        #e.g response_keys_type_check(target_struct = {"name" : "STRING", "type" :"HASH", "index" : "INT", "verify" : "BOOL"})
        该结果表示将结果的result['content']['list'][0]同target_struct指定的字段和类型做对比
        '''
        target_struct = kwargs["target_struct"]
        content =  self.conver_response_body_to_struct()
        for key in args:
            content = content[key]
        for key,value in target_struct.items():
            #类型是None,需要特别处理
            if value == "NULL":
                if content[key] is not None:
                    Log.log_error_info("Verify..., the type of key %s is not None type"%(key))
            else:        
                if not  isinstance(content[key], HttpHandle.TYPES[value]):
                    Log.log_error_info("Verify..., the type of key %s is not %s "%(key, value))
        Log.log_info("Verify..., response deep key type is ok.")
        Log.log_step("检查响应结构内容符合指定内容" )

    #检查响应的各层级字段的内容
    #kwargs: target_struct={}
    #e.g response_deep_key_is_struct("content", "list", 0,  target_value = {"name" : "benhuang",  "index" : "7", "verify" : "true"})
    # e.g response_deep_key_is_struct(target_value = {"name" : "benhuang",  "index" : "7", "verify" : "true"})
    def response_key_value_is_right(self, *args, **kwargs):
        '''
        判断响应的python格式的指定字段格式如target_struct指定的格式．
        eg.  response_deep_key_is_struct("content", "list", 0,  target_value = {"name" : "benhuang",  "index" : "7", "verify" : "true"})
        该结果表示将结果的result['content']['list'][0]同target_struct指定的字段与响应结果做对比
        '''
        target_struct = kwargs["target_value"]
        content =  self.conver_response_body_to_struct()
        for key in args:
            content = content[key]
        for key,value in target_struct.items():
                if content[key] != value:
                    Log.log_error_info("Verify..., the value of key %s is not %s,it is %s "%(key, value,content[key]))
        Log.log_info("Verify..., response deep key,value  is ok.")
        Log.log_step("检查响应结构符合指定格式要求，且内容正确")