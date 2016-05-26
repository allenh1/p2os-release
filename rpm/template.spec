Name:           ros-jade-p2os-launch
Version:        2.0.4
Release:        0%{?dist}
Summary:        ROS p2os_launch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/p2os-vanderbilt
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-jade-catkin

%description
Launch and config files designed for use with the p2os stack.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu May 26 2016 Hunter Allen <allen286@purdue.edu> - 2.0.4-0
- Autogenerated by Bloom

* Sun Oct 25 2015 Hunter Allen <allen286@purdue.edu> - 2.0.3-0
- Autogenerated by Bloom

* Tue Aug 04 2015 Hunter Allen <allen286@purdue.edu> - 2.0.2-0
- Autogenerated by Bloom

* Sat Jul 11 2015 Hunter Allen <allen286@purdue.edu> - 2.0.1-0
- Autogenerated by Bloom

* Sat May 02 2015 Hunter Allen <allen286@purdue.edu> - 2.0.0-0
- Autogenerated by Bloom

