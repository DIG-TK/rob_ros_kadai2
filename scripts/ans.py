#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def cb(message):
    if message.data == 1:
        rospy.loginfo("correct answer")
    elif message.data == 2:
        rospy.loginfo("incorrect answer")

if __name__ == "__main__":
    rospy.init_node('ans')
    sub = rospy.Subscriber('prob', Int32, cb)
    rospy.spin()
