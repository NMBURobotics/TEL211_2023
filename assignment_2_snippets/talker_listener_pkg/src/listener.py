#!/usr/bin/env python

from std_msgs.msg._String import String
import rospy

class ListenerNode():
    
    def __init__(self, *args):
        print("Constructing ListenerNode")
        
        '''
        Parameters For a Subscriber Function:

            name (str) - graph resource name of topic, e.g. 'laser'.
            data_class (Message class) - data type class to use for messages, e.g. std_msgs.msg.String
            callback (str) - function to call ( fn(data)) when data is received. If callback_args is set, the function must accept the callback_args as a second argument, i.e. fn(data, callback_args). NOTE: Additional callbacks can be added using add_callback().
            callback_args (any) - additional arguments to pass to the callback. This is useful when you wish to reuse the same callback for multiple subscriptions.
            queue_size (int) - maximum number of messages to receive at a time. This will generally be 1 or None (infinite, default). buff_size should be increased if this parameter is set as incoming data still needs to sit in the incoming buffer before being discarded. Setting queue_size buff_size to a non-default value affects all subscribers to this topic in this process.
            buff_size (int) - incoming message buffer size in bytes. If queue_size is set, this should be set to a number greater than the queue_size times the average message size. Setting buff_size to a non-default value affects all subscribers to this topic in this process.
            tcp_nodelay (bool) - if True, request TCP_NODELAY from publisher. Use of this option is not generally recommended in most cases as it is better to rely on timestamps in message data. Setting tcp_nodelay to True enables TCP_NODELAY for all subscribers in the same python process.

        '''
        self.chat_subscriber = rospy.Subscriber("chat", String, self.callback,queue_size=1,buff_size=2002428800)
    
    def callback(self, msg):
        print("I have recieved a message: ", msg.data)
        
if __name__ == '__main__':
    node = ListenerNode()
    rospy.init_node('ListenerNode', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rate.sleep()
    print("Shutting down ListenerNode")
        
        