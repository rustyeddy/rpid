from adafruit_motorkit import MotorKit
import time

def skid_set_throttle(vehicle, left, right):
    assert -1.0 <= float(left) <= 1.0
    assert -1.0 <= float(right) <= 1.0
    vehicle.motor1.throttle = left
    vehicle.motor2.throttle = right

if __name__ == "__main__":

    skid = MotorKit()
    while True:

        # wait for stdin to tell us what to do
        instr = input("devctl~> ")
        if instr == "":
            continue

        # the command looks like the '<r>/<l>' where <r> and <l> are floating
        # point numbers between -1.0 and 1.0 inclusive. r stands for right, 
        # l stands for left
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

        print("Fixin to set throttle " + str(left) + " " + str(right))

        skid_set_throttle(skid, left, right)
