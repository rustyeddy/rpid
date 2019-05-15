class Motor:
    """This motor does nothing.  Speed is a number between 1 and 100
    representing the percentage of power to the motor (resulting in the
    speed the motor turns)"""
    def __init__(self, name):
        self._name = name
        self._throttle = 0

    def throttle(self):
        return self._throttle

    def throttle(self, value):
        self._throttle = value
    

## Incase adafruit does not exist
class MotorKit:
    """Class representing fake motors, this class is useful for running
    and debugging software on a device that does not have any motors
    attached to it.  This makes it easy to debug software on a
    platform that does not have motors.

    """
    def __init__(self, address=0x60, i2c=None):
        self.motor1 = Motor("motor1")
        self.motor2 = Motor("motor2")
        self.motor3 = Motor("motor3")
        self.motor4 = Motor("motor4")
        self.motors = [ self.motor1, self.motor2, self.motor3, self.motor4 ]

    def motors(self):
        return self._motors

class Skid:
    def __init__(self, wheels=2):
        self._wheel_count = wheels
        self._left_throttle = 0.0
        self._right_throttle = 0.0

        ## Ignore i2c since we are faking the hardware
        def left(self, speed=None):
            if speed:
                self._left_throttle = speed
            return self._left_throttle

        ## Ignore i2c since we are faking the hardware
        def right(self, speed=None):
            if speed:
                self._right_throttle = speed
            return self._right_throttle

        def stop(self):
            self.left(0.0)
            self.right(0.0)
