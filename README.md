# RPID Raspberry Pi Drive Controllor

This piece of software takes motor and driving commands from messages
that arrive either as REST requests or as MQTT messages.

## MQTT Message

Currently the software can only handle _skid steering_.  The MQTT
messages are like this:

> skid:l:r

This writes the message to the _skid_ channel that contains two
integers -i <= 0 <= i where |i| <= 1.0 representing the percentage of
speed the motor will run at, the direction is determined by the +/-.

## REST Request

> PUT /skid/-.85/.85

Will cause the vehicle to turn to the left, effectively spinning on
the Z axis. 
