// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autopatrol_interfaces:srv/SpeechText.idl
// generated code does not contain a copyright notice

#ifndef AUTOPATROL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__STRUCT_HPP_
#define AUTOPATROL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'text'
#include "std_msgs/msg/detail/string__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__autopatrol_interfaces__srv__SpeechText_Request __attribute__((deprecated))
#else
# define DEPRECATED__autopatrol_interfaces__srv__SpeechText_Request __declspec(deprecated)
#endif

namespace autopatrol_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SpeechText_Request_
{
  using Type = SpeechText_Request_<ContainerAllocator>;

  explicit SpeechText_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : text(_init)
  {
    (void)_init;
  }

  explicit SpeechText_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : text(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _text_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _text_type text;

  // setters for named parameter idiom
  Type & set__text(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->text = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autopatrol_interfaces__srv__SpeechText_Request
    std::shared_ptr<autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autopatrol_interfaces__srv__SpeechText_Request
    std::shared_ptr<autopatrol_interfaces::srv::SpeechText_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SpeechText_Request_ & other) const
  {
    if (this->text != other.text) {
      return false;
    }
    return true;
  }
  bool operator!=(const SpeechText_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SpeechText_Request_

// alias to use template instance with default allocator
using SpeechText_Request =
  autopatrol_interfaces::srv::SpeechText_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace autopatrol_interfaces


#ifndef _WIN32
# define DEPRECATED__autopatrol_interfaces__srv__SpeechText_Response __attribute__((deprecated))
#else
# define DEPRECATED__autopatrol_interfaces__srv__SpeechText_Response __declspec(deprecated)
#endif

namespace autopatrol_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SpeechText_Response_
{
  using Type = SpeechText_Response_<ContainerAllocator>;

  explicit SpeechText_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit SpeechText_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autopatrol_interfaces__srv__SpeechText_Response
    std::shared_ptr<autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autopatrol_interfaces__srv__SpeechText_Response
    std::shared_ptr<autopatrol_interfaces::srv::SpeechText_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SpeechText_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const SpeechText_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SpeechText_Response_

// alias to use template instance with default allocator
using SpeechText_Response =
  autopatrol_interfaces::srv::SpeechText_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace autopatrol_interfaces

namespace autopatrol_interfaces
{

namespace srv
{

struct SpeechText
{
  using Request = autopatrol_interfaces::srv::SpeechText_Request;
  using Response = autopatrol_interfaces::srv::SpeechText_Response;
};

}  // namespace srv

}  // namespace autopatrol_interfaces

#endif  // AUTOPATROL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__STRUCT_HPP_
