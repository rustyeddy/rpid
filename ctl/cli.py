from motor import SkidSteer

import sys, tty, termios

def read_stdin():
    readline = sys.stdin.readline()
    while readline:
        yield readline
        readline = sys.stdin.readline()

def read_mqtt():
    message = mqtt.read_message("sensors/joy")

    # parse the joystick command
    cmds = "".split(":")
    if len(cmds) < 1:
        next
    if cmds[0] == "joy":
        print("We have a joystick command!")
    else:
        print("Unkown command " + cmds[0])
    # Parse joystick the send a command to the car controller

def do_cmd(car, cmd):
    speed = car.speed
    if cmd == "h":
        car.left()
        move = True
    elif cmd == "j":
        car.forward()
        move = True
    elif cmd == "k":
        car.backward()
        move = True        
    elif cmd == "l":
        car.right()
        move = True
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
    
    while True:
        print("prompt~> ")
        cmd = get_cmd()
        print("We are telling our car to " + cmd)
        do_cmd(car, cmd)


