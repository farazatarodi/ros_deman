#!/usr/bin/env python3

from math import floor
from pymodbus.client.sync import ModbusTcpClient
import rospy
from std_msgs.msg import Int16, String, Int32
import json

VELOCITY_CONSTANT = 100
ACCELERATION_CONSTANT = 271


def mode_callback(mode: Int16):
    client.write_registers(4, [mode.data, 0], unit=1)


def position_callback(msg: Int32):
    position = msg.data
    if position < 0:
        position = 2**32 + position
    highPose, lowPose = divmod(int(hex(position), 16), 0x10000)
    client.write_registers(6, [lowPose, highPose], unit=1)


if __name__ == '__main__':
    rospy.init_node('c_client')

    client = ModbusTcpClient('192.168.11.5', 502)
    connection = client.connect()
    if (connection):
        rospy.loginfo('Connected to C motor on 192.168.11.5:502')

        configFile = open('src/deman_motor_clients/config.json')
        configData = json.load(configFile)

        config = configData['c_client']

        rospy.loginfo('Writing initial registers')

        client.write_registers(
            10, [floor(config['velocity']*VELOCITY_CONSTANT), 0], unit=1)
        result = client.read_holding_registers(10, 2, unit=1)
        rospy.loginfo('Velocity: ' + str(result.registers[0]))

        result = client.read_holding_registers(6, 2, unit=1)
        rospy.loginfo('Encoder value: ' + str(result.registers))

        client.write_registers(
            12, [floor(config['acceleration']/ACCELERATION_CONSTANT), 0], unit=1)
        result = client.read_holding_registers(12, 2, unit=1)
        rospy.loginfo('Acceleration: ' + str(result.registers[0]))

        subMode = rospy.Subscriber('/mode', Int16, callback=mode_callback)
        subPosition = rospy.Subscriber(
            '/c_client/position', Int32, callback=position_callback)
        pubStatus = rospy.Publisher('/c_client/status', String, queue_size=10)
        pubActualPosition = rospy.Publisher(
            '/c_client/actual_position', Int32, queue_size=10)
        rate = rospy.Rate(2)

        while not rospy.is_shutdown():
            response = client.read_holding_registers(70, 2, unit=1)
            status = response.registers[0]
            binaryStatus = bin(status)
            pubStatus.publish(binaryStatus)
            response = client.read_holding_registers(20, 2, unit=1)
            actualPosition = response.registers[1] * \
                0x10000+response.registers[0]
            actualPosition = actualPosition - \
                0x100000000 if actualPosition & 0x80000000 else actualPosition
            pubActualPosition.publish(actualPosition)
            rate.sleep()

        rospy.spin()
    else:
        rospy.loginfo('Failed to connect to C motor')
        rospy.signal_shutdown('Failed to connect to C motor')
