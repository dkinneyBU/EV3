#!/usr/bin/env python3
from sys import stderr
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import Sensor
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.display import Display


lcd = Display()

# Connect Pixy camera
pixy = Sensor()

# Connect TouchSensor
ts = TouchSensor(address = INPUT_1)

# Set mode
pixy.mode = 'ALL'

while not ts.value():
  lcd.clear()
  if pixy.value(0) != 0:  # Object with SIG1 detected
    x = pixy.value(1) 
    y = pixy.value(2)
    w = pixy.value(3)
    h = pixy.value(4)
    dx = int(w/2)       # Half of the width of the rectangle
    dy = int(h/2)       # Half of the height of the rectangle
    xb = x + int(w/2)   # X-coordinate of bottom-right corner
    yb = y - int(h/2)   # Y-coordinate of the bottom-right corner
    lcd.draw.rectangle((dx,dy,xb,yb), fill='black')
    lcd.update()
    for i in range(0,4):
      print(pixy.value(i),file=stderr)