#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
pinList = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 21, 20]

# loop through pins and set mode and state to 'high'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

try:
  while True:
    print "Enter the relay number you want toggle"

    try:
        # Getting the users input and checking that is is a number.
        input = raw_input("[1 - "+ str(len(pinList)) +"] ")
        relay = int(input)

        # Checking that the entered number is with in the correct range.
        if relay > 0 and relay <= len(pinList):

            # Toggling the status of the requested relay.
            GPIO.output(pinList[relay-1], not GPIO.input(pinList[relay-1]))
        else:
            print "The entered number is "

    except ValueError:
        print "The entered value is not a number"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

# find more information on this script at
# http://youtu.be/WpM1aq4B8-A
