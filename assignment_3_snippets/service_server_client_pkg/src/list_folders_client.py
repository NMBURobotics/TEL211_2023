#!/usr/bin/env python

import rospy
from service_server_client_pkg.srv import ListFolders, ListFoldersResponse, ListFoldersRequest


class ListFoldersClientNode():

    def __init__(self, *args):
        print("Constructing ListFoldersClientNode")
        rospy.init_node('ListFoldersClientNode', anonymous=True)

        # ATTENTION TO HERE ON HOW TO READ PARAMS FROM YAML FILE
        rospy.loginfo(
            "Listing an array of strings that I read from rosparam Server!")
        # if example_param_array cannot be found, we return an empty array as efault value
        strings_parameters = rospy.get_param("example_param_array", [])
        rospy.loginfo(strings_parameters)

        rospy.loginfo(
            "I can also read an int parameter from yaml!")

        # if yet_another_param cannot be found, we return zero as efault value
        int_param = rospy.get_param("yet_another_param", 0)
        rospy.loginfo("I read yet_another_param %d with value of " % int_param)

    def list_folders_client(self, path):
        rospy.wait_for_service('list_folders')

        try:
            service = rospy.ServiceProxy('list_folders', ListFolders)
            response = service(path)
            return response
        except rospy.ServiceException as e:
            rospy.loginfo('Failed to call list_folders', 'service')
            rospy.loginfo('Exection is %s' % e)


if __name__ == '__main__':
    node = ListFoldersClientNode()
    print(node.list_folders_client('/home/tel211/'))
