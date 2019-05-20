from picamera import PiCamera
from time import sleep

camera = PiCamera()

def preview(a=255, d=10):
    camera.start_preview(alpha=a)
    sleep()
    camera.stop_preview()

def snaps():
    for i in range(5):
        sleep(5)
        camera.capture("/home/pi/Desktop/image%s.jpg" % i)
    camera.stop_preview()


camera.resolution = (2592, 1944)
camera.framerate = 15

camera.start_preview()
camera.annotate_text = "Hello world"
camera.brightness = 80
# camera.start_recording("/home/pi/video.h264")
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
# camera.stop_recording()
camera.stop_preview()

