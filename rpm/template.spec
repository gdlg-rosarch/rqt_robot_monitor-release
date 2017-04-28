Name:           ros-indigo-rqt-robot-monitor
Version:        0.5.7
Release:        0%{?dist}
Summary:        ROS rqt_robot_monitor package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_robot_monitor
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-python-qt-binding >= 0.2.19
Requires:       ros-indigo-qt-gui
Requires:       ros-indigo-qt-gui-py-common
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-bag
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
Requires:       ros-indigo-rqt-py-common
BuildRequires:  ros-indigo-catkin

%description
rqt_robot_monitor displays diagnostics_agg topics messages that are published by
diagnostic_aggregator. rqt_robot_monitor is a direct port to rqt of
robot_monitor. All diagnostics are fall into one of three tree panes depending
on the status of diagnostics (normal, warning, error/stale). Status are shown in
trees to represent their hierarchy. Worse status dominates the higher level
status. Ex. 'Computer' category has 3 sub devices. 2 are green but 1 is error.
Then 'Computer' becomes error. You can look at the detail of each status by
double-clicking the tree nodes. Currently re-usable API to other pkgs are not
explicitly provided.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Fri Apr 28 2017 Aaron Blasdel <ablasdel@gmail.com> - 0.5.7-0
- Autogenerated by Bloom

