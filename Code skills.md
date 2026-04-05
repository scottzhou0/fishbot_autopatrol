# 1 Git 建号
## Gitee 账号与仓库
- scottzhou0 Token 8415b0c846616d6296adac655b8726f1
- Github 没有额外额密码
    - ssh-keygen
    - cat ~/.ssh/id_rsa.pub
    

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
- 

## 3.3. 安装键盘控制
- ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/velocity_controller/cmd_vel_unstamped

- ros2 run topic_tools relay /cmd_vel /velocity_controller/cmd_vel_unstamped **中继命令**