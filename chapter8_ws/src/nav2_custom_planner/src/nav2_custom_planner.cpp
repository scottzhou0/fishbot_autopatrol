#include "nav2_util/node_utils.hpp"
#include <cmath>
#include <memory>
#include <string>

#include "nav2_custom_planner/nav2_custom_planner.hpp"
#include "nav2_core/exceptions.hpp"


namespace nav2_custom_planner
{
    void CustomPlanner::configure(
        const rclcpp_lifecycle::LifecycleNode::WeakPtr & parent,
        const std::string name,
        std::shared_ptr<tf2_ros::Buffer> tf,
        std::shared_ptr<nav2_costmap_2d::Costmap2DROS> costmap_ros)

        {
            tf_ = tf;
            node_ = parent.lock();
            name_ = name;
            costmap_ = costmap_ros->getCostmap();
            global_frame_ = costmap_ros->getGlobalFrameID();

            //参数初始化
            nav2_util::declare_parameter_if_not_declared(
                node_, name_ + ".interpolation_resolution", rclcpp::ParameterValue(0.1));

            node_->get_parameter(
                name_ + ".interpolation_resolution", interpolation_resolution_);
            
            RCLCPP_INFO(node_->get_logger(), "已配置 CustomPlanner的插件 %.2f" , interpolation_resolution_);
        }

        void CustomPlanner::cleanup()
        {
            RCLCPP_INFO(node_->get_logger(), "正在清理 CustomPlanner的插件 %s" , name_.c_str());
        }

        void CustomPlanner::activate()
        {
            RCLCPP_INFO(node_->get_logger(), "正在激活 CustomPlanner的插件 %s" , name_.c_str());
        }

        void CustomPlanner::deactivate()
        {
            RCLCPP_INFO(node_->get_logger(), "正在停用 CustomPlanner的插件 %s" , name_.c_str());
        }

        //规划方法，当前仅返回一个空路径
        nav_msgs::msg::Path 
        CustomPlanner::createPlan(
            const geometry_msgs::msg::PoseStamped & start,
            const geometry_msgs::msg::PoseStamped & goal)
        {
            nav_msgs::msg::Path global_path;
            // 必须设置路径的坐标系（和起点/终点一致）
            global_path.poses.clear();
            global_path.header.frame_id = start.header.frame_id;
            global_path.header.stamp = node_->now();

            // 检查起点和终点是否在同一个坐标系下
            if (start.header.frame_id != global_frame_) {
                RCLCPP_ERROR(node_->get_logger(), "规划器仅接受来自%s 坐标系的起始位置坐标系为%s", 
                            global_frame_.c_str(), start.header.frame_id.c_str());
                return global_path;
            }

            if(goal.header.frame_id != global_frame_) {
                RCLCPP_ERROR(node_->get_logger(), "规划器仅接受来自%s 坐标系标位置，但收到的目标坐标系为%s", 
                            global_frame_.c_str(), goal.header.frame_id.c_str());
                return global_path;
            }

            //3.0 计算当前起点和终点的距离，循环次数和步进数值
            int total_number_of_loop =
                std::hypot(goal.pose.position.x - start.pose.position.x, 
                        goal.pose.position.y - start.pose.position.y) / 
                        interpolation_resolution_;
            double step_x = (goal.pose.position.x - start.pose.position.x) / total_number_of_loop;
            double step_y = (goal.pose.position.y - start.pose.position.y) / total_number_of_loop;

            //4.0 插值生成路径点
            for (int i = 0; i < total_number_of_loop; ++i)
            {   
                geometry_msgs::msg::PoseStamped pose; //生成一个点
                pose.pose.position.x = start.pose.position.x + step_x * i;
                pose.pose.position.y = start.pose.position.y + step_y * i;
                pose.pose.position.z = 0.0; // 假设z=0

                pose.header.frame_id = start.header.frame_id;
                pose.header.stamp = node_->now(); // 使用当前时间戳

                global_path.poses.push_back(pose); // 将生成的点加入路径

                // 5.0 使用costmap检查路径点是否可行（这里简单示例，实际应用中需要考虑机器人的尺寸和安全距离）
                for (geometry_msgs::msg::PoseStamped pose: global_path.poses)
                {
                    unsigned int mx, my;
                    if (costmap_->worldToMap(pose.pose.position.x, pose.pose.position.y, mx, my)) 
                    {
                        unsigned char cost = costmap_->getCost(mx, my); //获取对应栅格的代价值
                        //如果存在致命障碍物，则抛出异常
                        if (cost == nav2_costmap_2d::LETHAL_OBSTACLE) 
                        {
                            RCLCPP_WARN(node_->get_logger(), "路径点 (%.2f, %.2f) 位于障碍物上，跳过该点",
                                        pose.pose.position.x, pose.pose.position.y);
                            throw nav2_core::PlannerException(
                                "路径点位于障碍物上，无法规划:"+std::to_string(pose.pose.position.x)+","+std::to_string(pose.pose.position.y));
                
                        }
                    }
                }
                // 6.0 返回生成的路径
                geometry_msgs::msg::PoseStamped goal_pose = goal;
                goal_pose.header.stamp = node_->now(); // 更新目标点的时间戳
                goal_pose.header.frame_id = global_frame_;

                global_path.poses.push_back(goal_pose); // 将目标点加入路径
             }
             return global_path; // 返回生成的路径
        }
        
}

#include "pluginlib/class_list_macros.hpp"
PLUGINLIB_EXPORT_CLASS(nav2_custom_planner::CustomPlanner, 
                        nav2_core::GlobalPlanner)
