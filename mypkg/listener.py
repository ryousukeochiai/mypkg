# SPDX-FileCopyrightText: 2023 Ryousuke Ochiai 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener():
    def __init__(self):
        self.node = Node("listener")
        self.pub = self.node.create_publisher(Int16, "countup", 10)
        self.n = 0

    def cb(self, msg):
        self.node.get_logger().info("Listen: %d" % msg.data)

def main():
    rclpy.init()
    listener = Listener()
    sub = listener.node.create_subscription(Int16, "countup", listener.cb, 10)
    rclpy.spin(listener.node)

if __name__ == '__main__':
    main()
