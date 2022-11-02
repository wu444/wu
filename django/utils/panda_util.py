#coding = utf-8
import pandas as pd
from sqlalchemy import create_engine
import os
import logger
from Read_Mysql import Mysql_Utils
import json
mysql = Mysql_Utils()
#获取文件所在位置
def getpath():
    name = input('请输入需要执行的用例名：')
    filepath = os.path.abspath(
        os.path.abspath(os.path.dirname(os.getcwd()))) + os.path.sep + 'excutefile/' + os.path.sep + name
    return filepath
#写入数据库
def readfile():
    df = pd.read_csv(getpath(), encoding='gbk')
    df.to_sql(name='file', con=create_engine(
        'mysql+pymysql://{}:{}@{}:{}/{}'.format('root', 'Wu971003.', '172.16.1.84', 3306, 'wu')), index=False,
              if_exists='replace')
    # logger.logger.info('已成功将用例写入__{}'.format(mysql.get_fetchall("select * from file;")))
    return df
# res = Mysql_Utils().get_fetchall("select * from file;")
# print(res)
#从数据库读取需要执行的用例
def Allcase():
    res = mysql.get_fetchall("select * from file")
    # print(res)
    dict1 = []
    for i in res:
        dict1.append(i)
        # print(dict1)
    logger.logger.info('所有用例取出{}'.format(dict1))
    # print(type(dict1))
    return dict1
def isruncase():
    runcase = []
    a = Allcase()
    for i in a:
        # print(type(i))
        if i['execute'] == 'Y':
            runcase.append(i)
            logger.logger.info('可执行用例{}'.format(runcase))
    # print(runcase)
    return runcase

if __name__ == '__main__':
    readfile()
    # res = mysql.get_fetchall("select * from file;")
    # print(res)
    # mysql.sql_execute('truncate table file;')
    isruncase()
