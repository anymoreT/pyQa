# -*- coding:utf-8 -*-
import pymysql
from frameWork.log.log import Log
import pdb

class MysqlUtil(object):
    def __init__(self, host, user, passwd, db, port= 3306):
        self.conn  = None
        try: 
            self.conn = pymysql.connect(host = host, user = user, passwd = passwd, db = db, port = int(port), charset='utf8')
        except:
            Log.log_error_info("fail to connect db %s %s %s %s %s \n" % (host, user, passwd, db, port))
    
    def query(self, sql_str): 
        result = []  
        cur = self.conn.cursor()
        cur.execute(sql_str)
        result = cur.fetchall()
        return result 
    
    def  execute_sql(self, sql_str):
        result = []  
        cur = self.conn.cursor()
        result = cur.execute(sql_str)
        return result 