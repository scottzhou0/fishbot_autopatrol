# 1 Git 建号
## 1.1 Gitee 账号与仓库
- scottzhou0 Token 8415b0c846616d6296adac655b8726f1
    - ssh-keygen
    - cat ~/.ssh/id_rsa.pub
- git remote add origin https://gitee.com/scottzhou0/ros2_patrol_robot.git
- git remote set-url --add --push origin https://gitee.com/scottzhou0/ros2_patrol_robot.git
- git remote set-url --add --push origin https://github.com/scottzhou0/fishbot_autopatrol.git
- git init
- git add .
- rm -f /home/scott/.git/index.lock
- git commit -m "first commit"
- git push origin master
- git push github master
- 推 Gitee：git push
- 推 GitHub：git push github master 

## 1.2 Git 命令
- git init
- git add .
- git commit -m "first commit"
- git remote add origin https://gitee.com/scottzhou0/autopatrol_robot.git
- git remote add github https://github.com/scottzhou0/fishbot_autopatrol.git #双推送管理
- git remote -v
- git push -u origin master
# 2 C++ 基础
## 2.1 C++ 基础
- C++ 基础语法
- C++ 基础数据类型
- C++ 基础运算符
- C++ 基础控制语句
- C++ 基础函数
# 3 ROS2
## 3.1. 安装
- sudo apt update
- sudo apt install ros-humble-desktop
- sudo apt install ros-humble-ros2-launch
- sudo apt install ros-humble-ros2-control
- sudo apt install ros-humble-ros2-controllers
- sudo apt install ros-humble-ros2-navigation
- sudo apt install ros-humble-ros2-tf2-geometry-msgs
- sudo apt install ros-humble-ros2-tf2
- sudo apt install ros-humble-ros2-tf2-ros
- sudo apt install ros-humble-ros2-tf2-ros2
- sudo apt install ros-humble-ros2-tf2-ros1
- sudo apt install ros-humble-ros2-tf2-ros1-bridge
- sudo apt install ros-humble-ros2-tf2-ros1-bridge
## 3.2 导航相关
- sudo apt install ros-$ROS_DISTRO-slam-toolbox
- sudo apt install ros-$ROS_DISTRO-nav2-map-server
- sudo apt install ros-$ROS_DISTRO-pluginlib -y
   ![alt text](image.png)
## 3.2.1 高阶导航使用方法,C++ 方法
- ros2 pkg create motion_control_system --dependencies pluginlib --license Apache-2.0
## 3.2.2 自定义规划器搭建
- 创建工作包 ros2 pkg create nav2_custom_planner --dependencies pluginlib nav2_core
## 3.2.3 自定义规划路径算法

## 3.2.4 自定义控制器
- ros2 pkg create nav2_custom_controller --build-type ament_cmake --dependencies pluginlib nav2_core


## 3.3. 安装键盘控制
- ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/velocity_controller/cmd_vel_unstamped
- ros2 run topic_tools relay /cmd_vel /velocity_controller/cmd_vel_unstamped **中继命令**


# 4 Linux 常用的指令
## 4.1 操作文件夹
- mkdir -p /home/scottzhou0/autopatrol_robot
- cd /home/scottzhou0/autopatrol_robot
- rm -rf /home/scottzhou0/autopatrol_robot
- cp -r /home/scottzhou0/autopatrol_robot /home/scottzhou0/autopatrol_robot_bak
- 移动文件夹 mv /home/scottzhou0/autopatrol_robot_bak /home/scottzhou0/autopatrol_robot
- 重命名 mv /home/scottzhou0/autopatrol_robot /home/scottzhou0/autopatrol_robot_bak
- pwd

- ls
- ls -l 详细信息
- ls -a 查看隐藏文件

# 5. 编译的
- colcon build --packages-select motion_control_system

# 6. 实战fishbot，
## 6.1 安装fishbot_tool 配置软件
- git clone https://github.com/fishros/fishbot_tool.git
  根据Readme 使用下载相关以来，使用python3 运行main.py 源码价值的烧录软件的界面
- 注意事项:WSL使用需要共享USB端口给到WSL中，
    usbipd bind --busid 2-2
    usbipd attach --wsl --busid 2-2
    - ls /dev/ttyUSB*
    /dev/ttyUSB0 #看到这个信息，说明WSL USB 串口加载成功了

安装docker，拉取microROS
sudo docker run -it --rm -v /dev:/dev -v /dev/shm:/dev/shm --privileged --net=host microros/micro-ros-agent:$ROS_DISTRO udp4 --port 8888 -v6

<!-- powershell 向 wsl转发的方法
netsh interface portproxy add v4tov4 listenport=8888 listenaddress=0.0.0.0 connectport=8888 connectaddress=172.24.129.150
netsh interface portproxy show v4tov4 -->

## 6.2 解决WLS 网络通信问题，WSL 的IP地址与Windows 地址不一致
    1. 新建
    C:\Users\你的用户名\.wslconfig
    2. 复制
    [wsl2]
    networkingMode=mirrored
    dnsTunneling=true
    firewall=true
    autoMemoryReclaim=gradual
    3. 关闭
    wsl --shutdown
    4.检查
    hostname -I
    5. ROS 环境变量（WSL 内）
    # 临时生效
    export ROS_MASTER_URI=http://$(hostname -I | awk '{print $1}'):11311
    export ROS_IP=$(hostname -I | awk '{print $1}')

    # 永久生效（写入 ~/.bashrc）
    echo "export ROS_MASTER_URI=http://$(hostname -I | awk '{print $1}'):11311" >> ~/.bashrc
    echo "export ROS_IP=$(hostname -I | awk '{print $1}')" >> ~/.bashrc
source ~/.bashrc

## 6.3 安装雷达，以及雷达驱动 https://fishros.org.cn/forum/topic/954/fishbot%E6%95%99%E7%A8%8B-9-0-6-%E9%9B%B7%E8%BE%BE%E9%A9%B1%E5%8A%A8%E5%8F%8A%E5%BB%BA%E5%9B%BE%E6%B5%8B%E8%AF%95
国内镜像
xhost + && sudo docker run -it --rm -p 8889:8889 -p 8889:8889/udp -v /dev:/dev -v /tmp/.X11-unix:/tmp/.X11-unix --device /dev/snd -e DISPLAY=unix$DISPLAY registry.cn-hangzhou.aliyuncs.com/fishros/fishbot_laser
国外镜像
xhost + && sudo docker run -it --rm -p 8889:8889 -p 8889:8889/udp -v /dev:/dev -v /tmp/.X11-unix:/tmp/.X11-unix --device /dev/snd -e DISPLAY=unix$DISPLAY  fishros2/fishbot_laser

监听端口 nc -l 8889
清理 Docker端口占用的问题
sudo docker ps -q | xargs -r sudo docker stop
sudo docker ps -a -q | xargs -r sudo docker rm -f

powershell 查询端口命令 netstat -ano | findstr :8889
杀掉进程taskkill /F /PID 5656


### 6.3.1 安装laserscan, Rviz2 建图
sudo apt install nav2_map_server
ros2 run nav2_map_server map_server 

ros2 topic list
ros2 topic hz /scan
ros2 topic echo /scan
rivz2

## 6.4 测试驱动板
ros2 node list
ros2 node info /fishbot_motion_control
ros2 topic echo /imu --once

# 7. 单片机开发基础
## 7.1. 安装Arduino IDE
- sudo apt install python3-venv


- sudo apt install arduino
- arduino
- . bin/activate
- pip install platformio
- pio 命令
   [env:fishbot]
    platform = espressif32
    board = esp32dev
    framework = arduino




  
  

