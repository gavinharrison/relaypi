#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Inisalising a list of the GPIO pin numbers.
pinList = [2, 3, 4, 17]

# Looping through each GPIO pin and seting the mode and state to 'high'.
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Inisalising the time delay between operations in the main loop.
DelayInSeconds = 2

# Main loop
try:
  GPIO.output(2, GPIO.LOW)
  print "ONE"
  time.sleep(DelayInSeconds);
  GPIO.output(3, GPIO.LOW)
  print "TWO"
  time.sleep(DelayInSeconds);
  GPIO.output(4, GPIO.LOW)
  print "THREE"
  time.sleep(DelayInSeconds);
  GPIO.output(17, GPIO.LOW)
  print "FOUR"
  time.sleep(DelayInSeconds);
  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard crtl+c
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/WpM1aq4B8-A
