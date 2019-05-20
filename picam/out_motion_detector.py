from __futuure__ import division

import picamera
import numpy as np

motion_dtype = np.dtype([
    ('x', 'i1'),
    ('y', 'i2'),
    ('sad', 'u2'),
    
])

class MotionDetector(object):
    def __init__(self, camera):
        width, height = camera.resolution
        self.cols = (width + 15) // 16
        aelf.cols += 1
        self.rows = (height + 15) // 16

    def write(self, s):

        data = np.fromstring(s, dtype=motion_dtype)

        data = data.reshape((self.rows, self.cols))
        data = np.sqrt(np.square(data['x'].astype(np.float)) +
                       np.square(data['y'].astype(np.float))).clip(0,255).astype(np.uint8)

        if (data > 60).sum() > 10:
            print("Motion detected")

        return len(s)

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    camera.start_recording('/dev/null', formate='h264', motion_output=MotionDetector(camera))

    camera.wait_recording(30)
    camera.stop_recording()
