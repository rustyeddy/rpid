"""This code started as the Simple test for using adafruit_motorkit then 
hacked a bit to support 'motor groups' or a set of motors that will be set
to the same speed."""
import time
import atexit

from adafruit_motorkit import MotorKit
# motors = MotorKit()

def Stop():
   motors = MotorKit()
   motors.motor1.throttle = 0
   motors.motor2.throttle = 0
   motors.motor3.throttle = 0
   motors.motor4.throttle = 0
   
class SkidSteer:
    """This class assumes two powered motors (or motor groups) that oppose
    each other to form a right and left side of the vehical, which
    also presumes a front and rear.

    """
    def __init__(self):
        self._left_trim = 0
        self._right_trim = 0
        self._stop_at_exit = True
        self._motors = MotorKit()

        # 2wd
        # self.left       = [ kit.motor1 ]
        # self.right      = [ kit.motor2 ]
        #
        # 4wd 
        self.leftMotors  = [ self._motors.motor1, self._motors.motor3 ]
        self.rightMotors = [ self._motors.motor2, self._motors.motor4 ]
        self.speed = 0

        if self._stop_at_exit:
            atexit.register(Stop)


    def _left_speed(self, speed):
        """Set the speed of the left motor, taking into account its trim
        offset.  _left_speed and _right_speed have been converted into
        groups such that each motor in a group will have the motor set
        to the same speed.  This applies to 4wd, 6wd, etc. as well as
        tracked vehicals with more than one motor like a tank.

        """
        assert -1 <= speed <= 1, 'Speed must be a value between -1 to 1 inclusive!'
        speed += self._left_trim
        speed = max(-1, min(1, speed))  # Constrain speed to 0-255 after trimming.

        for m in self.leftMotors:
            m.throttle = speed

    def _right_speed(self, speed):
        """Set the speed of the right motor, taking into account its trim
        offset.

        """
        assert -1 <= speed <= 1, 'Speed must be a value between -1 to 1 inclusive!'
        speed += self._right_trim
        speed = max(-1, min(1, speed))  # Constrain speed to 0-255 after trimming.

        for m in self.rightMotors:
            m.throttle = speed
        self.right_speed = speed  # record for posterity just in case we get confused

    def stop(self):
        """Stop all movement."""
        self._motors.motor1.throttle = 0
        self._motors.motor2.throttle = 0
        self._motors.motor3.throttle = 0
        self._motors.motor4.throttle = 0

    def forward(self, seconds=None):
        """Move forward at the specified speed (0-255).  Will start moving
        forward and return unless a seconds value is specified, in which
        case the robot will move forward for that amount of time and then stop.
        """
        # Set motor speed and move both forward.
        self._left_speed(self.speed)
        self._right_speed(self.speed)
        # If an amount of time is specified, move for that time and then stop.
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def steer(self, direction):
        # Move forward at the specified speed (0- 1).  Direction is +- 1.
        # Full left is -1, Full right is +1
        # calibrate so total motor output never goes above 1
        speed = self.speed
        if (speed + direction/2) > 1:
            speed = speed - direction/2
            
        left = speed + direction/2
        right = speed - direction/2
        self._left_speed(left)
        self._right_speed(right)

    def backward(self, seconds=None):
        """Move backward at the specified speed (0-255).  Will start moving
        backward and return unless a seconds value is specified, in which
        case the robot will move backward for that amount of time and then stop.
        """
        # Set motor speed and move both backward.
        self._left_speed(-1*self.speed)
        self._right_speed(-1*self.speed)
        # If an amount of time is specified, move for that time and then stop.
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def right(self, seconds=None):
        """Spin to the right at the specified speed.  Will start spinning and
        return unless a seconds value is specified, in which case the robot will
        spin for that amount of time and then stop.
        """
        # Set motor speed and move both forward.
        self._left_speed(self.speed)
        self._right_speed(0)
        # If an amount of time is specified, move for that time and then stop.
        if seconds is not None:
            time.sleep(seconds)
            self.stop()
 
    def left(self, seconds=None):
        """Spin to the left at the specified speed.  Will start spinning and
        return unless a seconds value is specified, in which case the robot will
        spin for that amount of time and then stop.
        """
        # Set motor speed and move both forward.
        self._left_speed(0)
        self._right_speed(self.speed)
        # If an amount of time is specified, move for that time and then stop.
        if seconds is not None:
            time.sleep(seconds)
            self.stop()



