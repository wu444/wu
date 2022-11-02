# coding=utf-8
import datetime
import json
from utils.Mysql_Utils import Mysql_Utils
mysql = Mysql_Utils()
from utils.logger import logger
class Rdtestcase():
    # 加载所有的测试用例
    def loadAllcase(self):
        # sql = "select * from `file` where web = '{0}'".format(web)
        # results = mysql.get_fetchall(sql)
        results = mysql.get_fetchall('select * from file;')
        return results
    # 筛选可执行的用例
    def is_run_data(self):
        run_list = list()
        for case in self.loadAllcase():
            if case['execute'] == "Y":
                run_list.append(case)
        return run_list
    def loadConfkey(self,web,key):
        sql = "select * from `环境配置表` where web='{0}' and `key`='{1}'".format(web,key)
        results = mysql.get_fetchone(sql)
        return results
    def updateResults(self,result,is_pass,case_id):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "insert into `file`(result,time,result,ispass) values ('{0}','{1}','{2}','{3}')".format(result,current_time,json.dumps(result),is_pass)
        rows = mysql.sql_execute(sql)
        print(sql)
        return rows

if __name__ == '__main__':
    test = Rdtestcase()
    res = test.updateResults("{'code': 200, 'body': {'error': 1, 'message': '\u7528\u6237\u540d\u548c\u5bc6\u7801\u90fd\u4e0d\u80fd\u4e3a\u7a7a'}, 'cookies': {}}",'True','45')
    print(res)