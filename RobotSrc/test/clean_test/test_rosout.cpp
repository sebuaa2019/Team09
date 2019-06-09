#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <tf/tf.h>
#include <tf/transform_listener.h>
#include <std_msgs/String.h>
#include <rosgraph_msgs/Log.h>
#include <ctime>
#include <cstdio>
#include <cstdlib>

void rosoutCB(const rosgraph_msgs::Log::ConstPtr& msg){
	if (msg->level == rosgraph_msgs::Log::ERROR){    
		printf("[test_rosout] FIND LOG ERR\n");
	}
}

int main(int argc, char** argv){
    ros::init(argc, argv, "test_rosout");

    ros::NodeHandle n;
    ros::Subscriber rosout_sb = n.subscribe("/rosout", 0, rosoutCB);


	ROS_INFO("this is a info");
	ros.spinOnce();
	ROS_ERROR("this is a err");
	ros.spinOnce();
	ROS_INFO("this is a info");
	ros.spinOnce();
	ROS_ERROR("this is a err");

	while (ros::ok()){
		ros::spin();
	}

    return 0;
}
