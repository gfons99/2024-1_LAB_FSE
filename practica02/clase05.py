### LIBRARIES ###
from gpiozero import Button

### PINS ###
button = Button(2)

### CODE ###
button.wait_for_press()
print("Button was pressed")
