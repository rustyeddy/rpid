from motor import SkidSteer
import paho.mqtt.client as mqtt
from pprint import pprint


def on_connect(client, userdata, flags, rc):
    print("Connected with result " + str(rc))
    client.subscribe("mot")

def on_message(client, userdata, msg):
    car._left_speed(.7)
    car._right_speed(.7)
    print(msg.topic + " " + str(msg.payload))
    print("Hello, cmds")

    msgstr = msg.payload
    
    cmds = msgstr.split(':')
    print("Commands have ... ")
    print(len(cmds))
    pprint(cmds)

    print("0")
    print(cmds[0])
    print("1")
    print(cmds[1])
    if cmds[0] == "mot":
        num = cmds[1]
        lspeed = cmds[2]
        rspeed = cmds[3]

        print("lspeed " + str(lspeed))
        print("rspeed " + str(rspeed))
        car._left_speed(lspeed)
        car._right_speed(rspeed)



if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    car = SkidSteer()
    car.speed = .3

    client.connect("localhost", 1883, 60)
    client.loop_forever()


