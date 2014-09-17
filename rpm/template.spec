Name:           ros-hydro-moveit-visual-tools
Version:        1.3.0
Release:        0%{?dist}
Summary:        ROS moveit_visual_tools package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/davetcoleman/moveit_visual_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-graph-msgs
Requires:       ros-hydro-moveit-core
Requires:       ros-hydro-moveit-msgs
Requires:       ros-hydro-moveit-ros-robot-interaction
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-trajectory-msgs
Requires:       ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-eigen-conversions
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-graph-msgs
BuildRequires:  ros-hydro-moveit-core
BuildRequires:  ros-hydro-moveit-msgs
BuildRequires:  ros-hydro-moveit-ros-robot-interaction
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf-conversions
BuildRequires:  ros-hydro-trajectory-msgs
BuildRequires:  ros-hydro-visualization-msgs

%description
Helper functions for displaying and debugging MoveIt! data in Rviz via published
markers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Sep 17 2014 Dave Coleman <davetcoleman@gmail.com> - 1.3.0-0
- Autogenerated by Bloom

* Thu Jul 31 2014 Dave Coleman <davetcoleman@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

* Mon Aug 11 2014 Dave Coleman <davetcoleman@gmail.com> - 1.2.1-0
- Autogenerated by Bloom

* Fri Aug 08 2014 Dave Coleman <davetcoleman@gmail.com> - 1.2.0-0
- Autogenerated by Bloom

