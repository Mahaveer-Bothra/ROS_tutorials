#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
def pose_callback(data):
    rospy.loginfo("Turtle Pose - Position: ({}, {}), Orientation: {}".format(data.x, data.y, data.theta))
def turtle_pose_subscriber():
    rospy.init_node('turtle_pose_subscriber', anonymous=True)
    rospy.Subscriber('turtle1/pose', Pose, pose_callback)
    rospy.spin()
if __name__ == '__main__':
    turtle_pose_subscriber()