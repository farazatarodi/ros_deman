#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32, String
from stop_and_move import StopAndMove

positionCounter = 0

def next_point(msg: String):
    status = msg.data
    global pathX
    global positionCounter
    if len(status) > 6:
        if status[-5] == '1':
            if positionCounter < len(pathX)-1:
                positionCounter+=1

    rospy.loginfo(positionCounter)
    pubXPosition.publish(pathX[positionCounter])

if __name__ == '__main__':
    rospy.init_node('tsp_node')

    pathX = StopAndMove()
    print(pathX)
    
    pubXPosition = rospy.Publisher('/x_client/position', Int32, queue_size=10)
    subXStatus = rospy.Subscriber('/x_client/status', String, callback=next_point)

    pubXPosition.publish(pathX[0])

    rospy.spin()
