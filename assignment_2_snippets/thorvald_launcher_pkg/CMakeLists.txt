cmake_minimum_required(VERSION 3.0.2)

project(thorvald_launcher_pkg)

find_package(catkin REQUIRED COMPONENTS 
roscpp
rospy
std_msgs 
geometry_msgs
)

catkin_package(
    CATKIN_DEPENDS roscpp rospy std_msgs geometry_msgs)

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
