from skid import SkidSteer

import sys, tty, termios

def read_stdin():
    ## Can we add an mqtt task here also?
    readline = sys.stdin.readline()
    while readline:
        yield readline
        readline = sys.stdin.readline()


def get_cmd():
    """Get a single character from stdin, Unix version"""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())          # Raw read
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def do_cmd(car, cmd):
    speed = car._left_throttle
    left = 0
    right = 0

    if cmd == "h":
        right = speed 
        left = speed * -1
    elif cmd == "j":
        left = speed
        right = speed
    elif cmd == "k":
        left = speed * -1
        right = speed * -1
    elif cmd == "l":
        left = speed
        right = speed * -1

    elif cmd == "f":
        if speed < 1.0:
            speed = speed + .1
    elif cmd == "s":
        if speed > 0:
            speed = speed - .1

    elif cmd == "q":
        print("Goodbye ...")
        sys.exit(0)

    else:
        print("Do not know what to do with cmd " + cmd)
        return

    print("left " + left + " right " + right)
    kit.motor1.throttle = left
    kit.motor2.throttle = right
    return

if __name__ == "__main__":

    # create an instance of our skidder
    while True:
        print("prompt~> ")
        cmd = get_cmd()
        if cmd == "":
            continue 

        print("We are telling our car to " + cmd)
        do_cmd(skidder, cmd)

