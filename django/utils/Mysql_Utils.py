# coding=utf-8
import pymysql
from utils.logger import logger
class Mysql_Utils():
    def __init__(self):
        self.db = pymysql.connect(host="localhost",user="root",password="Wu971003.",database="wu",port=3306,charset="utf8")
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
    # 获取单条数据
    def get_fetchone(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    # 获取多条数据
    def get_fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def sql_execute(self,sql):
        try:
            if self.db and self.cursor:
                self.cursor.execute(sql)
                self.db.commit()
        except Exception as e:
            self.db.rollback()
            logger.error("sql语句执行错错，已执行回滚操作")
            return False

    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.db is not None:
            self.db.close()
if __name__ == '__main__':
    mysql = Mysql_Utils()
    res = mysql.get_fetchall("select * from daka")
    print(type(res))