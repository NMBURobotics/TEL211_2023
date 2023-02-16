cmake_minimum_required(VERSION 3.0.2)

project(service_server_client_pkg)

find_package(catkin REQUIRED COMPONENTS 
rospy
std_msgs 
geometry_msgs
message_generation
message_runtime)

add_service_files(FILES
 ListFolders.srv)

generate_messages(DEPENDENCIES 
  std_msgs)

catkin_package(
    CATKIN_DEPENDS rospy std_msgs geometry_msgs message_runtime)

catkin_install_python(PROGRAMS
                      src/list_folders_server.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
                      )

catkin_install_python(PROGRAMS
                    src/list_folders_client.py
                    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
                    )

install(DIRECTORY launch params
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
