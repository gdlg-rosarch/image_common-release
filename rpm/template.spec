Name:           ros-indigo-image-transport
Version:        1.11.10
Release:        0%{?dist}
Summary:        ROS image_transport package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/image_transport
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-filters
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-sensor-msgs

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
* Tue Jan 19 2016 Jack O'Quin <jack.oquin@gmail.com> - 1.11.10-0
- Autogenerated by Bloom

* Sun Jan 17 2016 Jack O'Quin <jack.oquin@gmail.com> - 1.11.9-0
- Autogenerated by Bloom

* Sun Nov 29 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

* Tue Jul 28 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.6-0
- Autogenerated by Bloom

* Thu May 14 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.5-0
- Autogenerated by Bloom

