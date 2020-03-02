from ev3dev.ev3 import *
pixy = Sensor(address=INPUT_2)
assert pixy.connected, "Error while connecting Pixy camera to port2"
pixy.mode = 'ALL'
