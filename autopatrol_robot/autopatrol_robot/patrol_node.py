import os
import rclpy
from geometry_msgs.msg import PoseStamped,Pose
from nav2_simple_commander.robot_navigator import BasicNavigator,TaskResult
from rclpy.node import Node
from rclpy.time import Time
from rclpy.duration import Duration
from tf2_ros import TransformListener,Buffer
from tf_transformations import euler_from_quaternion, quaternion_from_euler
import math #           math.pi
from autopatrol_interfaces.srv import SpeechText
from sensor_msgs.msg import Image #消息接口
from cv_bridge import CvBridge # ROS和OpenCV之间的桥梁库
import cv2

class PatrolNode(BasicNavigator):
    def __init__(self,node_name='patrol_node'):

        """
        初始化函数，用于创建巡逻节点并设置相关参数和客户端
        
        参数:
            node_name (str): 节点名称，默认为'patrol_node'
        """
        super().__init__(node_name)  # 调用父类的初始化方法
        #申明相关参数
        self.declare_parameter('initial_point',[0.0, 0.0, 0.0])  # 声明初始点参数，包含x、y、yaw值
        self.declare_parameter('target_points',[0.0, 0.0, 0.0,1.0,1.0,1.57])  # 声明目标点参数，包含多个x、y、yaw值
        self.declare_parameter('img_save_path','')  # 声明图像保存路径参数

        self.initial_point_= self.get_parameter('initial_point').value  # 获取初始点参数值
        self.target_points_= self.get_parameter('target_points').value  # 获取目标点参数值
        self.img_save_path_ = self.get_parameter('img_save_path').value 


                # ===================== 修复 1：自动创建文件夹 =====================
        if self.img_save_path_ and not os.path.exists(self.img_save_path_):
            os.makedirs(self.img_save_path_)
            self.get_logger().info(f"✅ 自动创建文件夹：{self.img_save_path_}")
            
        self.buffer_=Buffer()  # 创建坐标变换缓冲区
        self.listener_=TransformListener(self.buffer_,self)  # 创建坐标变换监听器
        self.speech_client_=self.create_client(SpeechText,'speech_text') # 创建客户端
        self.cv_bridge_=CvBridge() # 创建CV桥梁对象
        self.latest_img_=None # 最新图像
        self.img_sub_=self.create_subscription(
            Image,
            '/camera/image_raw',
            self.img_callback,
            1) # 订阅图像话题
        
    def img_callback(self,msg):
        self.latest_img_=msg


    def record_image(self):
        if self.latest_img_ is None:
            self.get_logger().warn("⚠️ 未收到相机图像，无法保存！")
            return
        
        if not self.img_save_path_:
            self.get_logger().warn("⚠️ 图片保存路径未配置！")
            return

        try:
            pose=self.get_current_pose()
            cv_img=self.cv_bridge_.imgmsg_to_cv2(self.latest_img_,'bgr8')

            filename = f"img_{pose.translation.x:.2f}_{pose.translation.y:.2f}.png"
            save_path = os.path.join(self.img_save_path_, filename)
            cv2.imwrite(
                save_path,
                cv_img)
            self.get_logger().info(f'✅ 图片已保存：{save_path}')

        except Exception as e:
            self.get_logger().error(f"❌ 保存失败：{str(e)}")



    def get_pose_by_xyyaw(self,x,y,yaw):
            """根据x,y,yaw生成Pose对象"""
            pose=PoseStamped()
            pose.header.frame_id = "map"
            pose.pose.position.x = x
            pose.pose.position.y = y

            # ========== 修复：必须加时间戳 ==========
            pose.header.stamp = self.get_clock().now().to_msg()

            #返回顺序是xyzyaw，所以需要将yaw放在最后一个位置
            quat =quaternion_from_euler(0, 0, yaw) #  将yaw角转换为四元数格式'
            pose.pose.orientation.x = quat[0]
            pose.pose.orientation.y = quat[1]
            pose.pose.orientation.z = quat[2]
            pose.pose.orientation.w = quat[3]
            return pose
    
    def init_robot_pose(self):
        """将机器人初始位置设置为参数中指定的位置"""
        self.initial_point_= self.get_parameter('initial_point').value
        init_pose =self.get_pose_by_xyyaw(self.initial_point_[0],self.initial_point_[1],self.initial_point_[2])
        self.setInitialPose(init_pose)
        self.waitUntilNav2Active() # 等待导航系统激活

    def get_target_points(self):
        """根据参数中指定的目标点生成PoseStamped列表"""
        points=[]
        self.target_points_= self.get_parameter('target_points').value
        for index in range(int(len(self.target_points_)/3)):
            x=self.target_points_[index*3]
            y=self.target_points_[index*3+1]
            yaw=self.target_points_[index*3+2]

            # point_pose =self.get_pose_by_xyyaw(x,y,yaw)
            points.append((x,y,yaw))
            self.get_logger().info(f'获取到目标点{index}: x={x}, y={y}, yaw={yaw}') 
        return points

    def nav_to_pose(self,target_pose):
        """导航到指定的Pose位置"""

        self.goToPose(target_pose)
        while not self.isTaskComplete():
                feedback = self.getFeedback()
                if feedback:
                    # self.get_logger().info(
                    #     f'剩余距离: {feedback.distance_remaining}|'
                    #     f'当前坐标位置: {feedback.current_pose.pose.position}|'
                    #     f'目标坐标位置: {target_pose.pose.position}')
                # self.cancelTask()
                    self.get_logger().info(
                        f'剩余距离: {feedback.distance_remaining:.2f} | '
                        f'当前位置: X:{feedback.current_pose.pose.position.x:.2f} Y:{feedback.current_pose.pose.position.y:.2f} | '
                        f'目标位置: X:{target_pose.pose.position.x:.2f} Y:{target_pose.pose.position.y:.2f}'
                        )
        result = self.getResult()
        self.get_logger().info(f'导航结果: {result}') 

    def get_current_pose(self):
        """获取当前机器人位姿"""
        while rclpy.ok():
            try:
                result= self.buffer_.lookup_transform('map',
                                                        'base_footprint', #  尝试从buffer中获取从'map'坐标系到'base_footprint'坐标系的变换    使用时间为0（最新可用数据），最长等待1秒
                                                        Time(),
                                                        Duration(seconds=2))
                transform=result.transform #  获取变换结果中的变换信息
                self.get_logger().info(f'平移:{transform.translation}') #  记录平移信息到日志
                return transform
            except Exception as e:
                self.get_logger().warn(f'获取坐标失败：原因{str(e)}')              #  如果获取变换失败，记录警告信息到日志

    def speech_text(self,text):
        """调用语音服务朗读指定文本"""
        # 等待语音服务上线，每秒检查一次
        while not self.speech_client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待语音服务未上线，继续等待...')
        # 创建语音服务请求对象
        request = SpeechText.Request()
        # 将要朗读的文本内容填入请求
        request.text.data = text
        # 异步调用语音服务
        future=self.speech_client_.call_async(request)
        # 等待服务调用完成
        rclpy.spin_until_future_complete(self,future)
        # 检查服务调用是否成功
        if future.result() is not None:
            response = future.result()
            # 根据返回结果输出日志
            if response.success == True:
                self.get_logger().warn(f'语音服务调用成功，结果: {response}')
            else:
                self.get_logger().warn(f'语音服务调用失败，结果: {response}')
        else:
            # 服务调用失败，输出异常信息
            self.get_logger().warn(f'语音服务响应失败，原因: {future.exception()}')

  
    

def main():
    rclpy.init()
    patrol= PatrolNode()
    patrol.speech_text('正在准备初始化位置')
    patrol.init_robot_pose()             # rclpy.spin(patrol) # 让节点处理，以确保参数被正确加载
    patrol.speech_text('初始化位置完成，导航开始')

    while rclpy.ok():
        points=patrol.get_target_points()
        for point in points:
            x,y,yaw=point[0],point[1],point[2]
            target_pose=patrol.get_pose_by_xyyaw(x,y,yaw)

            patrol.speech_text(f'正在前往目标点{x},{y},{yaw}')
            patrol.nav_to_pose(target_pose)

            patrol.speech_text(f'已到达目标点{x},{y},{yaw}，正在准备记录图像')
            patrol.record_image()
            patrol.speech_text(f'图像记录完成，继续前往下一个目标点')

    rclpy.shutdown()

    


