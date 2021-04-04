from flask import Flask
import mysql.connector
#import MySQLdb

#DB接続情報
def conn_db():
    conn = mysql.connector.connect(
        #dbコンテナのipアドレス コンテナ内でhostname -i で確認
        #dockerビルドで変わる可能性あるため都度確認
        host = '172.19.0.2',
        port = '3306',     #localhostでもOK
        user = 'test_user',
        passwd = '1q2w3e4r5t',
        database = 'sample_db'
    )
    conn.ping(reconnect=True)
    return conn

def setDB(name, value):

    try:
        conn = conn_db()

        sql = "INSERT INTO exchange(name, value) VALUES (%(name)s, %(value)s)"
        data = {'name': name, 'value': value}
        cur.execute(sql, data)

    except:
        print('エラーだぜ')
