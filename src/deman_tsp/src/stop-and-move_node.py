#!/usr/bin/env python3

from os import stat
from socketserver import StreamRequestHandler
import rospy
from std_msgs.msg import Int32, String
from stop_and_move import StopAndMove

positionCounter = 0
positionBits = [False, False, False]
start = False

def next_point():
    global pathX
    global pathY
    global pathZ
    global positionCounter
    global positionBits
    global start

    if positionBits == [True, True, True]:
        if positionCounter < len(pathX)-1:
            positionCounter+=1
            rospy.loginfo(positionCounter)
            rospy.loginfo(positionBits)
            positionBits=[False, False, False]
            
    if not start:
        pubXPosition.publish(pathX[positionCounter])
        pubYPosition.publish(pathY[positionCounter])
        pubZPosition.publish(pathZ[positionCounter])

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


def c_move(msg: Int32):
    actualPosition = msg.data
    global positionBits
    global pathX
    global pathY
    global pathZ
    global positionCounter
    global start

    if actualPosition == -11000000 and not start:
        pubXPosition.publish(pathX[0])
        pubYPosition.publish(pathY[0])
        pubZPosition.publish(pathZ[0])
        start = True


if __name__ == '__main__':
    rospy.init_node('tsp_node')

    pathX, pathY, pathZ = StopAndMove()
    pathX.insert(0,0)
    pathY.insert(0,0)
    pathZ.insert(0,0)
    print(pathX)
    print(pathY)
    print(pathZ)
    
    pubXPosition = rospy.Publisher('/x_client/position', Int32, queue_size=10)
    pubYPosition = rospy.Publisher('/y_client/position', Int32, queue_size=10)
    pubZPosition = rospy.Publisher('/z_client/position', Int32, queue_size=10)
    pubCPosition = rospy.Publisher('/c_client/position', Int32, queue_size=10)
    
    subXActualPosition = rospy.Subscriber('/x_client/actual_position', Int32, callback=next_point_x)
    subYActualPosition = rospy.Subscriber('/y_client/actual_position', Int32, callback=next_point_y)
    subZActualPosition = rospy.Subscriber('/z_client/actual_position', Int32, callback=next_point_z)
    subCActualPosition = rospy.Subscriber('/c_client/actual_position', Int32, callback=c_move)

    rospy.spin()
