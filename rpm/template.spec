Name:           ros-indigo-p2os-doc
Version:        1.0.11
Release:        3%{?dist}
Summary:        ROS p2os_doc package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/p2os_msgs
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin

%description
Contains the Documentation for the p2os driver/componenets

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Jul 11 2015 Hunter Allen <hunter.allen@vanderbilt.edu> - 1.0.11-3
- Autogenerated by Bloom

* Sat May 02 2015 Hunter Allen <hunter.allen@vanderbilt.edu> - 1.0.11-2
- Autogenerated by Bloom

* Sat May 02 2015 Hunter Allen <hunter.allen@vanderbilt.edu> - 1.0.11-1
- Autogenerated by Bloom

