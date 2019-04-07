from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2

size = (640, 480)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]


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

def frame_generator():
    """This is our main video feed"""
    #camera = pi_camera_stream.setup_camera()
    camera = setup_camera()

    time.sleep(0.1)

    for frame in start_stream(camera):
        #encoded_bytes = pi_camera_stream.get_encoded_bytes_for_frame(frame)
        encoded_bytes = get_encoded_bytes_for_frame(frame)
        # need to turn this into multi part data
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + encoded_bytes + b'\r\n')
