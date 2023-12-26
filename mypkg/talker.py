import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

class Talker():          #ヘッダの下にTalkerというクラスを作成
    def __init__(self, node):  # オブジェクトを作ると呼ばれる関数
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0 #selfはオブジェクトのこと,オブジェクトにひとつパブリッシャと変数をもたせる。
        node.create_timer(0.5, self.cb)

    def cb(self):              #関数内のnやpubをtalkerのものに変更
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)      #オブジェクトを作成（__init__が実行される。）
    rclpy.spin(node)

if __name__ == '__main__':
    main()
