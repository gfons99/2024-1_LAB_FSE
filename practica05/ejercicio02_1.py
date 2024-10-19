### LIBRARIES ###
from gpiozero import Button, LED 
from signal import pause 
 
### PINS ###
button = Button(23) 
led = LED(24) 

### CODE ###
button.when_pressed = led.on
button.when_released = led.off
 
pause() 
