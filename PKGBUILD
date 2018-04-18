# Script generated with Bloom
pkgdesc="ROS - camera_calibration_parsers contains routines for reading and writing camera calibration parameters."
url='http://ros.org/wiki/camera_calibration_parsers'

pkgname='ros-kinetic-camera-calibration-parsers'
pkgver='1.11.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'pkg-config'
'ros-kinetic-catkin'
'ros-kinetic-rosbash'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-rosunit'
'ros-kinetic-sensor-msgs'
'yaml-cpp'
)

depends=('boost'
'ros-kinetic-roscpp'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-sensor-msgs'
'yaml-cpp'
)

conflicts=()
replaces=()

_dir=camera_calibration_parsers
source=()
md5sums=()

prepare() {
    cp -R $startdir/camera_calibration_parsers $srcdir/camera_calibration_parsers
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

