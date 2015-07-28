Name:           ros-jade-image-transport
Version:        1.11.7
Release:        0%{?dist}
Summary:        ROS image_transport package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/image_transport
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-message-filters
Requires:       ros-jade-pluginlib
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp
Requires:       ros-jade-roslib
Requires:       ros-jade-sensor-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-sensor-msgs

%description
image_transport should always be used to subscribe to and publish images. It
provides transparent support for transporting images in low-bandwidth compressed
formats. Examples (provided by separate plugin packages) include JPEG/PNG
compression and Theora streaming video.

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
* Tue Jul 28 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.6-0
- Autogenerated by Bloom

* Thu May 14 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.5-0
- Autogenerated by Bloom

* Thu Jan 01 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.4-0
- Autogenerated by Bloom

