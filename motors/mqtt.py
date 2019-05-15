from motors import SkidSteer

def read_mqtt():
    message = mqtt.read_message("mot")

    cmds = "".split(":")
    if len(cmds) < 1:
        next
    if cmds[0] == "mot":
        print("We have a joystick command!")
    else:
        print("Unkown command " + cmds[0])

    lspeed = cmds[2]
    rspeed = cmds[3]

    # Parse joystick the send a command to the car controller
    m1.left_speed(lspeed)
    m2.right_speed(rspeed)
