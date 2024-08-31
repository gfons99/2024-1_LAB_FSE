### LIBRARIES ###
from gpiozero import LEDBoard
from time import sleep
from signal import pause

### PINS ###
leds = LEDBoard(17, 27, 22, 10, 9)

### CODE ###
leds.on()
sleep(1)
leds.off()
sleep(1)
leds.value = (1, 0, 1, 0, 1)
sleep(1)
leds.blink()
pause()
