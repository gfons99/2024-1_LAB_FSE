### LIBRARIES ###
from gpiozero import LED
from signal import pause

### PINS ###
led = LED(17)

### CODE ###
led.blink()
pause()
