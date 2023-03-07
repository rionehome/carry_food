cmake_minimum_required(VERSION 3.0.2)
project(carry_food)

find_package(catkin REQUIRED COMPONENTS
	rospy
	std_msgs
	message_generation
)

add_message_files(
	FILES
	PositionValues.msg
)

add_service_files(
  FILES
  isMeaning.srv
  MoveArm.srv
  SpeechToText.srv
)

add_service_files(
  FILES
  Camera_msg.srv
  MoveArm.srv
)

generate_messages(
	DEPENDENCIES
	std_msgs
)

catkin_package(
   CATKIN_DEPENDS rospy std_msgs message_runtime
)

include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)
