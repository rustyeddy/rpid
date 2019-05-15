##
## This program runs on a Raspberry Pi with an Adafruit Motorshield,
## it can be used to control a vehicle employing skid steering.  The
## fundamental constraints for skid steering are
##
## 1. Wheels belong to either the left or right wheel group.
## 2. All wheels in a wheel group MUST rotate at the same *speed*
## 3. Velocity is directly controlled by the speed to the two motors
## 4. Turn is performed by one side turning faster than the other side
## 
## With that, the skid API will expose a very simple fundamental API,
## left_throttle and right_throttle.  I will add stop and coast for convienince.
##
## If we are running on a Raspberry Pi with the Adafruit Motorkit
## installed we will use that to drive the motors.  If the Adafruit
## Motorkit is NOT installed, we will use the local copy of the
## fake_motorkit.
##
## This will keep the program from puking, it will also allow us to
## run and test (to a great extent) this code on pretty much any
## computer with python.  Of course no motors will turn, so you will
## just have to assume the Motor driver does it's job and control the
## motors.
##
import atexit
from pprint import pprint

try:
    from adafruit_motorkit import MotorKit
except:
    from fake_motorkit import MotorKit

def Stop():
    """Stop all motors incase we our motor kit has crashed and the program
    has exited.  In our case fake_motorkit, we do nothing"""
    skid = MotorKit()
    skid.motor1.threshold = 0.0
    skid.motor2.threshold = 0.0
    skid.motor3.threshold = 0.0
    skid.motor4.threshold = 0.0
    
class SkidSteer:
    """This class assumes two powered motors (or motor groups) that oppose
    each other to form a right and left side of the vehical, which
    also presumes a front and rear.
    """
    def __init__(self, name="skid", wheels=2):
        self._name = name
        self._wheel_count = wheels
        self._left_trim = 0
        self._right_trim = 0
        self._stop_at_exit = True

        self._motors = MotorKit()
        self._left_throttle = 0
        self._right_throttle = 0
        if self._wheel_count == 2:
            self.left_motors      = [ self._motors.motor1 ]
            self.right_motors     = [ self._motors.motor2 ]
        elif self._wheel_count == 4:
            self.left_motors       = [ self._motors.motor1, self._motors.motor3 ]
            self.right_motors      = [ self._motors.motor2, self._motors.motor4 ]
            
        if self._stop_at_exit:
            atexit.register(Stop)

    @property        
    def throttle(self, throttle):
        self._left_throttle = throttle
        self._right_throttle = throttle
        
    def left_throttle(self, throttle):
        """Set the throttle of the left motor, taking into account its trim
        offset.  _left_throttle and _right_throttle have been converted into
        groups such that each motor in a group will have the motor set
        to the same throttle.  This applies to 4wd, 6wd, etc. as well as
        tracked vehicals with more than one motor like a tank.
        """
        assert -1.0 <= throttle <= 1.0, 'Throttle must be a value between -1 to 1 inclusive!'
        throttle += self._left_trim
        throttle = max(-1, min(1, throttle))

        for m in self.left_motors:
            m.throttle(throttle)
            
    def right_throttle(self, throttle):
        """Set the throttle of the right motor, taking into account its trim
        offset.
        """
        assert -1.0 <= throttle <= 1.0, 'Throttle must be a value between -1 to 1 inclusive!'
        throttle += self._right_trim
        throttle = max(-1, min(1, throttle))

        for m in self.right_motors:
            pprint(throttle)
            m.throttle(throttle)

    def forward(self, throttle):
        self.right(throttle)
        self.left(throttle)
        return throttle

    def backward(self, throttle):
        throttle *= -1.0
        self.right_throttle(throttle)
        self.left_throttle(throttle)
        return throttle

    def right(self, throttle):
        self.left_throttle(throttle)
        self.right_throttle(throttle * -1.0)
        return throttle

    def left(self, throttle):
        self.left_throttle(throttle * -1.0)
        self.right_throttle(throttle)
        return throttle

    def string(self):
        return "skidder: " + self._name
    
