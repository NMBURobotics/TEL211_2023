#!/usr/bin/env python

from genpy.message import strify_message
import rospy
from  geometry_msgs.msg import Twist

class CommandPublisherNode():
    
    def __init__(self, *args):
        print("Constructing CommandPublisherNode")
        
        self.command_pub = rospy.Publisher("/twist_mux/cmd_vel", Twist)
    
    def publish(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = -0.2
        self.command_pub.publish(msg)
        print("I am publishing commands to Thorvald ")
        
if __name__ == '__main__':
    node = CommandPublisherNode()
    rospy.init_node('CommandPublisherNode', anonymous=True)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        node.publish()
        rate.sleep()
    print("Shutting down CommandPublisherNode")
        
        