#!/usr/bin/env python3

from pymodbus.client.sync import ModbusTcpClient
import rospy
from std_msgs.msg import Int16, String

def mode_callback(mode: Int16):
    client.write_registers(4, [mode.data, 0], unit=1)

if __name__ == '__main__':
    rospy.init_node('x_client')

    client = ModbusTcpClient('192.168.11.2', 502)
    connection = client.connect()
    if (connection):
        rospy.loginfo('Connected to X motor on 192.168.11.2:502')

        sub = rospy.Subscriber('/mode', Int16, callback=mode_callback)
        pub = rospy.Publisher('/x_client/status', String, queue_size=10)
        rate = rospy.Rate(1)
        
        while not rospy.is_shutdown():
            response = client.read_holding_registers(4, 2, unit=1)
            currentMode = response.registers
            if (currentMode == [0,0]):
                pub.publish('Idle')
            elif (currentMode == [1,0]):
                pub.publish('Velocity')

            rate.sleep()

        rospy.spin()
    else:
        rospy.loginfo('Failed to connect to X motor')
        rospy.signal_shutdown('Failed to connect to X motor')

