import cv2
import zmq
import numpy as np
from picamera2 import Picamera2, Preview
import time

# Initialize the camera
picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (800, 480)})
picam2.configure(config)
picam2.set_controls({"AfMode":2,"AfTrigger":0})  # Enable autofocus
picam2.start()

# Setup ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

print("Camera and ZeroMQ setup complete. Starting capture...")

try:
    while True:
        frame = picam2.capture_array()
        if frame is None:
            print("Failed to capture frame")
            continue
        
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            print("Failed to encode frame")
            continue

        socket.send(buffer)
        print("Frame sent")

        # To avoid overwhelming the receiver, add a small delay
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Streaming stopped.")
finally:
    picam2.stop()
    socket.close()
    context.term()
