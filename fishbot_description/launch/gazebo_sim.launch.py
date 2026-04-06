import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
import os
import launch_ros.parameter_descriptions


def generate_launch_description():
    #获取urdf路径
    urdf_package_path= get_package_share_directory('fishbot_description')

    default_xacro_path =os.path.join(urdf_package_path,'urdf','fishbot/fishbot.urdf.xacro')
    #default_rviz_config_path=os.path.join(urdf_package_path,'config','display_robot_model.rviz')
    default_gazebo_world_path=os.path.join(urdf_package_path,'world','custom_room.world')
    #声明一个urdf的目录参数，方便修改
    action_declare_arg_mode_path =launch.actions.DeclareLaunchArgument(
        name='model',
        default_value=str(default_xacro_path),
        description='加载模型的文件路径'
    )
    #通过文件路径获取内容并转化为参数值对象，以供传入robot_state_publisher
    substitutions_command_result=launch.substitutions.Command(
        ['xacro ',launch.substitutions.LaunchConfiguration('model')]
        )
    
    robot_description_value=launch_ros.parameter_descriptions.ParameterValue(
        substitutions_command_result,
        value_type=str
        )

    action_robot_state_publisher =launch_ros.actions.Node(
        package ='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description':robot_description_value}])

    action_joint_state_publisher =launch_ros.actions.Node(
        package ='joint_state_publisher',
        executable='joint_state_publisher'
    )

    # action_rviz_node=launch_ros.actions.Node(
    #     package ='rviz2',
    #     executable='rviz2',
    #     arguments= ['-d', default_rviz_config_path]
    # )
    action_launch_gazebo = launch.actions.IncludeLaunchDescription(
    # 修正1：路径拼接（Launch→launch，用os.path.join更规范）
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',  # 小写launch，匹配实际目录
                'gazebo.launch.py'
            )
        ),
        launch_arguments=[
            ('world',default_gazebo_world_path),
            ('verbose','true')
        ]

    )
    action_spawn_entity = launch_ros.actions.Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic',
            '/robot_description',
            '-entity',
            'fishbot',
            '-x',
            '0.0',
            '-y',
            '0.0',
            '-z',
            '0.1'
            ]        
    )

    action_load_joint_state_controller = launch.actions.ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'fishbot_joint_state_broadcaster'],
        output='screen',
    )

        # 加载差速驱动控制器（关节控制器加载完成后）
    action_load_diff_drive_controller = launch.actions.ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'velocity_controller'],
        output='screen',
    )

    action_load_effort_controller = launch.actions.ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'fishbot_effort_controller'],
        output='screen',
    )

        # 事件处理：生成实体后先加载关节控制器，再加载差速控制器
    # ========== 事件处理器：严格链式加载（移除硬编码sleep，改用事件依赖） ==========
    # 层级1: effort控制器加载完成后，加载差速控制器
    handler_diff_after_effort = launch.actions.RegisterEventHandler(
        launch.event_handlers.OnProcessExit(
            target_action=action_load_effort_controller,
            on_exit=[action_load_diff_drive_controller]
            # 明确事件类型，避免误触发
            )
    )

    # 层级2: 关节控制器加载完成后，加载effort控制器 + 注册差速控制器监听
    handler_effort_after_joint = launch.actions.RegisterEventHandler(
        launch.event_handlers.OnProcessExit(
            target_action=action_load_joint_state_controller,
            on_exit=[
                action_load_effort_controller,
                handler_diff_after_effort
            ]
        )
    )

    # 层级3: 实体生成完成后，加载关节控制器 + 注册后续监听
    event_handler = launch.event_handlers.OnProcessExit(
        target_action=action_spawn_entity,
        on_exit=[
            action_load_joint_state_controller,
            handler_effort_after_joint
        ]
    )
 
    return launch.LaunchDescription([
        action_declare_arg_mode_path,
        action_robot_state_publisher,
        action_joint_state_publisher,
        action_launch_gazebo,
        action_spawn_entity,
        # action_rviz_node
        launch.actions.RegisterEventHandler(event_handler),     
        launch.actions.LogInfo(msg="FishBot Gazebo仿真启动中...") 
    ])