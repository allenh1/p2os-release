/* Auto-generated by genmsg_cpp for file /home/rosbuild/hudson/workspace/doc-electric-p2os/doc_stacks/2013-03-01_16-19-23.450784/p2os/p2os_driver/msg/GripState.msg */
#ifndef P2OS_DRIVER_MESSAGE_GRIPSTATE_H
#define P2OS_DRIVER_MESSAGE_GRIPSTATE_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"


namespace p2os_driver
{
template <class ContainerAllocator>
struct GripState_ {
  typedef GripState_<ContainerAllocator> Type;

  GripState_()
  : state(0)
  , dir(0)
  , inner_beam(false)
  , outer_beam(false)
  , left_contact(false)
  , right_contact(false)
  {
  }

  GripState_(const ContainerAllocator& _alloc)
  : state(0)
  , dir(0)
  , inner_beam(false)
  , outer_beam(false)
  , left_contact(false)
  , right_contact(false)
  {
  }

  typedef uint32_t _state_type;
  uint32_t state;

  typedef int32_t _dir_type;
  int32_t dir;

  typedef uint8_t _inner_beam_type;
  uint8_t inner_beam;

  typedef uint8_t _outer_beam_type;
  uint8_t outer_beam;

  typedef uint8_t _left_contact_type;
  uint8_t left_contact;

  typedef uint8_t _right_contact_type;
  uint8_t right_contact;


private:
  static const char* __s_getDataType_() { return "p2os_driver/GripState"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "370eb3507be0ed1043be50a3da3a07c6"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "# direction -1 is inward, +1 is outward, 0 is stationary\n\
uint32 state\n\
int32 dir\n\
bool inner_beam\n\
bool outer_beam\n\
bool left_contact\n\
bool right_contact\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, state);
    ros::serialization::serialize(stream, dir);
    ros::serialization::serialize(stream, inner_beam);
    ros::serialization::serialize(stream, outer_beam);
    ros::serialization::serialize(stream, left_contact);
    ros::serialization::serialize(stream, right_contact);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, state);
    ros::serialization::deserialize(stream, dir);
    ros::serialization::deserialize(stream, inner_beam);
    ros::serialization::deserialize(stream, outer_beam);
    ros::serialization::deserialize(stream, left_contact);
    ros::serialization::deserialize(stream, right_contact);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(state);
    size += ros::serialization::serializationLength(dir);
    size += ros::serialization::serializationLength(inner_beam);
    size += ros::serialization::serializationLength(outer_beam);
    size += ros::serialization::serializationLength(left_contact);
    size += ros::serialization::serializationLength(right_contact);
    return size;
  }

  typedef boost::shared_ptr< ::p2os_driver::GripState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::p2os_driver::GripState_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct GripState
typedef  ::p2os_driver::GripState_<std::allocator<void> > GripState;

typedef boost::shared_ptr< ::p2os_driver::GripState> GripStatePtr;
typedef boost::shared_ptr< ::p2os_driver::GripState const> GripStateConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::p2os_driver::GripState_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::p2os_driver::GripState_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace p2os_driver

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::p2os_driver::GripState_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::p2os_driver::GripState_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::p2os_driver::GripState_<ContainerAllocator> > {
  static const char* value() 
  {
    return "370eb3507be0ed1043be50a3da3a07c6";
  }

  static const char* value(const  ::p2os_driver::GripState_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x370eb3507be0ed10ULL;
  static const uint64_t static_value2 = 0x43be50a3da3a07c6ULL;
};

template<class ContainerAllocator>
struct DataType< ::p2os_driver::GripState_<ContainerAllocator> > {
  static const char* value() 
  {
    return "p2os_driver/GripState";
  }

  static const char* value(const  ::p2os_driver::GripState_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::p2os_driver::GripState_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# direction -1 is inward, +1 is outward, 0 is stationary\n\
uint32 state\n\
int32 dir\n\
bool inner_beam\n\
bool outer_beam\n\
bool left_contact\n\
bool right_contact\n\
\n\
";
  }

  static const char* value(const  ::p2os_driver::GripState_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::p2os_driver::GripState_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::p2os_driver::GripState_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.state);
    stream.next(m.dir);
    stream.next(m.inner_beam);
    stream.next(m.outer_beam);
    stream.next(m.left_contact);
    stream.next(m.right_contact);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GripState_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::p2os_driver::GripState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::p2os_driver::GripState_<ContainerAllocator> & v) 
  {
    s << indent << "state: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.state);
    s << indent << "dir: ";
    Printer<int32_t>::stream(s, indent + "  ", v.dir);
    s << indent << "inner_beam: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.inner_beam);
    s << indent << "outer_beam: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.outer_beam);
    s << indent << "left_contact: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.left_contact);
    s << indent << "right_contact: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.right_contact);
  }
};


} // namespace message_operations
} // namespace ros

#endif // P2OS_DRIVER_MESSAGE_GRIPSTATE_H
