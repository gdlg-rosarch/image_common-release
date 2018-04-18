# Script generated with Bloom
pkgdesc="ROS - image_transport should always be used to subscribe to and publish images. It provides transparent support for transporting images in low-bandwidth compressed formats. Examples (provided by separate plugin packages) include JPEG/PNG compression and Theora streaming video."
url='http://ros.org/wiki/image_transport'

pkgname='ros-lunar-image-transport'
pkgver='1.11.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-message-filters'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-roslib'
'ros-lunar-sensor-msgs'
)

depends=('ros-lunar-message-filters'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-roslib'
'ros-lunar-sensor-msgs'
)

conflicts=()
replaces=()

_dir=image_transport
source=()
md5sums=()

prepare() {
    cp -R $startdir/image_transport $srcdir/image_transport
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

