#!/usr/bin/env python


import rospy
from service_server_client_pkg.srv import ListFolders, ListFoldersResponse
import os


class ListFoldersServerNode():

    def __init__(self, *args):
        rospy.loginfo("Constructing ListFoldersServerNode")
        rospy.Service("list_folders", ListFolders, self.list_folders_callback)

    def list_folders_callback(self, request):
        path = request.path
        print("Listing folders under: ", path)
        print(os.listdir(path))
        return ListFoldersResponse(os.listdir(path))


if __name__ == '__main__':
    node = ListFoldersServerNode()
    rospy.init_node('ListFoldersServerNode', anonymous=False)
    rospy.spin()
    rospy.loginfo("Shutting down ListFoldersServerNode")
