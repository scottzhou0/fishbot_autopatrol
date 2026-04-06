from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy

def main():
    # 初始化ROS2通信系统
    rclpy.init()
    nav= BasicNavigator() 
    nav.waitUntilNav2Active()
    goal_poses = []    

    goal_pose =PoseStamped()
    goal_pose.header.frame_id = "map"
    goal_pose.header.stamp = nav.get_clock().now().to_msg()
    goal_pose.pose.position.x = 1.1
    goal_pose.pose.position.y = 0.7
    goal_pose.pose.orientation.w = 1.0
    goal_poses.append(goal_pose)

    goal_pose1=PoseStamped()
    goal_pose1.header.frame_id = "map"
    goal_pose1.header.stamp = nav.get_clock().now().to_msg()
    goal_pose1.pose.position.x = 0.5
    goal_pose1.pose.position.y = 1.2
    goal_pose1.pose.orientation.w = 1.0
    goal_poses.append(goal_pose1)

    goal_pose2=PoseStamped()
    goal_pose2.header.frame_id = "map"
    goal_pose2.header.stamp = nav.get_clock().now().to_msg()
    goal_pose2.pose.position.x = -2.0
    goal_pose2.pose.position.y = -2.0
    goal_pose2.pose.orientation.w = 1.0
    goal_poses.append(goal_pose2)


    nav.followWaypoints(goal_poses)
    while nav.isTaskComplete():
            feedback = nav.getFeedback()
            nav.get_logger().info(f'路店编号: {feedback}.current_waypoint')
            # nav.cancelTask()
    result = nav.getResult()
    nav.get_logger().info(f'导航结果: {result}') 
       
    


    rclpy.spin(nav)
    nav.shutdown()

    


