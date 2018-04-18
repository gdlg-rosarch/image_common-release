# Script generated with Bloom
pkgdesc="ROS - polled_camera contains a service and C++ helper classes for implementing a polled camera driver node and requesting images from it. The package is currently for internal use as the API is still under development."
url='http://ros.org/wiki/polled_camera'

pkgname='ros-melodic-polled-camera'
pkgver='1.11.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-catkin'
'ros-melodic-image-transport'
'ros-melodic-message-generation'
'ros-melodic-roscpp'
'ros-melodic-sensor-msgs'
'ros-melodic-std-msgs'
)

depends=('ros-melodic-image-transport'
'ros-melodic-message-runtime'
'ros-melodic-roscpp'
'ros-melodic-sensor-msgs'
'ros-melodic-std-msgs'
)

conflicts=()
replaces=()

_dir=polled_camera
source=()
md5sums=()

prepare() {
    cp -R $startdir/polled_camera $srcdir/polled_camera
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

