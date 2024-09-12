### LIBRARIES ###
from gpiozero import LED
from bluedot import BlueDot 
from signal import pause 

### CODE ###
def dpad(pos): 
	if pos.top: 
		v.value = 1
		a.value = 0
		r.value = 0.1
	elif pos.left: 
		v.value = 1
		a.value = 0.1
		r.value = 0
	elif pos.right: 
		v.value = 0
		a.value = 0.1
		r.value = 1
		
### PINS ###
v = LED(17)
a = LED(27)
r = LED(22)

bd = BlueDot() 
bd.when_pressed = dpad 
 
pause()
