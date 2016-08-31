from  unittest import TestCase
from dianRongQa.database.mysqlUtil import MysqlUtil
from dianRongQa.database.oracleUtil import OracleUtil
import pdb

def test_query_update_oracle():
    host = "10.18.19.32"
    user = "slprod"
    password =  "slsg20"
    db = "testdb2"
    port =  "1521" 
    oracle_instance  = OracleUtil(host, port,db,user, password)
    oracle_instance .connect()
    sql = 'select * from sl$loan_app where loan_id=14801'
    res = oracle_instance.query(sql)
    TestCase().assertTrue(14801==res[0][0])
    sql = 'update sl$loan_app set status=3 where loan_id=14801'
    res = oracle_instance.do_no_query_action(sql)
    sql = 'select * from sl$loan_app where loan_id=14801'
    res = oracle_instance.query(sql)
    TestCase().assertTrue(3 ==res[0][4])
    print("oracel test finished")
    
    
    
def test_query_update_mysql():
    host = "10.18.19.43"
    user =  "wfcrm"
    password =  "crmdemo_uc"
    db = "wfcrm"
    port =  "3308"
    mysql_instance  = MysqlUtil(host, user, password, db, port)
    sql = 'SELECT * FROM wfcrm.actor where actor_id=11335844'
    res = mysql_instance.query(sql)
    TestCase().assertTrue(24943 == res[0][0])
    
    sql = 'update wfcrm.actor  set recommend_actor_id="1234567" where crm_customer_id=24943'
    res = mysql_instance.do_no_query_action(sql)
    sql = 'SELECT * FROM wfcrm.actor where crm_customer_id=24943'
    res = mysql_instance.query(sql)
    TestCase().assertTrue('1234567' == res[0][8])
    print("mysql test finished")

        
    
    
def run_database_test():
    test_query_update_oracle()
    test_query_update_mysql()
    
    
run_database_test()    
    
    