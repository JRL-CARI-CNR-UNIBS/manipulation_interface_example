cmake_minimum_required(VERSION 3.0.2)
project(manipulation_interface_example)

find_package(catkin REQUIRED COMPONENTS
	rospy
	std_msgs
	message_generation
)

## Generate services in the 'srv' folder
add_service_files(
	FILES
	SaveParam_.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
	DEPENDENCIES
	std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES manipulation_interface_example
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

include_directories(
# include
 ${catkin_INCLUDE_DIRS}
)
