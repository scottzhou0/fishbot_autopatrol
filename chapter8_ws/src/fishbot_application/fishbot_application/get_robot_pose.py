import rclpy
from rclpy.node import Node
from rclpy.time import Time
from rclpy.duration import Duration
from tf2_ros import TransformListener,Buffer
from tf_transformations import euler_from_quaternion
import math #           math.pi

class TFBroadcaster(Node):
    def __init__(self):
            # 初始化节点，继承自Node类
            super().__init__('tf_broadcaster')
            # 创建TF缓冲区
            self.buffer_=Buffer()
            self.listener_=TransformListener(self.buffer_,self)

            self.timer_=self.create_timer(1,self.get_transform)
         

    def get_transform(self):
        """获取TF 从camera_link 到bottle_link之间的关系"""
        try:
             result= self.buffer_.lookup_transform('map',
                                                   'base_footprint', #  尝试从buffer中获取从'map'坐标系到'base_footprint'坐标系的变换    使用时间为0（最新可用数据），最长等待1秒
                                                   Time(),
                                                   Duration(seconds=2))
             transform=result.transform #  获取变换结果中的变换信息
             self.get_logger().info(f'平移:{transform.translation}') #  记录平移信息到日志
             self.get_logger().info(f'旋转：{transform.rotation}') #  记录旋转信息到日志
             rotation_euler =euler_from_quaternion([ #  将四元数格式的旋转转换为欧拉角(RPY)格式
                transform.rotation.x,
                transform.rotation.y,
                transform.rotation.z,
                transform.rotation.w])
             self.get_logger().info(f'旋转RPY:{transform.rotation}')

        except Exception as e:
            self.get_logger().warn(f'获取坐标失败：原因{str(e)}')              #  如果获取变换失败，记录警告信息到日志
            


def main():
    # 初始化ROS2客户端库
     rclpy.init()
    # 创建TF广播器节点实例
     node= TFBroadcaster()
     rclpy.spin(node)
     rclpy.shutdown()
