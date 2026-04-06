# 1 Git 建号
## Gitee 账号与仓库
- scottzhou0 Token 8415b0c846616d6296adac655b8726f1
    - ssh-keygen
    - cat ~/.ssh/id_rsa.pub
-git remote add origin https://gitee.com/scottzhou0/ros2_patrol_robot.git
- git remote set-url --add --push origin https://gitee.com/scottzhou0/ros2_patrol_robot.git
- git remote set-url --add --push origin https://github.com/scottzhou0/fishbot_autopatrol.git
- 推 Gitee：git push
- 推 GitHub：git push github master 

# 2 Git 命令
- git init
- git add .
- git commit -m "first commit"
- git remote add origin https://gitee.com/scottzhou0/autopatrol_robot.git
- git remote add github https://github.com/scottzhou0/fishbot_autopatrol.git #双推送管理
- git remote -v
- git push -u origin master

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