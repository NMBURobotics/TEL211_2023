cmake_minimum_required(VERSION 3.0.2)
project(example_cpp_python)

# FIND CATKIN MACROS, LIBRARIES AND PACKAGES
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_message_files(
 FILES
 StringStamped.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

# THINGS TO BE PASSED TO DEPENDENT PROJECTS
catkin_package(
  CATKIN_DEPENDS message_runtime
)

# BUILD C++ EXECUTABLE
include_directories(
  ${catkin_INCLUDE_DIRS}
)
add_executable(cpp_talker src/cpp_talker.cpp)
add_dependencies(cpp_talker ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(cpp_talker ${catkin_LIBRARIES})

# INSTALL PYTHON FILES
catkin_install_python(PROGRAMS
  nodes/listener
  nodes/talker
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# INSTALL C++ EXECUTABLE
install(TARGETS cpp_talker
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
