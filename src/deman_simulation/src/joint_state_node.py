#!/usr/bin/env python3

from math import floor
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from stop_and_move import StopAndMove

if __name__ == '__main__':
    rospy.init_node('joint_state')

    pubPosition = rospy.Publisher(
        '/set_joint_trajectory', JointTrajectory, queue_size=10)
    rate = rospy.Rate(1)

    msg = JointTrajectory()
    msg.header.frame_id = 'world'
    msg.joint_names = ['x_joint', 'y_joint', 'z_joint', 'c_joint']
    point = JointTrajectoryPoint()

    pathX, pathY, pathZ, pathC = StopAndMove()
    print(pathX, pathY, pathZ, pathC)
    point.positions = [pathX[0], pathY[0], pathZ[0], pathC[0]]
    msg.points = [point]
    pubPosition.publish(msg)

    i = 0

    while not rospy.is_shutdown() and i < len(pathX):
        point.positions = [pathX[i], pathY[i], pathZ[i], pathC[i]]
        msg.points = [point]
        pubPosition.publish(msg)
        i = i+1
        rate.sleep()

    rospy.spin()
