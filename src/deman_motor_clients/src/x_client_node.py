#!/usr/bin/env python3

from pymodbus.client.sync import ModbusTcpClient
import rospy
from std_msgs.msg import Int16

def mode_callback(mode: Int16):
    client.write_registers(4, [mode.data, 0], unit=1)

if __name__ == '__main__':
    rospy.init_node('x_client')

    client = ModbusTcpClient('192.168.11.2', 502)
    connection = client.connect()
    if (connection):
        rospy.loginfo('Connected to X motor on 192.168.11.2:502')

        sub = rospy.Subscriber('/mode', Int16, callback=mode_callback)
    else:
        rospy.loginfo('Failed to connect to X motor')
        rospy.signal_shutdown('Failed to connect to X motor')

    rospy.spin()
