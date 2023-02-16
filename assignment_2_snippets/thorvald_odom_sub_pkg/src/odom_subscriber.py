#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


class OdomSubscriber():

    def __init__(self, *args):

        topic_name = rospy.get_param(
            "~topic_name", "odom")  # private to this node

        self.subscriber = rospy.Subscriber(
            topic_name, Odometry, self.odom_callback, queue_size=1)

    def odom_callback(self, msg):

        print(msg.pose)


if __name__ == '__main__':
    rospy.init_node("OdomSubscriber", anonymous=False)

    node = OdomSubscriber()
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rate.sleep()
    print("Shutting down OdomSubscriber")
