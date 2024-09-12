### LIBRARIES ###
from gpiozero import LED
from bluedot import BlueDot

from time import sleep

### PINS ###
bd = BlueDot()

verde = LED(17)
amarillo = LED(27)
rojo = LED(22)
b_cambiar = False

### CODE ###
while True:
    	
	verde.on()
	
	if bd.is_pressed:
		b_cambiar = True
		print("Button is pressed")
		sleep(4)	
		verde.off()
	
	if b_cambiar == True:
		amarillo.on()
		sleep(2)
		amarillo.off()
		
		rojo.on()
		sleep(4)
		rojo.off()
		b_cambiar = False
