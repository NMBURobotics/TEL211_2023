cmake_minimum_required(VERSION 3.0.2)

project(demo_packages)

find_package(catkin REQUIRED COMPONENTS 
roscpp
sensor_msgs
tf
gazebo_ros
message_generation 
std_msgs 
geometry_msgs)
find_package(gazebo REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

catkin_package(
    INCLUDE_DIRS velodyne_simulator/include ${GAZEBO_INCLUDE_DIRS}
    LIBRARIES gazebo_ros_velodyne_laser gazebo_ros_velodyne_gpu_laser    
    CATKIN_DEPENDS roscpp sensor_msgs tf gazebo_ros message_generation std_msgs geometry_msgs)

include_directories(
    velodyne_simulator/include
    ${catkin_INCLUDE_DIRS}
    ${GAZEBO_INCLUDE_DIRS}
)

link_directories(
    ${GAZEBO_LIBRARY_DIRS}
)

catkin_install_python(PROGRAMS
                    thorvald_command/command_publisher.py
                    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
                    )

catkin_install_python(PROGRAMS
                    velodyne_simulator/pcl2_subscriber.py
                    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
                    )

add_library(gazebo_ros_velodyne_laser velodyne_simulator/src/GazeboRosVelodyneLaser.cpp)
    target_link_libraries(gazebo_ros_velodyne_laser
    ${catkin_LIBRARIES}
    ${GAZEBO_LIBRARIES}
    RayPlugin
)

add_library(gazebo_ros_velodyne_gpu_laser velodyne_simulator/src/GazeboRosVelodyneLaser.cpp)
    target_link_libraries(gazebo_ros_velodyne_gpu_laser
    ${catkin_LIBRARIES}
    ${GAZEBO_LIBRARIES}
    GpuRayPlugin
)
target_compile_definitions(gazebo_ros_velodyne_gpu_laser PRIVATE GAZEBO_GPU_RAY=1)

install(TARGETS gazebo_ros_velodyne_laser gazebo_ros_velodyne_gpu_laser
    LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
)

install(DIRECTORY velodyne_simulator/include/${PROJECT_NAME}/
    DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)

install(DIRECTORY launch meshes rviz urdf world
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
