# Fiducial-mark-QR-code-tracking-system

A QR code-based tracking system. The QR code is affixed as a fiducial marker, enabling real-time tracking of position, orientation, and movement.

Detection Process: 

Using OpenCV, the system applies edge detection (Sobel algorithm) and contour finding to identify squares. It scans for contours matching the ratio, confirms the right-triangle formation, and locks the QR code. Zbar library simulates laser scanning for efficient decoding, focusing on light-dark transitions (binary data).
![QRdetect1](https://github.com/user-attachments/assets/2e01e75f-c755-45aa-9554-6661209296cc)

This system improves:
=
Applies morphological dilation (e.g., rate 0.1) to enlarge black pixels, smoothing boundaries and reducing noise/blur at distances >30 cm. This makes edges more readable without losing features.

Extends tracking range from ~30 cm (without) to 50–80 cm. However, it slightly reduces accuracy at close range (<25 cm) by shrinking measured area, causing 0.1–0.35 cm underestimation. Optimal for low-resolution webcams (e.g., 2 MP, 30 FPS).

Optical Flow for Motion Handling (Lucas-Kanade Method): Handles motion blur by estimating pixel displacements between consecutive frames. Assumes small, linear movements; builds a pyramid of frame resolutions (Gaussian downsampling) to compute gradients. Solves linear equations for pixel shifts, restoring the QR code.
![屏幕截图 2026-03-10 095445](https://github.com/user-attachments/assets/4b2e7e75-cbf8-4c2f-8d02-ea94d3528637)


Convolutional Neural Network (CNN): Detector CNN: Identifies QR codes by feature extraction (edges, colors in early layers; shapes/objects in later layers). Compares input to trained weight matrix (shorter distance = match).
![ocluded test](https://github.com/user-attachments/assets/63c7fe29-9734-4a70-bc30-9659003fdf8c)

![low lighting test](https://github.com/user-attachments/assets/d4742565-002d-4499-a84d-382935ba6e22)


====================================================================================================================

To install all libraries and doc required on your Linux system for this project:
=
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

Notice:
=
The latest raspberry pi camera module V3 does not working well with raspberry pi 4, with latest system , all camera libraries has changed to libcamera for C++ or picamera2 for python. There's lots of bugs when adapting libcamera with OpenCV in C++, OpenCV will never receive any frames from camera when using Videocapture(0), because Videocapture(0) does not support libcamera in C++,  there's no solution for raspberry pi 64 bit OS, libcamera may works for OpenCV in bullseye OS. To solve this problem, I wrote a python script which use picamera2 to read the frame from camera and streaming the frame through ZMQ, in OpenCV set up ZMQ receiver port to receive the frame from camera and proceed further.

=================================================================================================================================


