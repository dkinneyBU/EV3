# EV3
Mindstorms EV3 code

![My EV3](https://github.com/dkinneyBU/EV3/blob/master/MyEV3.PNG)

These are all various Python programs for my Legos Mindstorms EV3 device. In its current configuration is has infrared, color, and touch sensors. I also have a Pixy camera module but I've had the hardest time getting that programmed. The Python code I have running on it right now will have the robot motor along in a straight line until either the infrared or touch sensor is triggered, at which point it will turn around at a roughly oblique angle, and motor on until it encounters another obstruction. It also feeds back the color sensor data; I hope to add to the data gathering in the near future.

My next endeavor will be to research a Machine Learning application, whereby the little fella can learn as it motors through life.

**ultrasonic_sensor** - I don't actually have an ultrasonic sensor, but I *do* have an infrared sensor. So I heavily modified this code (well maybe not heavily, I can't really remember at this point what was there and what I added) to work with the sensors I have at hand. I've been working lately to "dial in" some of the parameters. For instance, I have the infrared sensor stopping to turn around at 50 mm, which is a bit before the touch sensor would get triggered. However there are times the robot encounters barriers where neither sensor gets triggered. I think the easiest approach is going to be modifying the touch sensor's "arm" to cover a greater space.

The other thing I learned recently was to click on VS Code's **Output** tab if I want to monitor the data the robot's sensors are recording.

All in all, I'm having a lot of fun with this one. I really need to integrate my Pixy camera now...

I will add more to the documentation soon...
