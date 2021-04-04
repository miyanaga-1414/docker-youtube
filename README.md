# docker-youtube

Docker、YoutubeAPIを使用した自己学習用
 
# 本リポジトリの目的
 
dockerを用いたクライアント、アプリケーションサーバ、DBサーバの疎通設定の学習
YoutubeAPIを用いてPython言語の学習
 
# 各種使用バージョン一覧
 
* Python 3.6
* Flask 1.1.0
* requests 2.22.0
* mysql-connector-python-rf
 
# 各種インストール
 
「docker-compose up -d --build」

コマンドにて上記記載のライブラリがappコンテナにインストールされる。

# 準備

動作を行うにあたり以下準備が必要

1.DBコンテナのIPを取得し、実装へ記載する。（DBの疎通を行う場合）

1-1. 「docker-compose exec db bash」　を実行し、DBコンテナへアクセスする。

1-2. DBコンテナ内で　「hostname -i」　を実行しIPを取得する。

1-3. 「app/util/db_util.py」内の変数「host」へ記載する。



2.APIKeyの取得、記載

2-1. 以下サイトを参考にYoutubeDataAPIの登録及びAPIKeyの取得をする。

https://qiita.com/iroiro_bot/items/1016a6a439dfb8d21eca

2-2. 取得したAPIKeyを「app/util/youtube_util.py」内の変数「DEVELOPER_KEY」へ記載する。

# 使い方
 
①「docker-compose up -d --build」 コマンドにてdockerを起動する。

②cURLを使用し以下リクエストでDBとの疎通が行えているか確認する。

「curl http://localhost:7010/api/status/任意の文字列」

```
{
  "任意の文字列": [
    true
  ]
}
```

上記レスポンスがReturnされればOK

③YoutubeAPI、動画の検索にて任意の文字列で検索を実施する。

「curl http://localhost:7010/api/youtube/任意の文字列」

以下レスポンスの例

```
{
  "body": {
    "etag": "JqVdIE5qUjDUOs8ZfV55t1Rb5WQ", 
    "items": [
      {
        "etag": "E96NbZEdrNl8Jnjpr1l4B8_XvKw", 
        "id": {
          "channelId": "UCZf__ehlCEBPop-_sldpBUQ", 
          "kind": "youtube#channel"
        }, 
        "kind": "youtube#searchResult"
      }, 
      {
        "etag": "MuhRSv8ZZq2GEcjdBA8cJGUMEQU", 
        "id": {
          "kind": "youtube#video", 
          "videoId": "3qCcZ_WrHPs"
        }, 
        "kind": "youtube#searchResult"
      }, 
    ], 
    "kind": "youtube#searchListResponse", 
    "nextPageToken": "CAUQAA", 
    "pageInfo": {
      "resultsPerPage": 5, 
      "totalResults": 629939
    }, 
    "regionCode": "JP"
  }, 
  "status": 200
}

```
 
上記レスポンス内の「channelId」、「videoId」で動画、チャンネルを参照可能

例）

チャンネルの場合、「https://www.youtube.com/channel/"上記channelId"」で該当チャンネルを表示

動画の場合、「https://www.youtube.com/watch?v="上記のvideoId"」で該当動画を表示
