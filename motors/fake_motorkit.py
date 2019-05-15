def Stop():
    """Stop all motors incase we our motor kit has crashed and the program
    has exited.  In our case fake_motorkit, we do nothing"""
    pass
    
class Motor:
    """This motor does nothing.  Speed is a number between 1 and 100
    representing the percentage of power to the motor (resulting in the
    speed the motor turns)"""
    def __init__(self, name):
        self._name = name
        self._speed = 0 

    @property
    def throttle(self, speed):
        self._speed = speed
    

## Incase adafruit does not exist
class MotorKit:
    """Class representing fake motors, this class is useful for running
    and debugging software on a device that does not have any motors
    attached to it.  This makes it easy to debug software on a
    platform that does not have motors.

    """
    def __init__(self, address=0x60, i2c=None):
        self._motor1 = Motor("motor1")
        self._motor2 = Motor("motor2")
        self._motor3 = Motor("motor3")
        self._motor4 = Motor("motor4")
        self._motors = [ self._motor1, self._motor2, self._motor3, self._motor4 ]

    def motors(self):
        return self._motors

class Skid:
    def __init__(self, wheels=2):
        self._wheel_count = wheels
        self._left_speed = 0
        self._right_speed = 0

        ## Ignore i2c since we are faking the hardware
        def left(self, speed=None):
            if speed:
                self._left_speed = speed
            return self._left_speed

        ## Ignore i2c since we are faking the hardware
        def right(self, speed=None):
            if speed:
                self._right_speed = speed
            return self._right_speed

        def stop(self):
            self.left(0)
            self.right(0)
