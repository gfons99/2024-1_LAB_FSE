### LIBRARIES ###
from gpiozero import LED
from time import sleep

### PINS ###
led = LED(17)

### CODE ###
while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)
