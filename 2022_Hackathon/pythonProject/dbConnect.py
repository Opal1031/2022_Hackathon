import logging
import sys
import os
import pymysql
import pandas


def pyQTConnect(bGender, bOct,cate):
    # RDS info
    host = 'database-1.cf7q1akso6qq.ap-northeast-2.rds.amazonaws.com'
    port = 3306
    username = 'hello'
    password = 'abc12345'
    database = 'SongDB'

    try:
        conn = pymysql.connect(host=host, user=username, passwd=password, db=database,
                               port=port, use_unicode=True, charset='utf8')
        cursor = conn.cursor(pymysql.cursors.DictCursor)

    except:
        logging.error("RDS에 연결되지 않았습니다.")
        sys.exit(1)

    gender = bGender
    oct = bOct
    category = cate
    data = (gender, oct, category)
    sql = 'SELECT * FROM SONGDB WHERE (gender = %s AND oct = %s AND category = %s)  ORDER BY likes DESC limit 10';


    cursor.execute(sql, data)
    result = cursor.fetchall()
    df = pandas.DataFrame(result)
    return df.values

#exam
#gend="M"
#oct="2옥시"
#cateName="댄스"
#dif = pyQTConnect(gend, oct, cateName)
#print(dif)

