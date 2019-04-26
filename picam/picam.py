from time import sleep
from picamera import PiCamera

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

def sequence(camera):
    """Take a sequence of images and save in /tmp/image0x.jpg"""
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(['/tmp/image%02d.jpg' % i for i in range(10)])


if __name__ == "__main__":

    fname="/tmp/snap.jpg"
    delay=2

    print("Create and init the camera")
    camera = init_camera()

    print("  take a snapshot after 2 sec delay then save in /tmp/snap.jpg")
    snap(camera, fname, delay)

    print("  take a sequence and save the sequence to /tmp/image0x.jpg")
    sequence(camera)

    print("done.")
