import pymysql
from tool.logger_ import logger
from tool.object_path.file_path import config_
from tool.redconfig import IniRead

db_dict = {'host': IniRead(config_).red_get('credit_db', 'host'),
           'port': IniRead(config_).red_int('credit_db', 'port'),
           'user': IniRead(config_).red_get('credit_db', 'user'),
           'password': IniRead(config_).red_get('credit_db', 'password'),
           'database': IniRead(config_).red_get('credit_db', 'database')}
print(db_dict)


class databaseConnection(object):
    def __init__(self, user_mysql=None):
        """
        连接信贷数据库,连接需要的账号信息，
        放到ini文件中,用的时候转成字dian
        :param user_mysql:
        """
        if user_mysql is None:
            user_mysql = db_dict
        if type(user_mysql) is not dict:
            logger.info("传入的类参数类型不对，必须是要dict类型")
        else:
            for key in ['host', 'port', 'user', 'password', 'database']:
                if key not in user_mysql.keys():
                    logger.error(f"数据库连接的信息错误:缺少{key}")

        try:
            self.__conn = pymysql.connect(
                host=user_mysql['host'],
                user=user_mysql['user'],
                password=user_mysql['password'],
                database=user_mysql['database'],
                port=user_mysql['port'],

                cursorclass=pymysql.cursors.DictCursor
            )
            self.connected = True
        except pymysql.err as e:
            logger.error(f"数据库连接的信息错误:缺少{e}", end='')
            raise e

        else:
            pass

    def cnn_fetch_one(self, __sql):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(__sql)
            return cursor.fetchone()
        except pymysql.err as e:
            logger.info(f"查询单条数据错误:{e}", end='')
            raise e

    def cnn_fetch_all(self, __sql):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(__sql)
            return cursor.fetchall()
        except pymysql.err as e:
            logger.info(f"查询多条数据错误:{e}", end='')
            raise e

    def cnn_update_values(self, __sql):
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(__sql)
            self.__conn.commit()
            return cursor.rowcount
        except pymysql.err as e:
            logger.info(f"更新数据错误:{e}", end='')
            raise e

    def cnn_delete_(self, __sql):
        """
        删除数据的法方，尽量少整
        :param __sql:
        :return:
        """
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(__sql)
            self.__conn.commit()
            return cursor.rowcount
        except pymysql.err as e:
            logger.info(f"删除数据错误:{e}", end='')
            raise e

    def cnn_inster_(self, __sql, __insert):
        """
        大规模造测试数据
        :param __sql:
        :param __insert:
        :return:
        """
        try:
            with self.__conn.cursor() as cursor:
                cursor.executemany(__sql, __insert)
            self.__conn.commit()
            return cursor.rowcount
        except pymysql.err as e:
            logger.info(f"插入数据错误:{e}", end='')
            raise e

    def close(self):
        return self.__conn.close()


if __name__ == '__main__':
    """
    一下插入较大数据时注意的点：
        1.原测试环境,数据库表,提前备份号(忘了提前备份,出现bug后，要去写sql删除插入的测试数据,)
        2.插入数据过大,内存是否充足,提前看下,不然内存不够栈会溢出(忘了提前看内存,导致内存溢出报错,还的去把测试数据清除,不然影响其他插入测试.....)
        3.插入数据的准确性,因为数据表中,某些字段的类型/是否为空，唯一性,的提前确认好
    """
    import uuid
    import random

    # 必要字段随机范围
    valid_black_types = [1, 2, 3, 7]
    valid_sources = [1, 2]
    inster_sql = r"INSERT INTO " \
                 r"`hc_loans_nga_mix`.`loans_black` " \
                 r"(black_no, black_type, source)" \
                 r" VALUES (%s, %s, %s)"
    __data = []
    # 为避免误操作,在数据库插入大量无用数据，将range()参数置为0,需要测试大量插入数据是,在更改range参数
    for sql_ in range(0):
        black_no = str(uuid.uuid4()).replace('-', '')
        black_type = random.choice(valid_black_types)
        source = random.choice(valid_sources)
        __data.append((black_no, black_type, source))
    __cnn = databaseConnection().cnn_inster_(inster_sql, __data)
    databaseConnection().close()
    print(f"插入数据情况:{__cnn}")
