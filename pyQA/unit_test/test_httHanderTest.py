# -*- coding:utf-8 -*-

from  unittest import TestCase
from pyQa.httpHander import httpHandler
import json
from requests.models import Response
import pdb
from pyQa.log.log import Log


def test_replace_paramter_for_url():
    origin_url = "http://www.baidu/{0}"
    instance = httpHandler.HttpHandle()
    parm0 = "news"
    new_url = instance.replace_paramter_for_url(origin_url, parm0)
    TestCase().assertTrue("http://www.baidu/news" == new_url)
    
    origin_url = "http://www.baidu/{0}/test/{1}"
    parm0 = "news"
    parm1 = "auto"
    new_url = instance.replace_paramter_for_url(origin_url, parm0, parm1)
    TestCase().assertTrue("http://www.baidu/news/test/auto" == new_url)
    
    origin_url = "http://www.baidu/{0}/test/{1}?name={2}"
    parm0 = "news"
    parm1 = "auto"
    parm2 = "ben"
    new_url = instance.replace_paramter_for_url(origin_url, parm0, parm1,parm2)
    TestCase().assertTrue("http://www.baidu/news/test/auto?name=ben" == new_url)
    Log.log_info("test_replace_paramter_for_url is ok")

    
def tes_resonse_deep_key_is_struct():
    '''
    #可以验证如下的类型
    #TYPES = {"STRING" : str, "HASH" : dict, "INT" : int, "FLOAT" : float, "LIST" : list, "BOOL" : bool}
    '''
    content = b'{"content": {"list": [{"name": "string", "birthday":null,"index":1,"verify":true, "type": { "name": "string","parent": null,"path": "string","description": "string", "title": true,"order": 0,"icon": "string" },"hot": true,"platform": [  "desktop" ], "from": "string", "until": "string", "locale": "string", "staticLink": "string", "thumbnail": "string", "content": "string", "htmlContent": "string", "description": "string" }],"totalRecords": 0},"result": "string","errors": ["string"]}'
    response = Response()
    setattr(response, '_content',  content)
    instance = httpHandler.HttpHandle()
    instance.http_response = response
    instance.response_deep_key_is_struct(target_struct = {"content" : "HASH", "result" :"STRING", "errors" : "LIST"})
    instance.response_deep_key_is_struct("content", "list", 0,  target_struct = {"name" : "STRING", "type" :"HASH", "birthday":"NULL","index" : "INT", "verify" : "BOOL"})

def response_deep_key_value_is_right():
    '''
    #可以数据正确性
    '''
    content = '{"data": {"name":"黄勇","info":[{"id":12345,"gender":null}]} }'
    response = Response()
    setattr(response, '_content',  content)
    instance = httpHandler.HttpHandle()
    instance.http_response = response
    instance.print_response_body()
    instance.get_response_struct()
    instance.response_deep_key_value_is_right("data", target_value= {"name" :"黄勇"})
    instance.response_deep_key_value_is_right("data", "info", 0, target_value= {"id":12345})
    instance.response_deep_key_value_is_right("data", "info", 0, target_value= {"id":12345,"gender":None})
    instance.response_deep_key_value_is_right("data", target_value=  {"name":"黄勇","info":[{"id":12345,"gender":None}]})



def test_get_response_body():
        content = b'{"content": true, "int":1}'
        response = Response()
        setattr(response, '_content',  content)
        instance = httpHandler.HttpHandle()
        instance.http_response = response
        TestCase().assertTrue( '{"content": true, "int":1}' == instance.get_response_body())
        
        content = b'{"content": true, "int":1, "list:[]"}'
        response = Response()
        setattr(response, '_content',  content)
        instance = httpHandler.HttpHandle()
        instance.http_response = response
        TestCase().assertTrue('{"content": true, "int":1, "list:[]"}' == instance.get_response_body())
        Log.log_info("test_get_resonse_body is ok")
        
def test_print_response_body():
        content = b'{"content": true, "int":1}'
        response = Response()
        setattr(response, '_content',  content)
        instance = httpHandler.HttpHandle()
        instance.http_response = response
        instance.print_response_body()
        Log.log_info("test_print_response_body is ok")
        
def test_get_header():
        response = Response()
        instance = httpHandler.HttpHandle()
        instance.http_response = response
        header_dic = {"content-type":"text/html"}
        instance.set_header(header_dic)    
        TestCase().assertTrue(header_dic== instance.get_header())
        Log.log_info("test_get_header is ok")
         
         
def test_update_header():
        response = Response()
        instance = httpHandler.HttpHandle()
        instance.http_response = response
        header_dic = {"content-type":"text/html"}
        instance.set_header(header_dic)
        instance.update_header({"add":"test","content-type":"test"})
        header_dic = {"add":"test","content-type":"test"}
        TestCase().assertTrue(header_dic== instance.get_header())
        header_dic = {"content-type":"test"}
        instance.delete_header(['add'])
        TestCase().assertTrue(header_dic== instance.get_header())
        Log.log_info("test_update_header is ok")

def test_response_code_status_should_be():
        response = Response()
        instance = httpHandler.HttpHandle()
        setattr(response, 'status_code',  200)
        instance.http_response = response
        instance.response_code_status_should_be(200)
        setattr(response, 'status_code',  404)
        instance.http_response = response
        instance.response_code_status_should_be(404)
        
def test_response_body_should_be_list_struct():
        content = b'[{"content": true, "int":1}]'
        response = Response()
        setattr(response, '_content',  content)
        instance = httpHandler.HttpHandle()
        instance.http_response = response
        instance.response_body_should_be_list_struct()

def test_response_body_should_be_dictionary_struct():
        content = b'{"content": true, "int":1}'
        response = Response()
        setattr(response, '_content',  content)
        instance = httpHandler.HttpHandle()
        instance.http_response = response
        instance.response_body_should_be_dictionary_struct()
        instance. response_dictionary_should_have_key("content")    
        instance. response_dictionary_should_have_key("int")    
        instance.response_dictionary_should_not_have_key("int1")
        instance.response_dictionary_should_have_keys(["content","int"])
        instance.response_dictionary_should_have_not_keys(["content1","int1"])
        instance.response_dictionary_should_have_key_value("content",True)
        instance.response_dictionary_should_have_key_value("int",1)
        instance.response_string_should_include("content")
        
def test_conver_json_str_response_to_struct():
        content = b'{"content": true, "int":1}'
        response = Response()
        setattr(response, '_content',  content)
        instance = httpHandler.HttpHandle()
        instance.http_response = response
        TestCase().assertTrue( {"content": True, "int":1} == instance.conver_json_str_response_to_struct())
               
        

def run_unit_test():
    test_replace_paramter_for_url()
    tes_resonse_deep_key_is_struct()
    test_get_response_body()
    test_print_response_body()
    test_get_header()
    test_update_header()
    test_response_code_status_should_be()
    test_response_body_should_be_list_struct()
    test_response_body_should_be_dictionary_struct()
    test_conver_json_str_response_to_struct()
    response_deep_key_value_is_right()
    
run_unit_test()