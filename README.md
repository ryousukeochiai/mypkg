# mypkg
[![test](https://github.com/ryousukeochiai/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/ryousukeochiai/mypkg/actions/workflows/test.yml)

### ロボットシステム学2023 課題2 提出用リポジトリ
このリポジトリはtalkerとlistener間で通信を行うROS 2のパッケージです.

## talker.py
0.5秒ごとに16ビット符号つき整数をカウントしてトピック"countup"を通じてパブリッシュ

## listener.py
トピック"countup"からのデータをサブスクライブしてログを表示

## talk_listen.launch.py
talker.pyとlistener.pyを実行

## トピック
### countup
 "talker.py" ノードが生成した16ビット符号つきの整数情報を "listener.py" ノードが受け取り、それをログに表示するための通信経路

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


### 例2　(端末2つ使用 , talker.py&listener.pyを実行)

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



### 例3　(端末1つ使用 , talker.py&listener.pyを実行)

### 入力

```
$ ros2 launch mypkg talk_listen.launch.p
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
[listener-2] [INFO] [1703691041.551767608] [listener]: Listen: 5
・・・
```


## 動作確認済み環境
* Python
* Ubuntu 20.04
* ROS 2 Foxy


## テスト環境
テストには以下のコンテナを使用しています.
* [ryuichiueda/ubuntu22.04-ros2](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)


## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
   * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

* © 2023 Ryousuke Ochiai
