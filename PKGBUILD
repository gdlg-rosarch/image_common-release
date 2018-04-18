# Script generated with Bloom
pkgdesc="ROS - This package provides a C++ interface for camera calibration information. It provides CameraInfo, and handles SetCameraInfo service requests, saving and restoring the camera calibration data."
url='http://ros.org/wiki/camera_info_manager'

pkgname='ros-melodic-camera-info-manager'
pkgver='1.11.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'gtest'
'ros-melodic-camera-calibration-parsers'
'ros-melodic-catkin>=0.5.68'
'ros-melodic-image-transport'
'ros-melodic-roscpp'
'ros-melodic-roslib'
'ros-melodic-rostest'
'ros-melodic-sensor-msgs'
)

depends=('boost'
'ros-melodic-camera-calibration-parsers'
'ros-melodic-image-transport'
'ros-melodic-roscpp'
'ros-melodic-roslib'
'ros-melodic-sensor-msgs'
)

conflicts=()
replaces=()

_dir=camera_info_manager
source=()
md5sums=()

prepare() {
    cp -R $startdir/camera_info_manager $srcdir/camera_info_manager
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

