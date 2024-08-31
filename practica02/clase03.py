### LIBRARIES ###
from gpiozero import PWMLED
from time import sleep

### PINS ###
led = PWMLED(17)

### CODE ###
while True:
	led.value = 0
	sleep(1)
	led.value = 0.3
	sleep(1)
	led.value = 0.6
	sleep(1)
	led.value = 1.0
	sleep(1)
