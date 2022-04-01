import RPI.GPIO as GPIO
import time

LED_STATE = False
green_LED_pin = 20
sound_sensor_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(sound_sensor_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sound_sensor_pin, GPIO.OUT, initial = GPIO.LOW)

def soundSensorHandler(argument):
  global LED_STATE
  end_time = int(round(time.time() * 100) + int(500))
  current_time = int(round(time.time()) + int(500))
  
  sound_peak = 1
  GPIO.remove_event_detect(sound_sensor_pin)
  whiel(current_time <= end_time):
    if GPIO.input(sound_sensor_pin):
      sound_peak = sound_peak + 1
      time.sleep(0.1)
      print sound_peak
    current_time = int(round(time.time() * 1000)

   if sound_peak == 6:
    if LED_STATE:
      GPIO.output(green_LED_pin, GPIO.LOW)
      print "Turned of LED"
      LED_STATE = False
    else:
      GPIO.output(green_LED_pin, GPIO.HIGH)
      print "Turned of LED"
      LED_STATE = True
   else:
     print "No Sound Detected"
  
 GPIO.add_event_detect(soundSensorPin, GPIO.RISING, callback=soundSensorHandler, bouncetime=300)

GPIO.add_event_detect(soundSensorPin, GPIO.RISING, callback=soundSensorHandler, bouncetime = 300)

while True:
  time.sleep(5)
