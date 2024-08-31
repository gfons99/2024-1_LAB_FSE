### LIBRARIES ###
from gpiozero import LED, Button
from signal import pause

### PINS ###
led = LED(17)
button = Button(2)

### CODE ###
button.when_pressed = led.on
button.when_released = led.off
pause()
