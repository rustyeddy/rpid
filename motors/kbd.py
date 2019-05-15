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
    if cmd == "h":
        car.left(speed)
    elif cmd == "j":
        car.forward(speed)
    elif cmd == "k":
        car.backward(speed)
    elif cmd == "l":
        car.right(speed)
    elif cmd == "f":
        if car._left_throttle < 1.0:
            car._left_throttle += 0.1
            car._right_throttle = car._left_throttle
            
    elif cmd == "s":
        if car._left_throttle > 0.0:
            car._left_throttle -= 0.1
            car._right_throttle = car._left_throttle

    elif cmd == "q":
        print("Goodbye ...")
        sys.exit(0)

    else:
        print("Do not know what to do with cmd " + cmd)

    print("left " + str(car._left_throttle) + " right " + str(car._right_throttle))
    return

if __name__ == "__main__":

    # create an instance of our skidder
    skidder = SkidSteer("skid", 2)
    
    # Start looping waiting for and reading commands, the 
    # cmd we have is totally independant of the car the 
    # command will be applied to.
    while True:
        print("prompt~> ")
        cmd = get_cmd()
        if cmd == "":
            continue 

        print("We are telling our car to " + cmd)
        do_cmd(skidder, cmd)

