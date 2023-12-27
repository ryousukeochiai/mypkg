# mypkg
[![test](https://github.com/ryousukeochiai/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/ryousukeochiai/mypkg/actions/workflows/test.yml)

### ロボットシステム学2023 課題2 提出用リポジトリ

## talker.py
0.5秒ごとに16ビット符号つき整数をカウントしてトピック"countup"を通じてパブリッシュ

## listener.py
トピック"countup"からの表示をサブスクライブして表示

## トピック
### countup
 "talker.py" ノードが生成した整数情報を "listener.py" ノードが受け取り、それをログに表示するための通信経路

## 実行例

## 必要なソフトウェア
* Python
* Ubuntu 20.04

## テスト環境
テストには以下のコンテナを使用しています
* [ryuichiueda/ubuntu22.04-ros2](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)

## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
   * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

* © 2023 Ryousuke Ochiai
