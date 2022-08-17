#!/usr/bin/env python3

from os import stat
from socketserver import StreamRequestHandler
import rospy
from std_msgs.msg import Int32, String
from stop_and_move import StopAndMove

positionCounter = 0
positionBits = [False, False, False, False]

def next_point():
    global pathX
    global pathY
    global pathZ
    global positionCounter
    global positionBits

    if positionBits == [True, True, True, True]:
        if positionCounter < len(pathX)-1:
            positionCounter+=1
            rospy.loginfo(positionCounter)
            rospy.loginfo(positionBits)
            positionBits=[False, False, False, False]
            
    pubXPosition.publish(pathX[positionCounter])
    pubYPosition.publish(pathY[positionCounter])
    pubZPosition.publish(pathZ[positionCounter])
    pubCPosition.publish(pathC[positionCounter])

def next_point_x(msg: Int32):
    actualPosition = msg.data
    global positionBits
    global pathX
    global positionCounter
    
    if actualPosition >= pathX[positionCounter] - 150 and actualPosition <= pathX[positionCounter] + 150:
        positionBits[0] = True
        next_point()


def next_point_y(msg: Int32):
    actualPosition = msg.data
    global positionBits
    global pathY
    global positionCounter

    if actualPosition >= pathY[positionCounter] - 200 and actualPosition <= pathY[positionCounter] + 200:
        positionBits[1] = True
        next_point()


def next_point_z(msg: Int32):
    actualPosition = msg.data
    global positionBits
    global pathZ
    global positionCounter

    if actualPosition >= pathZ[positionCounter] - 200 and actualPosition <= pathZ[positionCounter] + 200:
        positionBits[2] = True
        next_point()


def next_point_c(msg: Int32):
    actualPosition = msg.data
    global positionBits
    global pathC
    global positionCounter

    if actualPosition >= pathC[positionCounter] - 200 and actualPosition <= pathC[positionCounter] + 200:
        positionBits[3] = True
        next_point()


if __name__ == '__main__':
    rospy.init_node('tsp_node')

    pathX, pathY, pathZ, pathC = StopAndMove()
    
    pubXPosition = rospy.Publisher('/x_client/position', Int32, queue_size=10)
    pubYPosition = rospy.Publisher('/y_client/position', Int32, queue_size=10)
    pubZPosition = rospy.Publisher('/z_client/position', Int32, queue_size=10)
    pubCPosition = rospy.Publisher('/c_client/position', Int32, queue_size=10)
    
    subXActualPosition = rospy.Subscriber('/x_client/actual_position', Int32, callback=next_point_x)
    subYActualPosition = rospy.Subscriber('/y_client/actual_position', Int32, callback=next_point_y)
    subZActualPosition = rospy.Subscriber('/z_client/actual_position', Int32, callback=next_point_z)
    subCActualPosition = rospy.Subscriber('/c_client/actual_position', Int32, callback=next_point_c)

    rospy.spin()
