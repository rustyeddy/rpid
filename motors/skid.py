from adafruit_motorkit import MotorKit
import time

skid = MotorKit()

def skid_set_throttle(vehicle, left, right):
    assert -1.0 <= float(left) <= 1.0
    assert -1.0 <= float(right) <= 1.0
    vehicle.motor1.throttle = left
    vehicle.motor2.throttle = right

while True:
    instr = input("devctl~> ")
    if instr == "":
        continue

    vals = instr.split("/")
    if len(vals) != 2:
        print("ERROR expected two values")
        continue

    left = float(vals[0])
    right = float(vals[1])
    assert -1.0 <= right <= 1.0
    assert -1.0 <= left <= 1.0
    print("Fixin to set throttle " + str(left) + " " + str(right))

    skid_set_throttle(skid, left, right)
