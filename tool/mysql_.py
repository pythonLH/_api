import pymysql
import configparser

from tool.object_path.file_path import config_
from tool.redconfig import IniRead

config_


# 用来查询sql的
class MysqlUtil:

    def __init__(self):

        host = IniRead(config_).red_get('credit_db', 'host')
        port = IniRead(config_).red_int('credit_db', 'port')
        user = IniRead(config_).red_get('credit_db', 'user')
        password = IniRead(config_).red_get('credit_db', 'password')
        database = IniRead(config_).red_get('credit_db', 'database')
        try:
            self.mysql = pymysql.connect(host=host,
                                         user=user,
                                         password=password,
                                         database=database,
                                         port=port,
                                         cursorclass=pymysql.cursors.DictCursor)

        except Exception as e:
            print("数据库连接错误:{}".format(e))
            raise e

    def fetch_one(self, sql_):
        cursor = self.mysql.cursor()
        cursor.execute(sql_)
        return cursor.fetchone()

    def fetch_all(self, sql_):
        cursor = self.mysql.cursor()
        cursor.execute(sql_)
        return cursor.fetchall()

    def commit(self):
        self.mysql.commit()

    def close(self):
        self.mysql.close()


if __name__ == '__main__':
    sql = "select * from `mp-asset`.`t_asset`  order by  id desc limit 2;"
    code = []
    mysql_util = MysqlUtil()
    results = mysql_util.fetch_all(sql)
    print(results)
