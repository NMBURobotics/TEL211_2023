#include "ros/ros.h"
#include "example_cpp_python/StringStamped.h"


int main(int argc, char** argv)
{
    ros::init(argc, argv, "talker_node");
    ros::NodeHandle nh;
    ros::Publisher string_pub = nh.advertise<example_cpp_python::StringStamped>("chitchat", 1);
    ros::Rate rate(1);

    int counter = 0;
    
    ROS_INFO("Talker started");

    while (ros::ok())
    {
        std::stringstream msg_ss;
        msg_ss << "I want " << counter << " ice cream cones!";
        example_cpp_python::StringStamped msg;
        msg.data = msg_ss.str();
        msg.header.stamp = ros::Time::now();
        string_pub.publish(msg);
        counter++;
        rate.sleep();
    }

    return 0;
}