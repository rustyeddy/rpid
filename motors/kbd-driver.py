from motor import SkidSteer

import sys, tty, termios

def read_stdin():
    ## Can we add an mqtt task here also?
    readline = sys.stdin.readline()
    while readline:
        yield readline
        readline = sys.stdin.readline()

def do_cmd(car, cmd):
    speed = car.speed
    if cmd == "h":
        car.left()
    elif cmd == "j":
        car.forward()
    elif cmd == "k":
        car.backward()
    elif cmd == "l":
        car.right()
    elif cmd == "f":
        if car.speed < 10:
            car.speed++
    elif cmd == "s":
        if car.speed > 0:
            car.speed--
    elif cmd == "q":
        print("Trying to exit")
        sys.exit(0)
    else:
        print("Do not know what to do with cmd " + cmd)

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
    

if __name__ == "__main__":

    car = SkidSteer()
    car.speed = .4
    
    # Start looping waiting for and reading commands, the 
    # cmd we have is totally independant of the car the 
    # command will be applied to.
    while True:
        print("prompt~> ")
        cmd = get_cmd()
        print("We are telling our car to " + cmd)
        do_cmd(car, cmd)


