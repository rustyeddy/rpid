from picamera.array import PiRGBArray
from picamera import PiCamera

from multiprocessing import Process
from multiprocessing import Queue

import numpy as np
import time
import cv2

# import app

size = (640, 480)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

control_queue = Queue()
display_queue = Queue(maxsize=2)
display_template = 'image_server.html'

def setup_camera():
    camera = PiCamera()
    camera.resolution = size
    camera.rotation = 180
    return camera

def start_stream(camera):
    image_storage = PiRGBArray(camera, size=size)

    cam_stream = camera.capture_continuous(image_storage, format="bgr", use_video_port=True)
    for raw_frame in cam_stream:
        yield raw_frame.array
        image_storage.truncate(0)

def get_encoded_bytes_for_frame(frame):
    result, encoded_image = cv2.imencode('.jpg', frame, encode_param)
    return encoded_image.tostring()

"""
def frame_generator1():
    camera = setup_camera()

    time.sleep(0.1)

    for frame in start_stream(camera):
        #encoded_bytes = pi_camera_stream.get_encoded_bytes_for_frame(frame)
        encoded_bytes = get_encoded_bytes_for_frame(frame)
        # need to turn this into multi part data
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + encoded_bytes + b'\r\n')
"""

def frame_generator():
    """This is our NEW main video feed"""
    while True:
        time.sleep(0.02)
        encoded_bytes = display_queue.get()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + encoded_bytes + b'\r\n')

def put_output_image(encoded_bytes):
    """Queue an output image"""
    if display_queue.empty():
        display_queue.put(encoded_bytes)

def get_control_instruction():
    """Get control instructions from Web app if any"""
    if control_queue.empty():
        return None
    else:
        return control_queue.get()


def controlled_image_server_behavior():
    camera = setup_camera()
    time.sleep(0.02)

    for frame in start_stream(camera):
        encoded_bytes = get_encoded_bytes_for_frame(frame)
        put_output_image(encoded_bytes)

        instruction = get_control_instruction()
        if instruction == "exit":
            print("Stopping")
            return

    
