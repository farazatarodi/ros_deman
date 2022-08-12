#!/usr/bin/env python3

from math import floor
from pymodbus.client.sync import ModbusTcpClient
import rospy
from std_msgs.msg import Int16, String
import json

VELOCITY_CONSTANT = 2.8369
ACCELERATION_CONSTANT = 271

def mode_callback(mode: Int16):
    client.write_registers(4, [mode.data, 0], unit=1)

if __name__ == '__main__':
    rospy.init_node('x_client')

    client = ModbusTcpClient('192.168.11.2', 502)
    connection = client.connect()
    if (connection):
        rospy.loginfo('Connected to X motor on 192.168.11.2:502')

        configFile = open('src/deman_motor_clients/config.json')
        configData = json.load(configFile)

        config = configData['x_client']

        rospy.loginfo('Writing initial registers')

        client.write_registers(10, [floor(config['velocity']*VELOCITY_CONSTANT),0], unit=1)
        result = client.read_holding_registers(10, 2, unit=1)
        rospy.loginfo('Velocity: ' + str(result.registers[0]))

        high, low = divmod(int(hex(config['home_position']), 16), 0x10000)
        client.write_registers(6, [low,high], unit=1)
        result = client.read_holding_registers(6, 2, unit=1)
        rospy.loginfo('Home position: ' + str(result.registers))

        client.write_registers(12, [floor(config['acceleration']/ACCELERATION_CONSTANT),0], unit=1)
        result = client.read_holding_registers(12, 2, unit=1)
        rospy.loginfo('Acceleration: ' + str(result.registers[0]))

        subMode = rospy.Subscriber('/mode', Int16, callback=mode_callback)
        pubStatus = rospy.Publisher('/x_client/status', String, queue_size=10)
        rate = rospy.Rate(1)
        
        while not rospy.is_shutdown():
            response = client.read_holding_registers(4, 2, unit=1)
            currentMode = response.registers
            if (currentMode == [0,0]):
                pubStatus.publish('Idle')
            elif (currentMode == [1,0]):
                pubStatus.publish('Velocity')

            rate.sleep()

        rospy.spin()
    else:
        rospy.loginfo('Failed to connect to X motor')
        rospy.signal_shutdown('Failed to connect to X motor')

