Name:           ros-indigo-moveit-visual-tools
Version:        3.0.2
Release:        0%{?dist}
Summary:        ROS moveit_visual_tools package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/davetcoleman/moveit_visual_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-graph-msgs
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-moveit-ros-robot-interaction
Requires:       ros-indigo-rviz-visual-tools
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-graph-msgs
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-moveit-ros-robot-interaction
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rviz-visual-tools
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf-conversions
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
Helper functions for displaying and debugging MoveIt! data in Rviz via published
markers

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
* Sun Dec 27 2015 Dave Coleman <davetcoleman@gmail.com> - 3.0.2-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Dave Coleman <davetcoleman@gmail.com> - 3.0.1-0
- Autogenerated by Bloom

* Wed Dec 02 2015 Dave Coleman <davetcoleman@gmail.com> - 3.0.0-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Dave Coleman <davetcoleman@gmail.com> - 2.2.0-0
- Autogenerated by Bloom

