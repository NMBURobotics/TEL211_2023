cmake_minimum_required(VERSION 3.0.2)

project(talker_listener_pkg)

find_package(catkin REQUIRED COMPONENTS 
roscpp
rospy
std_msgs 
geometry_msgs)

catkin_package(
    CATKIN_DEPENDS roscpp rospy std_msgs geometry_msgs)

catkin_install_python(PROGRAMS
                      src/talker.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
                      )

catkin_install_python(PROGRAMS
                    src/listener.py
                    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
                    )

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
