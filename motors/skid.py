try:
    from adafruit_motorkit import MotorKit
except:
    from fake_motorkit import MotorKit

import time


# MotorKit() provides us with access to the Adafruit circuit_python
# emulation library (I think I have that right), the motors object has
# fields for the 4 DC motors and 2 stepper motors (depending on the
# apps config). We make a global (singleton for you OO types), since
# there is only one set of motors controlled by this controller,
# second we want access in case our Object crashs and everything goes
# to hell in a hand basket, we can still shutdown the motors with
# atexit. 
motors = MotorKit()

class Skidder:
    """Skidder is a hyper simple SkidSterring class for the Adafruit
    MotorShield, it is really a simple copy of one of their examples
    that I sprinkled with some app dust"""

    def __init__(self):
        """We will remember the r/l throttle values, we will use them
        later to implement a dampening algorightm.  At the start of
        the program the motors will get recieve no load."""
        self._left_throttle = 0.0
        self._right_throttle = 0.0
        motors.motor1.throttle = 0
        motors.motor2.throttle = 0

    def set_throttle(self, left, right):
        """Set the percent of load that will be provided to the motor,
        which will intern determine the power to turn the axle.  But
        we have no idea what this will translate in terms of actual
        velocity with out any external feedback, so we just set the
        throttle and let the upper layers worry about setting the
        correct velocity and acceleration"""
        assert -1.0 <= l <= 1.0
        assert -1.0 <= r <= 1.0

        ## TODO ~ put some dampening in place if the new throttle
        ## values represent a large delta to avoid unneeded damage to
        ## the motors or chassis.
        vehicle.motor1.throttle = l
        vehicle.motor2.throttle = r
        self._left_throttle
        self._right_throttle

    def stop(self):
        """Come to an immediate halt"""
        vehicle.motor1.throttle = 0
        vehicle.motor2.throttle = 0
        
    def read_msg(self, msgstr):
        """We will read the incoming message, we only have one
        message, to set the throttle of the right and left motors.
        Hence we know it will have float/float or it will be an error.
        It is valid to represent floats as integers, i.e. 1 is a valid
        float. 

        """
        vals = instr.split("/")
        if len(vals) != 2:
            print("ERROR expected two values")
            continue

        # convert the parameter strings to floats
        left = float(vals[0])
        right = float(vals[1])

        # make sure we don't dive our motors something stupid
        assert -1.0 <= right <= 1.0
        assert -1.0 <= left <= 1.0
        self.set_throttle(left, right)
        

if __name__ == "__main__":

    skid = Skidder()
    while True:
        # wait for stdin to tell us what to do
        instr = input("devctl~> ")
        if instr == "":
            continue

        skid.read_msg(instr)
