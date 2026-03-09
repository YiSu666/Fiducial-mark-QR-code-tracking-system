# Fiducial-mark-QR-code-tracking-system

Notice:

The latest raspberry pi camera module V3 does not working well with raspberry pi 4, with latest system , all camera libraries has changed to libcamera for C++ or picamera2 for python. There's lots of bugs when adapting libcamera with OpenCV in C++, OpenCV will never receive any frames from camera when using Videocapture(0), because Videocapture(0) does not support libcamera in C++,  there's no solution for raspberry pi 64 bit OS, libcamera may works for OpenCV in bullseye OS. To solve this problem, I wrote a python script which use picamera2 to read the frame from camera and streaming the frame through ZMQ, in OpenCV set up ZMQ receiver port to receive the frame from camera and proceed further.

=================================================================================================================================

To install all libraries and doc required on your Linux system for this project:

sudo apt-get install git libjpeg-dev libpng-dev libtiff-dev libzbar-dev autoconf automake libtool pkg-config

git clone https://github.com/mchehab/zbar.git

cd zbar
autoreconf -vfi
./configure
make

sudo make install

sudo ldconfig
zbarimg --version

wget https://github.com/Qengineering/Install-OpenCV-Raspberry-Pi-32-bits/raw/main/OpenCV-4-9-0.sh

sudo chmod 755 ./OpenCV-4-9-0.sh
./OpenCV-4-9-0.sh
