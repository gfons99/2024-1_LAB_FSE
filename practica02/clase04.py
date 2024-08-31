### LIBRARIES ###
from gpiozero import Button

### PINS ###
button = Button(2)

### CODE ###
while True:
	if button.is_pressed:
		print("Button is pressed")
	else:
		print("Button is not pressed")
