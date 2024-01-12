# mypkg
[![test](https://github.com/ryousukeochiai/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/ryousukeochiai/mypkg/actions/workflows/test.yml)

### ロボットシステム学2023 課題2 提出用リポジトリ
このリポジトリはtalkerとlistener間、DOW_talkerとDOW_listener間でそれぞれ通信を行うROS 2のパッケージです.
talkerとlistener間ではトピック"countup"，DOW_talkerとDOW_listener間ではトピック"date"を使用しています.

## talker.py
0.5秒ごとに16ビット符号つき整数をカウントしてトピック"countup"を通じてパブリッシュ

## listener.py
トピック"countup"からのデータをサブスクライブしてログを表示

## DOW_talker.py
0.1秒ごとに16ビット符号つき整数をカウントしてトピック"date"を通じてパブリッシュ

## DOW_listener.py
トピック"date"からのデータをサブスクライブしメッセージが含む数値(d)を日数として現在の日時に加算

その後，計算したd日後の日時と曜日をログとして表示

## talk_listen.launch.py
talker.pyとlistener.pyを実行

## DOW_talk_listen.launch.py
DOW_talker.pyとDOW_listener.pyを実行

## トピック
### countup
 "talker.py" ノードが生成した16ビット符号つきの整数情報を "listener.py" ノードが受け取り，それをログに表示するための通信経路

### date
 "DOW_talker.py" ノードが生成した16ビット符号つきの整数情報を "DOW_listener.py" ノードが受け取り，計算結果をログに表示するための通信経路

## 実行例

### 例1 (端末2つ使用 , talker.pyを実行)

### 入力
#### 端末1

```
$ ros2 run mypkg talker
```

#### 端末2

```
$ ros2 topic echo /countup
```

### 出力

```
data: 42
---
data: 43
---
data: 44
---
data: 45
---
data: 46
---
・・・
```

### 例2　(端末2つ使用 , talker.py & listener.pyを実行)

### 入力
#### 端末1

```
$ ros2 run mypkg talker
```

#### 端末2

```
$ ros2 run mypkg listener
```

### 出力

```
[INFO] [1703690386.659035596] [listener]: Listen: 454
[INFO] [1703690387.145821959] [listener]: Listen: 455
[INFO] [1703690387.645278088] [listener]: Listen: 456
[INFO] [1703690388.143128216] [listener]: Listen: 457
[INFO] [1703690388.640975790] [listener]: Listen: 458
・・・
```

### 例3　(端末1つ使用 , talker.py & listener.pyを実行)

### 入力

```
$ ros2 launch mypkg talk_listen.launch.py
```

### 出力

```
[INFO] [launch]: All log files can be found below /home/ryousuke/.ros/log/2023-12-28-00-30-38-081232-dynabook0614-2205
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [2207]
[INFO] [listener-2]: process started with pid [2209]
[listener-2] [INFO] [1703691039.069808334] [listener]: Listen: 0
[listener-2] [INFO] [1703691039.551775082] [listener]: Listen: 1
[listener-2] [INFO] [1703691040.051774291] [listener]: Listen: 2
[listener-2] [INFO] [1703691040.551301372] [listener]: Listen: 3
[listener-2] [INFO] [1703691041.052199121] [listener]: Listen: 4
・・・
```

### 例4 (端末2つ使用 , DOW_talker.pyを実行)

### 入力
#### 端末1

```
$ ros2 run mypkg DOW_talker
```

#### 端末2

```
$ ros2 topic echo /date
```

### 出力

```
data: 73
---
data: 74
---
data: 75
---
data: 76
---
data: 77
---
・・・
```

### 例5　(端末2つ使用 , DOW_talker.py & DOW_listener.pyを実行)

### 入力
#### 端末1

```
$ ros2 run mypkg DOW_talker
```

#### 端末2

```
$ ros2 run mypkg DOW_listener
```

### 出力

```
[INFO] [1705035579.759725618] [DOW_listener]: 2024/02/02 (Fri)
[INFO] [1705035579.854471413] [DOW_listener]: 2024/02/03 (Sat)
[INFO] [1705035579.953579952] [DOW_listener]: 2024/02/04 (Sun)
[INFO] [1705035580.054491518] [DOW_listener]: 2024/02/05 (Mon)
[INFO] [1705035580.153439036] [DOW_listener]: 2024/02/06 (Tue)
・・・
```

### 例6　(端末1つ使用 , DOW_talker.py & DOW_listener.pyを実行)

### 入力

```
$ ros2 launch mypkg DOW_talk_listen.launch.py
```

### 出力

```
[INFO] [launch]: All log files can be found below /home/ryousuke/.ros/log/2024-01-12-14-02-09-481703-dynabook0614-4129
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [DOW_talker-1]: process started with pid [4131]
[INFO] [DOW_listener-2]: process started with pid [4133]
[DOW_listener-2] [INFO] [1705035729.882844148] [DOW_listener]: 2024/01/12 (Fri)
[DOW_listener-2] [INFO] [1705035729.971133169] [DOW_listener]: 2024/01/13 (Sat)
[DOW_listener-2] [INFO] [1705035730.071746834] [DOW_listener]: 2024/01/14 (Sun)
[DOW_listener-2] [INFO] [1705035730.171179560] [DOW_listener]: 2024/01/15 (Mon)
[DOW_listener-2] [INFO] [1705035730.271456473] [DOW_listener]: 2024/01/16 (Tue)
・・・
```


## 動作確認済み環境
* Python 3.8.10
* Ubuntu 20.04.5 LTS
* ROS 2 Foxy


## テスト環境
テストには以下のコンテナを使用しています.
* [ryuichiueda/ubuntu22.04-ros2](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)


## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
   * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

* © 2023 Ryousuke Ochiai
