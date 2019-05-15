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
## left_speed and right_speed.  I will add stop and coast for convienince.
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
try:
    from adafruit_motorkit import MotorKit
except:
    from fake_motorkit import MotorKit

class SkidSteer:
   """This class assumes two powered motors (or motor groups) that oppose
    each other to form a right and left side of the vehical, which
    also presumes a front and rear.

    """
    def __init__(self, wheels=2):
       self._wheel_count = wheels
       self._left_trim = 0
       self._right_trim = 0
       self._stop_at_exit = True
       self._motors = MotorKit()

       ## pseudo private
       self._left_speed = 0
       self._right_speed = 0

       if self._wheel_count == 2:
          self.left_motors      = [ self._motors.motor1 ]
          self.right_motors     = [ self._motors.motor2 ]
       else if self._wheel_count == 4:
          self.left_motors       = [ self._motors.motor1 self._motors.motor3 ]
          self.right_motors      = [ self._motors.motor2 self._motors.motor4 ]

       if self._stop_at_exit:
          atexit.register(Stop)
       
    def left_speed(self, speed):
        """Set the speed of the left motor, taking into account its trim
        offset.  _left_speed and _right_speed have been converted into
        groups such that each motor in a group will have the motor set
        to the same speed.  This applies to 4wd, 6wd, etc. as well as
        tracked vehicals with more than one motor like a tank.
        """
        assert -1 <= speed <= 1, 'Speed must be a value between -1 to 1 inclusive!'
        speed += self._left_trim
        speed = max(-1, min(1, speed))  # Constrain speed -1 <= x <= 1

        for m in self.left_motors:
            m.throttle = speed
            m._left_speed = speed
        
    def right_speed(self, speed):
        """Set the speed of the right motor, taking into account its trim
        offset.
        """
        assert -1 <= speed <= 1, 'Speed must be a value between -1 to 1 inclusive!'
        speed += self._right_trim
        speed = max(-1, min(1, speed))  # Constrain speed to 0-255 after trimming.

        for m in self.right_motors:
           m._right_speed = speed
           m.throttle = speed

    def forward(self, speed):
        self.right_speed(speed)
        self.left_speed(speed)
        return speed

    def backward(self, speed):
        speed *= -1
        self.right_speed(speed)
        self.left_speed(speed)
        return speed

    def right(self, speed):
        self.left_speed(speed)
        self.right_speed(speed * -1)
        return speed

    def left(self, speed):
        self.left_speed(speed * -1)
        self.right_speed(speed)
        return speed

