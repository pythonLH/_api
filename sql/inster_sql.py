import uuid
import random
import mysql.connector

# 连接数据库
cnx = mysql.connector.connect(
    host='192.168.122.177',
    user='root',
    password='hc123456',
    database='hc_loans_nga_mix'
)
cursor = cnx.cursor()

# 定义有效范围
valid_black_types = [1, 2, 3, 7]
valid_sources = [1, 2]

# 生成并插入测试数据
try:
    insert_query = "INSERT INTO loans_black (black_no, black_type, source) VALUES (%s, %s, %s)"
    data = []

    for _ in range(10):
        black_no = str(uuid.uuid4()).replace('-', '')
        black_type = random.choice(valid_black_types)
        source = random.choice(valid_sources)
        data.append((black_no, black_type, source))

    cursor.executemany(insert_query, data)
    print("sql语句为：%s" % (data))
    cnx.commit()
    print("数据插入成功")

except mysql.connector.Error as error:
    print("插入数据时出现错误:", error)

finally:
    cursor.close()
    cnx.close()
