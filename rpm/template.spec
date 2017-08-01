Name:           ros-lunar-p2os-teleop
Version:        2.1.0
Release:        0%{?dist}
Summary:        ROS p2os_teleop package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/p2os-purdue
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-tf
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-tf

%description
A teleoperation node for the p2os_driver package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Aug 01 2017 Hunter L. Allen <hunter@openrobotics.org> - 2.1.0-0
- Autogenerated by Bloom

* Tue May 30 2017 Hunter L. Allen <hunter@openrobotics.org> - 2.0.7-0
- Autogenerated by Bloom

* Tue May 30 2017 Hunter Allen <allen286@purdue.edu> - 2.0.6-3
- Autogenerated by Bloom

* Tue May 30 2017 Hunter Allen <allen286@purdue.edu> - 2.0.6-2
- Autogenerated by Bloom

* Tue May 30 2017 Hunter Allen <allen286@purdue.edu> - 2.0.6-1
- Autogenerated by Bloom

* Tue May 23 2017 Hunter Allen <allen286@purdue.edu> - 2.0.6-0
- Autogenerated by Bloom

