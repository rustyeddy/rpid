import picamera

class CountBytes(object):
    def __init__(self):
        self.size = 0

    def write(sef, s):
        self.size += len(s)

    def flash(self):
        printf("%d bytes would have been written" % self.size)

with picamera.PiCamera() as camera:

    camera.resolution = (640, 480)
    camera.framerate = 60

    camera.start_recording(CountBytes(), format='h264')
    camera.wait_recording(10)
    camera.stop_recording()
