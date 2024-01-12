# SPDX-FileCopyrightText: 2023 Ryousuke Ochiai 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from datetime import datetime, timedelta

DOW = 0

def cb(msg):
    global node, DOW

    t = datetime.today() + timedelta(days=msg.data)
    date_str = t.strftime("%Y/%m/%d")

    DOW = t.isoweekday()

    dow_str = ""
    if DOW == 1:
        dow_str = "(Mon)"
    elif DOW == 2:
        dow_str = "(Tue)"
    elif DOW == 3:
        dow_str = "(Wed)"
    elif DOW == 4:
        dow_str = "(Thu)"
    elif DOW == 5:
        dow_str = "(Fri)"
    elif DOW == 6:
        dow_str = "(Sat)"
    elif DOW == 7:
        dow_str = "(Sun)"

    time_str = f"{date_str} {dow_str}"
    node.get_logger().info(time_str)

rclpy.init()
node = Node("DOW_listener")
pub = node.create_subscription(Int16, "date", cb, 10)
rclpy.spin(node)
