#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16

if __name__ == '__main__':
    rospy.init_node('controller_node')

    modePub = rospy.Publisher('/mode', Int16, queue_size=10)
    
    while not rospy.is_shutdown():
        mode = input('Mode [0 for passive, 2 for position]: ')
        if mode == '0':
            modePub.publish(0)
            rospy.loginfo('Mode set to passive')
        elif mode == '1':
            modePub.publish(1)
            rospy.loginfo('Mode set to velocity')
        elif mode == '2':
            modePub.publish(2)
            rospy.loginfo('Mode set to position')
        else:
            rospy.loginfo('Mode not valid')

