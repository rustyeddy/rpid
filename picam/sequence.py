import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 30

    camera.start_preview()
    time.sleep(2)

    camera.capture_sequence([
        'i1.jpg',
        'i2.jpg',
        'i3.jpg',
        'i4.jpg',
        'i5.jpg',
        'i6.jpg',
    ], use_video_port=True)
