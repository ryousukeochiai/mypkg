import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from datetime import datetime, timedelta

rclpy.init()
node = Node("DOW_talker")
pub = node.create_publisher(Int16, "date", 10)

d = 0

def cb():
    global d
    msg = Int16()
    msg.data = d
    pub.publish(msg)
    d += 1

node.create_timer((0.1, cb)
rclpy.spin(node)

