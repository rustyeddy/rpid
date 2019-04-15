
"""Simple test for using adafruit_motorkit with a DC motor"""
import time
from adafruit_motorkit import MotorKit

kit = MotorKit()
m1 = kit.motor1
m2 = kit.motor2
m3 = kit.motor3
m4 = kit.motor4

# kit.motor1.throttle = 1.0
# time.sleep(0.5)
# kit.motor1.throttle = 0

m1.throttle = None
m2.throttle = None
m3.throttle = None
m4.throttle = None

def forward(th):
    """Forward throttle is throttle"""
    m1.throttle = None
    m2.throttle = None
    m3.throttle = None
    m4.throttle = None
