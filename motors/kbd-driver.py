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
    elif cmd == "+":
        car.speed = speed + 10
    elif cmd == "-":
        car.speed = speed - 10;
    elif cmd == "0":
        car.stop()
    elif cmd == "2":
        car.speed = .2
    elif cmd == "3":
        car.speed = .3
    elif cmd == "4":
        car.speed = .4
    elif cmd == "5":
        car.speed = .5
    elif cmd == "6":
        car.speed = .7
    elif cmd == "7":
        car.speed = .8
    elif cmd == "8":
        car.speed = .9
    elif cmd == "9":
        car.speed = 1
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


