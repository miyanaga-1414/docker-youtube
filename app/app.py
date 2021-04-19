from flask import Flask
from flask import jsonify
import mysql.connector
from util import db_util
from util import youtube_util
from util import ssl_util

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/api/get/<key>", methods=["GET"])
def api_get(key):
    return key

@app.route("/api/get_db/<key>", methods=["GET"])
def api_get_db(key):
    data = {key: []}
    sql = 'SELECT * FROM use_money'
    try:
        conn = db_util.conn_db()              #ここでDBに接続
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


#本API実行でレスポンスがtrueならDB接続可能
@app.route("/api/status/<key>", methods=["GET"])
def api_get_db_status(key):

    data = {key: []}

    try:
        conn = db_util.conn_db()
        #cursor = conn.cursor()
        status = conn.is_connected()
        data[key].append(status)
    except(mysql.connector.errors.InterfaceError) as e:
        return format(e)

    return jsonify(data)


@app.route("/api/youtube/<query>", methods=["GET"])
def search_youtube(query):
    return youtube_util.search_video(query)

@app.route("/api/openssl", methods=["GET"])
def getDegitalCertificate():
    data = ssl_util.getPublicKey()

    json = {"key": data}

    return jsonify(json)

@app.route("/api/privatekey", methods=["GET"])
def getPrivateKey():
    key = ssl_util.getPrivateKey()

    return jsonify(
        {
            "key": key
        }
    )

@app.route("/api/signature", methods=["GET"])
def signature():
    result = ssl_util.signature()

    return jsonify({"result":result})


app.run(host='0.0.0.0',port=7010,debug=True)