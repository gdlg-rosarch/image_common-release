Name:           ros-kinetic-camera-calibration-parsers
Version:        1.11.11
Release:        0%{?dist}
Summary:        ROS camera_calibration_parsers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/camera_calibration_parsers
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roscpp-serialization
Requires:       ros-kinetic-sensor-msgs
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rosbash
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roscpp-serialization
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  yaml-cpp-devel

%description
camera_calibration_parsers contains routines for reading and writing camera
calibration parameters.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Sep 24 2016 Jack O'Quin <jack.oquin@gmail.com> - 1.11.11-0
- Autogenerated by Bloom

* Thu Mar 17 2016 Jack O'Quin <jack.oquin@gmail.com> - 1.11.10-0
- Autogenerated by Bloom

