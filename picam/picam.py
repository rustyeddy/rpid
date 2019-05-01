from time import sleep
from picamera import PiCamera
from fractions import Fraction

resolution_large = (1024, 768)
resolution_small = (320, 240)

"""
See Capturing Consistent images in the PiCamera documents

According to PiCamera documentation

# camera.shutter_speed

Aa a rule of thumb, reasonable values are

- daytime: 100 - 200
- night:   400 - 800

# camera.exposure_speed

Can be queried to determine a reasonable shutter_speed value. 

# camera.iso

# camera.analog_gain
# camera.digital_gain
# camera.exposure_mode
# camera.awb_mode
# camera.awb_gains

"""

def init_camera():
    camera = PiCamera(resolution=resolution_large, framerate=30)
    camera.resolution = resolution_large
    camera.iso = 100
    sleep(2)

    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'

    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    return camera

def snap(camera, fname='/tmp/snap.jpg', delay=2):
    """Take a snapshot after delay seconds, then save file to fname"""
    camera.start_preview()
    sleep(delay)
    camera.capture(fname)

def sequence(camera, tmpl="/tmp/image%02d.jpg", count=10):
    """Take a sequence of images and save in /tmp/image0x.jpg"""
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(['/tmp/image%02d.jpg' % i for i in range(10)])

def time_lapse(camera):
    camera.start_preview()
    sleep(2)
    for filename in camera.capture_continuous('/tmp/img{counter:03d}.jpg'):
        print("    caputred %s" % filename)
        sleep(300)

def low_light(camera):
    """Set before take pictures or recording video in low light"""
    camera.framerate=Fraction(1, 6)
    camera.sensor_mode = 3
    camera.shutter_speed = 60000000
    camera.iso = 800

    # Give the camera a nice long time to set gains and measure
    # AWB (AWS could be fixed here instead)
    print("    low light - sleep for 30 seconds ")
    sleep(30)
    camera.exposure_mode = "off"

if __name__ == "__main__":
    fname="/tmp/snap.jpg"
    delay=2

    print("Create and init the camera")
    camera = init_camera()

    print("  take a snapshot after 2 sec delay then save in /tmp/snap.jpg")
    snap(camera, fname, delay)

    print("  take a sequence and save the sequence to /tmp/image0x.jpg")
    sequence(camera, "/tmp/image02d.jpg", 10)

    print("  now set low light before capturing a new image")
    low_light(camera)

    print("  take a snapshot in low light mode, with 6s exposure ")
    snap(camera, "/tmp/low-light.jpg")

    print("  now start the time lapse")
    time_lapse(camera)

    print("done.")
