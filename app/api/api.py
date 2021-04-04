from flask import Flask
import mysql.connector
from .db import db_util

@app.route("/api/get_db/<key>", methods=["GET"])
def api_get(key):
    data = {key: []}
    sql = 'SELECT * FROM sample'
    try:
        conn = conn_db()              #ここでDBに接続
        cursor = conn.cursor()       #カーソルを取得
        cursor.execute(sql)             #selectを投げる
        rows = cursor.fetchall()      #selectの結果を全件タプルに格納
    except(mysql.connector.errors.ProgrammingError) as e:
        print('エラーだぜ')
        print(e)

    for t_row in rows:
        res = {"id": t_row.id, "money": t_row.money}
        data[key].append(res)

    return jsonify(data)