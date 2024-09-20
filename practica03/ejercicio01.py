from bluedot import BlueDot 
from signal import pause
from gpiozero import LED, LEDBoard
from time import sleep

# a,b,c,d,e,f,g,dp
segment_pins = LEDBoard(13, 6, 16, 20, 21, 19, 26, 12)
CHARACTER_SEGMENTS = {
    'G': (0,1,0,0,0,0,1,1),
    'A': (0,0,0,1,0,0,0,1),
    'D': (1,0,0,0,0,1,0,1),
    'I': (0,1,0,1,1,1,1,1),
    'E': (0,1,1,0,0,0,0,1),
    'L': (1,1,1,0,0,0,1,1),
    'B': (1,1,0,0,0,0,0,1),
    'R': (1,1,1,1,0,1,0,1),
    'Y': (1,0,0,1,1,0,0,1),
    'F': (0,1,1,1,0,0,0,1),
    'N': (1,1,0,1,0,1,0,1) 
}

def display_name(name):
    # This function will display each character of the name one by one on the 7-segment display
    for char in name:
        segments = CHARACTER_SEGMENTS.get(char, (0, 0, 0, 0, 0, 0, 0, 0))  # default to off
        for segment, state in zip(segment_pins, segments):
            segment.value = state
        sleep(1)  # Display each character for 1 second
    clear_display()

def clear_display():
    for segment in segment_pins:
        segment.off()

def dpad(pos): 
    if pos.top: 
        print("GADIEL")
        display_name("GADIEL")
    elif pos.left: 
        print("BRYAN")
        display_name("BRYAN")
    elif pos.right: 
        print("FERNANDA")
        display_name("FERNANDA")
 
bd = BlueDot() 
bd.when_pressed = dpad 
 
pause()
