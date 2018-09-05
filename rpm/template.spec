Name:           ros-melodic-p2os-driver
Version:        2.1.1
Release:        3%{?dist}
Summary:        ROS p2os_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/p2os_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-kdl-parser
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-p2os-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-tf
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-kdl-parser
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-p2os-msgs
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-tf

%description
Driver file descriptions for P2OS/ARCOS robot

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
* Wed Sep 05 2018 Hunter L. Allen <hunter@openrobotics.org> - 2.1.1-3
- Autogenerated by Bloom

* Tue Sep 04 2018 Hunter L. Allen <hunter@openrobotics.org> - 2.1.1-2
- Autogenerated by Bloom

* Thu Aug 30 2018 Hunter L. Allen <hunter@openrobotics.org> - 2.1.1-1
- Autogenerated by Bloom

* Tue Jul 03 2018 Hunter L. Allen <hunter@openrobotics.org> - 2.1.1-0
- Autogenerated by Bloom

