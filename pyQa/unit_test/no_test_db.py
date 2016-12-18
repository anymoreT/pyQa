'''
from  unittest import TestCase
from pyQa.database.mysqlUtil import MysqlUtil
#from pyQa.database.oracleUtil import OracleUtil
from pyQa.log.log import Log
import pdb


def test_query_update_oracle():
    Log.log_case_desc("TC001:test_query_update_oracle")
    host = ""
    user = ""
    password =  ""
    db = ""
    port =  "" 
    oracle_instance  = OracleUtil(host, port,db,user, password)
    oracle_instance .connect()
    sql = 'select * from app where loan_id=14801'
    res = oracle_instance.query(sql)
    TestCase().assertTrue(14801==res[0][0])
    sql = 'update app set status=3 where loan_id=14801'
    res = oracle_instance.do_no_query_action(sql)
    sql = 'select * from app where loan_id=14801'
    res = oracle_instance.query(sql)
    TestCase().assertTrue(3 ==res[0][4])
    print("oracel test finished")
    
    
    
def test_query_update_mysql():
    Log.log_case_desc("TC001:test_query_update_mysql")
    host = ""
    user =  ""
    password =  ""
    db = ""
    port =  ""
    mysql_instance  = MysqlUtil(host, user, password, db, port)
    sql = 'SELECT * FROM actor where actor_id=112233'
    res = mysql_instance.query(sql)
    TestCase().assertTrue(24943 == res[0][0])
    
    sql = 'update wfcrm.actor  set recommend_actor_id="112233" where id=34578'
    res = mysql_instance.do_no_query_action(sql)
    sql = 'SELECT * FROM actor where id=34578'
    res = mysql_instance.query(sql)
    TestCase().assertTrue('112233' == res[0][8])
    print("mysql test finished")

        
    
    
def run_database_test():
    test_query_update_oracle()
    test_query_update_mysql()
    
    
run_database_test()    
    
'''