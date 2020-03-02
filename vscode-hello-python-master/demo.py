#!/usr/bin/env python3

import os
from time import sleep
from sys import stderr
from threading import Thread

from ev3dev2.led import Leds
from ev3dev2.display import Display
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor, ColorSensor
from ev3dev2.sensor.lego import Sensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.motor import MediumMotor, LargeMotor, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C

def speak_and_rotate():
    sound = Sound()
    os.system('setfont Lat15-TerminusBold14')
    mL = LargeMotor('outB'); mL.stop_action = 'hold'
    mR = LargeMotor('outC'); mR.stop_action = 'hold'
    print('Hello, my name is EV3D4!')
    str_en = 'Hello, my name is E V 3 D 4!'
    opts = '-a 200 -s 150 -p 70 -v'
    sound.speak(str_en, espeak_opts=opts+'en+f5')
    sleep(2)
    str_en = "Performing perimeter scan"
    sound.speak(str_en, espeak_opts=opts+'en+f5')
    # Sound.speak('Hello, my name is Evie, 3 D 4!').wait()
    mL.run_to_rel_pos(position_sp= 1662, speed_sp = 300)
    mR.run_to_rel_pos(position_sp=-1662, speed_sp = 300)
    #mL.wait_while('running')
    #mR.wait_while('running')
    sleep(1)
    str_en = "At your command Big Daddy"
    sound.speak(str_en, espeak_opts=opts+'en+f5')
    sleep(1)


def leds():
    leds = Leds()
    for i in range(3):
        leds.set_color('LEFT', 'AMBER')
        leds.set_color('RIGHT', 'GREEN')
        sleep(2)
        leds.set_color('LEFT', 'GREEN')
        leds.set_color('RIGHT', 'AMBER')
        sleep(2)


def write_to_lcd():
    os.system('setfont Lat15-TerminusBold14')
    # os.system('setfont Lat15-TerminusBold32x16')  # Try this larger font

    print('EV3 Python rules!')
    print()  # print a blank line

    print('EV3', 'Python rules!')  # comma means continue on same line

    # print() has a parameter 'end' which by
    # default is the new line character:
    print('EV3')    # A new line will be started after this
    print('Python rules!')

    # Here the 'end' parameter's default new line
    # character argument is replaced
    # by an empty string so no new line is begun
    print('EV3', end='')
    print('Python rules!')

    # Here the 'end' parameter's default new line
    # character argument is replaced
    # by a space character so no new line is begun
    print('EV3', end=' ')
    print('Python rules!')

    sleep(15)  # display the text long enough for it to be seen


def write_to_console():
    # To be able to print to the VS Code Output panel, this
    # script must be launched from VS Code, not from Brickman
    cl = ColorSensor()

    while True:
        # print to EV3 LCD screen
        print(cl.ambient_light_intensity) 
        # print to VS Code output panel
        print(cl.ambient_light_intensity, file=stderr) 
        sleep(0.5)


def display_different_fonts():
    lcd = Display()
    sound = Sound()

    def show_for(seconds):
        lcd.update()
        sound.beep()
        sleep(seconds)
        lcd.clear()

    # Try each of these different sets:
    style = 'helvB'
    #style = 'courB'
    #style = 'lutBS'

    y_value = 0
    str1 = ' The quick brown fox jumped'
    str2 = '123456789012345678901234567890'
    for height in [10, 14, 18, 24]:
        text = style+str(height)+str1
        lcd.text_pixels(text, False, 0, y_value, font=style+str(height))
        y_value += height+1   # short for  y_value = y_value+height+1
        lcd.text_pixels(str2, False, 0, y_value, font=style+str(height))
        y_value += height+1
    show_for(6)

    strings = [] # create an empty list
    # Screen width can accommodate 12 fixed
    # width characters with widths 14 or 15
    #               123456789012
    strings.append(style+'24 The')
    strings.append('quick brown ')
    strings.append('fox jumps   ')
    strings.append('over the dog')
    strings.append('123456789012')

    for i in range(len(strings)):
        lcd.text_pixels(strings[i], False, 0, 25*i, font=style+'24')
    show_for(6)


def medium_motor():
    mm = MediumMotor()
    mm.on_for_degrees(10,3)
    sleep(5)


def large_motor():
    lm = LargeMotor()

    '''
    This will run the large motor at 50% of its
    rated maximum speed of 1050 deg/s.
    50% x 1050 = 525 deg/s
    '''
    lm.on_for_seconds(50, seconds=3)
    sleep(1)

    '''
    speed and seconds are both POSITIONAL
    arguments which means
    you don't have to include the parameter names as
    long as you put the arguments in this order 
    (speed then seconds) so this is the same as
    the previous command:
    '''
    lm.on_for_seconds(50, 3)
    sleep(1)

    '''
    This will run at 500 degrees per second (DPS).
    You should be able to hear that the motor runs a
    little slower than before.
    '''
    lm.on_for_seconds(SpeedDPS(500), seconds=3)
    sleep(1)

    # 36000 degrees per minute (DPM) (rarely useful!)
    lm.on_for_seconds(SpeedDPM(36000), seconds=3)
    sleep(1)

    # 2 rotations per second (RPS)
    lm.on_for_seconds(SpeedRPS(2), seconds=3)
    sleep(1)

    # 100 rotations per minute(RPM)
    lm.on_for_seconds(SpeedRPM(100), seconds=3)


def move_steering_by_angle():
    steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    # drive in a turn for 10 rotations of the outer motor
    steer_pair.on_for_rotations(steering=-20, speed=75, rotations=10)
    # on_for_degrees(steering, speed, degrees, brake=True, block=True)


# Move Steering 'forever'
# on(steering, speed)
# Start rotating the motors according to steering and speed forever.
# Stop the motors
# off(brake=True)
# Stop both motors immediately.


def sensors():
    # Connect infrared and touch sensors to any sensor ports
    ir = InfraredSensor() 
    ts = TouchSensor()
    leds = Leds()

    leds.all_off() 
    # stop the LEDs flashing (as well as turn them off)
    # is_pressed and proximity are not functions and do not need parentheses
    while not ts.is_pressed:  # Stop program by pressing the touch sensor button
        if ir.proximity < 40*1.4: # to detect objects closer than about 40cm
            leds.set_color('LEFT',  'RED')
            leds.set_color('RIGHT', 'RED')
        else:
            leds.set_color('LEFT',  'GREEN')
            leds.set_color('RIGHT', 'GREEN')

        sleep (0.01) # Give the CPU a rest


def get_color_intensity():
    cl = ColorSensor() 

    while True:
        print(cl.reflected_light_intensity)
        sleep(1)
        
    # max is about 80 with white paper, 3mm separation 
    # and 5 with black plastic, same separation


def get_rgb():
    cl = ColorSensor() 
    ts = TouchSensor()

    # Stop program by long-pressing touch sensor button
    while not ts.is_pressed:
        # rgb is a tuple containing three integers
        # each 0-255 representing the amount of
        # red, green and blue in the reflected light
        print(cl.rgb)
        red = cl.rgb[0]
        green=cl.rgb[1]
        blue=cl.rgb[2]
        intensity = cl.reflected_light_intensity
        # print("Red: "+str(red)+", Green: "+str(green)+", Blue: "+str(blue)+'\n')
        print('Red: {0}\nGreen: {1}\nBlue: {2}\nIntensity: {3}'.format(str(red), 
            str(green), str(blue), str(intensity)))
        print('Red: {0}\nGreen: {1}\nBlue: {2}\nIntensity: {3}'.format(str(red), 
            str(green), str(blue), str(intensity)), file=stderr)
        # '\n' is the newline character so an extra (blank) line is printed
        sleep(1)


def remote_control_one_button():
    steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    ir = InfraredSensor()
    # Set the remote to channel 1

    def top_left_channel_1_action(state):
        if state: # state is True (pressed) or False
            steer_pair.on(steering=0, speed=40)
        else:
            steer_pair.off()

    def bottom_left_channel_1_action(state):
        if state:
            steer_pair.on(steering=0, speed=-40)
        else:
            steer_pair.off()

    def top_right_channel_1_action(state):
        if state:
            steer_pair.on(steering=100, speed=30)
        else:
            steer_pair.off()

    def bottom_right_channel_1_action(state):
        if state:
            steer_pair.on(steering=-100, speed=30)
        else:
            steer_pair.off()

    # Associate the event handlers with the functions defined above
    ir.on_channel1_top_left = top_left_channel_1_action
    ir.on_channel1_bottom_left = bottom_left_channel_1_action
    ir.on_channel1_top_right = top_right_channel_1_action
    ir.on_channel1_bottom_right = bottom_right_channel_1_action

    while True:
        ir.process()
        sleep(0.01)


def remote_control_two_buttons():
    steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    medium_motor = MediumMotor()
    ir = InfraredSensor()
    # Set the remote to channel 1

    def top_left_channel_1_action(state):
        move()

    def bottom_left_channel_1_action(state):
        move()

    def top_right_channel_1_action(state):
        move()

    def bottom_right_channel_1_action(state):
        move()

    def move():
        buttons = ir.buttons_pressed() # a list
        if len(buttons)==1:
            medium_motor.off()
            if buttons==['top_left']:
                steer_pair.on(steering=0, speed=40)
            elif buttons==['bottom_left']:
                steer_pair.on(steering=0, speed=-40)
            elif buttons==['top_right']:
                steer_pair.on(steering=100, speed=30)
            elif buttons==['bottom_right']:
                steer_pair.on(steering=-100, speed=30)
        elif len(buttons)==2:
            steer_pair.off()
            if buttons==['top_left', 'top_right']:
                medium_motor.on(speed_pct=10)
            elif buttons==['bottom_left', 'bottom_right']:
                medium_motor.on(speed_pct=-10)
        else: # len(buttons)==0
            medium_motor.off()
            steer_pair.off()

    # Associate the event handlers with the functions defined above
    ir.on_channel1_top_left = top_left_channel_1_action
    ir.on_channel1_bottom_left = bottom_left_channel_1_action
    ir.on_channel1_top_right = top_right_channel_1_action
    ir.on_channel1_bottom_right = bottom_right_channel_1_action

    return ir
    # while True:
    #     ir.process()
    #     sleep(0.01)


def distance_to_beacon():
    sound = Sound()
    ir = InfraredSensor()

    while True:
        for i in range(10):
            # try replacing with ir.distance(), ir.heading()
            # or ir.heading_and_distance()
            distance = ir.heading_and_distance()
            if distance==None:
                # distance() returns None if no beacon detected
                print('Beacon off?', end=' ')
                print('Beacon off?', end=' ', file=stderr)
            else:
                # print to EV3 LCD screen
                # print a space instead of starting a new line
                print(distance, end=' ')
                # print to VS Code output panel
                print(distance, end=' ', file=stderr)
                sound.play_tone(1800-10*distance, 0.4)
            sleep(0.5)
        print('') # start new line on EV3 screen
        print('', file=stderr) # start new line in VS Code

def master_function():
    cl = ColorSensor() 
    ts = TouchSensor()
    ir = InfraredSensor()
    sound = Sound()
    steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    medium_motor = MediumMotor()
    pixy = Sensor(address=INPUT_2)
    # assert pixy.connected, "Error while connecting Pixy camera to port 1"
    # pixy.mode = 'SIG1'
    # lcd = Sensor.Screen()
    lcd = Display()

    def top_left_channel_1_action(state):
        move()

    def bottom_left_channel_1_action(state):
        move()

    def top_right_channel_1_action(state):
        move()

    def bottom_right_channel_1_action(state):
        move()

    def move():
        buttons = ir.buttons_pressed() # a list
        if len(buttons)==1:
            medium_motor.off()
            if buttons==['top_left']:
                steer_pair.on(steering=0, speed=40)
            elif buttons==['bottom_left']:
                steer_pair.on(steering=0, speed=-40)
            elif buttons==['top_right']:
                steer_pair.on(steering=100, speed=30)
            elif buttons==['bottom_right']:
                steer_pair.on(steering=-100, speed=30)
        elif len(buttons)==2:
            steer_pair.off()
            if buttons==['top_left', 'top_right']:
                medium_motor.on(speed_pct=10)
            elif buttons==['bottom_left', 'bottom_right']:
                medium_motor.on(speed_pct=-10)
        else: # len(buttons)==0
            medium_motor.off()
            steer_pair.off()

    # Associate the event handlers with the functions defined above
    ir.on_channel1_top_left = top_left_channel_1_action
    ir.on_channel1_bottom_left = bottom_left_channel_1_action
    ir.on_channel1_top_right = top_right_channel_1_action
    ir.on_channel1_bottom_right = bottom_right_channel_1_action

    opts = '-a 200 -s 150 -p 70 -v'
    speech_pause = 0
    while not ts.is_pressed:
        # rgb is a tuple containing three integers
        ir.process()
        red = cl.rgb[0]
        green=cl.rgb[1]
        blue=cl.rgb[2]
        intensity = cl.reflected_light_intensity
        print('{4} Red: {0}\tGreen: {1}\tBlue: {2}\tIntensity: {3}'.format(str(red), 
        str(green), str(blue), str(intensity), speech_pause), file=stderr)
        lcd.clear()
        print(pixy.mode, file=stderr)
        if pixy.value(0) != 0:  # Object with SIG1 detected
            x = pixy.value(1) 
            y = pixy.value(2)
            w = pixy.value(3)
            h = pixy.value(4)
            dx = int(w/2)       # Half of the width of the rectangle
            dy = int(h/2)       # Half of the height of the rectangle
            xb = x + int(w/2)   # X-coordinate of bottom-right corner
            yb = y - int(h/2)   # Y-coordinate of the bottom-right corner
            lcd.draw.rectangle((xa,ya,xb,yb), fill='black')
            lcd.update()
        speech_pause += 1
        if speech_pause == 200:
            # try replacing with ir.distance(), ir.heading()
            # or ir.heading_and_distance()
            distance = ir.heading_and_distance()
            if distance==None:
                # distance() returns None if no beacon detected
                str_en = 'Beacon off?'
            else:
                str_en = 'Beacon heading {0} and distance {1}'.format(
                    distance[0], distance[1])
            sound.speak(str_en, espeak_opts=opts+'en+f5')
            print(str_en, file=stderr)
            speech_pause = 0
    str_en = 'Terminating program'   
    sound.speak(str_en, espeak_opts=opts+'en+f5')



def speech_examples():
    sound = Sound()
    # see http://espeak.sourceforge.net/
    # values -a 200 -s 130 SHOULD BE INCLUDED if specifying any other options
    # a = amplitude (200 max, 100 default), s = speed 80-500, default = 175)
    opts = '-a 200 -s 150 -p 70 -v'
    # str_en = "I think you ought to know, I'm feeling very depressed"
    str_en = "Hello Big Daddy, your wish is my command"
    # Default voice = English, male
    # sound.speak(str_en)
    # English, male1 (lowest male tone)
    # sound.speak(str_en, espeak_opts='-a 200 -s 130 -ven+m1') # long form
    # English, male7 (highest male tone)
    # sound.speak(str_en, espeak_opts=opts+'en+m7') # using my variable 'opts'
    # English, female1 (lowest female tone)
    # sound.speak(str_en, espeak_opts=opts+'en+f1')
    # English, female5 (highest female tone)
    sound.speak(str_en, espeak_opts=opts+'en+f5')
    sleep(5)
    # croak
    # sound.speak(str_en, espeak_opts=opts+'en+croak')
    # whisper
    # sound.speak(str_en, espeak_opts=opts+'en+whisper')
    # en-us = US English
    # sound.speak(str_en, espeak_opts=opts+'en-us')
    # en-rp = Received pronunciation ('BBC English')
    # sound.speak(str_en, espeak_opts=opts+'en-rp')
    # s = 80 is slowest possible speed
    # sound.speak(str_en, espeak_opts='-a 200 -s 80')
    # s = 300 is a high speed
    # sound.speak(str_en, espeak_opts='-a 200 -s 300')
    # French
    str_fr = 'Le chat est sous la chaise! Le singe est sur la branche!'
    # sound.speak(str_fr, espeak_opts=opts+'fr')
    # French, high pitched male
    # sound.speak(str_fr, espeak_opts=opts+'fr+m7')
    # French, rather low pitched female
    # sound.speak(str_fr, espeak_opts=opts+'fr+f2')
    # See http://espeak.sourceforge.net/languages.html
    # for other languages


def sounds_examples():
    sound = Sound()
    # play a standard beep
    sound.beep()
    sleep(2) # pause for 2 seconds
    # Play a SINGLE 2000 Hz tone for 1.5 seconds
    sound.play_tone(2000, 1.5)
    sleep(2)
    # Play a SEQUENCE of tones
    sound.tone([(200, 2000, 400),(800, 1800, 2000)])

    sleep(2)

    # Play a 500 Hz tone for 1 second and then wait 0.4 seconds
    # before playing the next tone 
    # Play the tone three times
    sound.tone([(500, 1000, 400)] * 3)

    sleep(2)

    #text to speech
    sound.speak('Hello, my name is E V 3!')


def mutlithreading():
    """
    In the first example below a thread called twenty_tones is started - it plays twenty tones
    while the main script waits for the touch sensor button to be 'bumped' (pressed and released) 
    5 times. The idea is that bumping five times will cause the tone-playing to be interrupted. 
    But if you try running the script you will observe that in this case the playing of the tones 
    is NOT interrupted if you bump the sensor 5 times. However, if the tones stop before the five 
    bumps have been finished then program execution stops after the bumps (and the beep) have been 
    completed, as you would expect. 
    """
    ts = TouchSensor()
    sound = Sound()

    def twenty_tones():
        for j in range(0,20):           # Do twenty times.
            sound.play_tone(1000, 0.2)  # 1000Hz for 0.2s
            sleep(0.5)

    t = Thread(target=twenty_tones)
    t.start()

    for i in range(0,5):       # Do five times, with i = 0, 1, 2, 3, 4.
        ts.wait_for_bump()

    sound.beep()


# List of functions
# speak_and_rotate()
# leds()
# write_to_lcd()
# write_to_console()
# display_different_fonts()
# large_motor()
# medium_motor()
# move_steering_by_angle()
# sensors()
# get_color_intensity()
# get_rgb()
# remote_control_one_button()
# distance_to_beacon()
# speech_examples()
# sounds_examples()
# mutlithreading()

master_function()