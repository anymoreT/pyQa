# -*- coding:utf-8 -*-

from  unittest import TestCase
from dianRongQa.httpHander import httpHandler
import json
from requests.models import Response
import pdb
from dianRongQa.log.log import Log

def tes_resonse_deep_key_is_struct():
    '''
    #可以验证如下的类型
    #TYPES = {"STRING" : str, "HASH" : dict, "INT" : int, "FLOAT" : float, "LIST" : list, "BOOL" : bool}
    '''
    content = b'{"content": {"list": [{"name": "string", "index":1,"verify":true, "type": { "name": "string","parent": "string","path": "string","description": "string", "title": true,"order": 0,"icon": "string" },"hot": true,"platform": [  "desktop" ], "from": "string", "until": "string", "locale": "string", "staticLink": "string", "thumbnail": "string", "content": "string", "htmlContent": "string", "description": "string" }],"totalRecords": 0},"result": "string","errors": ["string"]}'
    response = Response()
    setattr(response, '_content',  content)
    instance = httpHandler.HttpHandle()
    instance.http_response = response
    instance.response_deep_key_is_struct(target_struct = {"content" : "HASH", "result" :"STRING", "errors" : "LIST"})
    instance.response_deep_key_is_struct("content", "list", 0,  target_struct = {"name" : "STRING", "type" :"HASH", "index" : "INT", "verify" : "BOOL"})

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
        instance.response_dictionary_should_have_keys(["content","int"])
        instance.response_dictionary_should_have_key_value("content",True)
        instance.response_dictionary_should_have_key_value("int",1)
        instance.response_string_should_include("content")

def run_unit_test():
    tes_resonse_deep_key_is_struct()
    test_get_response_body()
    test_print_response_body()
    test_get_header()
    test_update_header()
    test_response_code_status_should_be()
    test_response_body_should_be_list_struct()
    test_response_body_should_be_dictionary_struct()
    
run_unit_test()