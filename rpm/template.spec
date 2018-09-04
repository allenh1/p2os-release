Name:           ros-melodic-p2os-msgs
Version:        2.1.1
Release:        2%{?dist}
Summary:        ROS p2os_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/p2os-purdue
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-message-generation
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-std-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-std-msgs

%description
Defines the messages that are used to communicate with the p2os_driver package
and the ROS infrastructure.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Sep 04 2018 Hunter L. Allen <hunter@openrobotics.org> - 2.1.1-2
- Autogenerated by Bloom

* Thu Aug 30 2018 Hunter L. Allen <hunter@openrobotics.org> - 2.1.1-1
- Autogenerated by Bloom

* Tue Jul 03 2018 Hunter L. Allen <hunter@openrobotics.org> - 2.1.1-0
- Autogenerated by Bloom

