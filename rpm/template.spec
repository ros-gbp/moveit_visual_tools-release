Name:           ros-jade-moveit-visual-tools
Version:        3.1.0
Release:        0%{?dist}
Summary:        ROS moveit_visual_tools package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/davetcoleman/moveit_visual_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-cmake-modules
Requires:       ros-jade-eigen-conversions
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-graph-msgs
Requires:       ros-jade-moveit-core
Requires:       ros-jade-moveit-ros-robot-interaction
Requires:       ros-jade-roscpp
Requires:       ros-jade-roslint
Requires:       ros-jade-rviz-visual-tools
Requires:       ros-jade-std-msgs
Requires:       ros-jade-tf-conversions
Requires:       ros-jade-trajectory-msgs
Requires:       ros-jade-visualization-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-graph-msgs
BuildRequires:  ros-jade-moveit-core
BuildRequires:  ros-jade-moveit-ros-robot-interaction
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslint
BuildRequires:  ros-jade-rviz-visual-tools
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf-conversions
BuildRequires:  ros-jade-trajectory-msgs
BuildRequires:  ros-jade-visualization-msgs

%description
Helper functions for displaying and debugging MoveIt! data in Rviz via published
markers

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
* Thu Apr 28 2016 Dave Coleman <davetcoleman@gmail.com> - 3.1.0-0
- Autogenerated by Bloom

* Tue Feb 09 2016 Dave Coleman <davetcoleman@gmail.com> - 3.0.5-0
- Autogenerated by Bloom

* Mon Jan 04 2016 Dave Coleman <davetcoleman@gmail.com> - 3.0.2-0
- Autogenerated by Bloom

* Sat Dec 05 2015 Dave Coleman <davetcoleman@gmail.com> - 3.0.1-0
- Autogenerated by Bloom

* Thu Dec 03 2015 Dave Coleman <davetcoleman@gmail.com> - 3.0.0-0
- Autogenerated by Bloom

