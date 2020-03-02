#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
# Play a sound.
brick.sound.beep()
# Initialize a motor at port B.
test_motor = Motor(Port.B)
# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
test_motor.run_target(500, 90)
# Play another beep sound.
# This time with a higher pitch (1000 Hz) and longer duration (500 ms).
brick.sound.beep(1000, 500)

# Do something if the left button is pressed
if Button.LEFT in brick.buttons():
    print("The left button is pressed.")
# Wait until any of the buttons are pressed
while not any(brick.buttons()):
    wait(10)
# Wait until all buttons are released
while any(brick.buttons()):
    wait(10)