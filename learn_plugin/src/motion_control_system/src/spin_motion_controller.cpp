#include <iostream>
#include "motion_control_system/spin_motion_controller.hpp"

namespace motion_control_system
{
/**
 * @brief SpinMotionController类的start函数实现
 * 该函数用于启动旋转运动控制器
 */
void SpinMotionController::start()
{
    std::cout << "SpinMotionController::start()" << std::endl;  // 输出函数调用信息到控制台
}
    void SpinMotionController::stop()
    {
        std::cout << "SpinMotionController::stop()" << std::endl;
    }
}

#include "pluginlib/class_list_macros.hpp"
PLUGINLIB_EXPORT_CLASS(
    motion_control_system::SpinMotionController, 
    motion_control_system::MotionController
)
