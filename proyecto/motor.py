import RPi.GPIO as GPIO
import time

# Configurar los pines GPIO
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Secuencia de activación del motor paso a paso
secuencia = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

def mover_motor(pasos, direccion):
    for _ in range(pasos):
        for paso in secuencia[::direccion]:
            GPIO.output(IN1, paso[0])
            GPIO.output(IN2, paso[1])
            GPIO.output(IN3, paso[2])
            GPIO.output(IN4, paso[3])
            time.sleep(0.001)  # Ajustar para la velocidad

try:
    # Mover hacia adelante 512 pasos (una revolución)
    mover_motor(512, 1)
    time.sleep(1)

    # Mover hacia atrás 512 pasos (una revolución)
    mover_motor(512, -1)

except KeyboardInterrupt:
    GPIO.cleanup()
