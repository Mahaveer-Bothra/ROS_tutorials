#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def turtle_twist_publisher():
    rospy.init_node('turtle_twist_publisher', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        twist_msg = Twist()
        twist_msg.linear.x = 1.0
        twist_msg.angular.z = 1.0
        rospy.loginfo("Publishing Twist: Linear={}, Angular={}".format(twist_msg.linear.x, twist_msg.angular.z))
        pub.publish(twist_msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        turtle_twist_publisher()
    except rospy.ROSInterruptException:
        pass