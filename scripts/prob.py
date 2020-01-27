#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Int32

if __name__ == "__main__":
    rospy.init_node('prob')
    pub = rospy.Publisher('prob', Int32, queue_size=1)
    while not rospy.is_shutdown():
        a = random.randint(1,100)
        b = random.randint(1,100)
        if a <=b:
            print('%d + %d = ?' %(a, b))
            n = raw_input('ansewr enter:')
            if n.isdigit():
                n = int(n)
                if n == (a + b):
                    pub.publish(1)
                elif n != (a + b):
                    pub.publish(2)
                    break
        elif a >b:
            print('%d - %d = ?' %(a, b))
            n = raw_input('ansewr enter:')
            if n.isdigit():
                n = int(n)
                if n == (a - b):
                    pub.publish(1)
                elif n != (a - b):
                    pub.publish(2)
                    break
