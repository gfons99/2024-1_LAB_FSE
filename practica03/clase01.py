### LIBRARIES ###
from bluedot import BlueDot 
from signal import pause 

### PINS ###


### CODE ###
def saludo(): 
    print("Hola Mundo") 
 
def despedida(): 
    print("Hasta pronto") 
 
bd = BlueDot() 
bd.when_pressed = saludo 
bd.when_released = despedida 
 
pause()

 
