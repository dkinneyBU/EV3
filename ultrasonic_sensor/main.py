#!/usr/bin/env pybricks-micropython
 
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
 
brick.sound.beep() # Play a sound.

# Initialize sensors used to detect obstacles as the robot drives around.
obstacle_sensor = InfraredSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S3)

# Initialize left and right motors of the drive base with default settings on Port B and Port C.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

wheel_diameter = 43 # The wheel diameter of the Robot Educator in millimeters.
axle_track = 114 # The axle track is the distance between the centers of each of the wheels.

# The DriveBase is composed of 2 motors with a wheel on each. The wheel_diameter and axle_track
#  values are used to make the motors move at the correct speed when you give a motor command.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Make the robot drive forward until it detects an obstacle. Then back up and turn around.
while True:
    robot.drive(200, 0) # Begin driving forward at 200 millimeters per second.
    # Wait until an obstacle is detected. This is done by repeatedly doing nothing (waiting for
    #  10 milliseconds) while the measured distance is still greater than 30 mm.
    while obstacle_sensor.distance() > 30 and touch_sensor.pressed() == False:
        print("Distance     : {0}".format(obstacle_sensor.distance()))
        print("Color        : {0}".format(color_sensor.color()))
        print("Ambient      : {0}".format(color_sensor.ambient()))
        print("Reflection   : {0}".format(color_sensor.reflection()))
        wait(10)
    # Drive backward at 100 millimeters per second. Keep going for 2 seconds.
    robot.drive_time(-100, 0, 2000)
    # Turn around at 60 degrees/second around the midpoint between the wheels for 2 seconds.
    robot.drive_time(0, 60, 2000)   