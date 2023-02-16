#!/usr/bin/env python

from genpy.message import strify_message
from std_msgs.msg._String import String
import rospy

class TalkerNode():
    
    def __init__(self, *args):
        print("Constructing TalkerNode")
        self.counter = 0
        
        """
        Parameters for Publisher Function:
            name (str) - resource name of topic, e.g. 'laser'.
            data_class (Message class) - message class for serialization
            subscriber_listener (SubscribeListener) - listener for subscription events. May be None.
            tcp_nodelay (bool) - If True, sets TCP_NODELAY on publisher's socket (disables Nagle algorithm). This results in lower latency publishing at the cost of efficiency.
            latch (bool) - If True, the last message published is 'latched', meaning that any future subscribers will be sent that message immediately upon connection.

        """
        self.string_pub = rospy.Publisher("chat", String)
    
    def publish(self):
        msg = String()
        msg.data = str(self.counter)
        self.string_pub.publish(msg)
        print("I am publishing ", self.counter)
        self.counter += 1
        
if __name__ == '__main__':
    node = TalkerNode()
    rospy.init_node('TalkerNode', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        node.publish()
        rate.sleep()
    print("Shutting down TalkerNode")
        
        