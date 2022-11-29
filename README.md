# AWS Lightsail コンテナ

## 目的

- Lightsailでコンテナを立てられるか実験
- 簡単にできるか検証

## 手順

[このファイル](https://github.com/hagerondev/flask-container)を使用する

1. イメージを作成

```bash
$ docker build -t test-flask .
```

2. コンテナを作成

```bash
$ docker run -p 8080:80 --name flask1 -d test-flask
```

3. 確認

```bash
$ curl localhost:8080
Hello UEC!
```

**準備完了**

4. Docker Hubにログイン

```bash
$ docker login
Login Succeeded
```

5. タグをつける

```bash
$ docker tag test-flask hageron/test-flask:latest
```

6. push

```bash
$ docker push hageron/test-flask:latest
```

[できた](https://hub.docker.com/r/hageron/test-flask)

7. コンテナサービスの作成

![コンテナサービスの作成](https://i.imgur.com/2UKQBkq.png)

8. デプロイ

![デプロイ](https://i.imgur.com/ec6hw1d.png)

※デプロイには少し時間がかかる

9. 確認

(https://websys-test.a522q8v01m9vu.ap-northeast-1.cs.amazonlightsail.com/)[https://websys-test.a522q8v01m9vu.ap-northeast-1.cs.amazonlightsail.com/]
