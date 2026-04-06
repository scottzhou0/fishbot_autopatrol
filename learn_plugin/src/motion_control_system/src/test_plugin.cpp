#include "motion_control_system/motion_control_interface.hpp"
#include <pluginlib/class_loader.hpp>

int main(int argc, char** argv)
{
    if (argc !=2) //  检查命令行参数数量是否为2（程序名+1个参数）
        return 0;
    
    std::string controller_name = argv[1];   //  从命令行参数获取控制器名称
    pluginlib::ClassLoader<motion_control_system::MotionController>  //  创建插件加载器，用于加载MotionController类型的插件     参数1: 插件基类所在的包名     参数2: 插件基类的完整名称（包含命名空间）
        controller_loader(
            "motion_control_system", 
            "motion_control_system::MotionController"
        );
    auto controller = controller_loader.createSharedInstance(controller_name); //  使用插件加载器创建指定名称控制器的共享实例
    controller->start(); //  启动控制器
    controller->stop(); //  停止控制器
    return 0;
}