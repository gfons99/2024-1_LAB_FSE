from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import asyncio
import smbus2
import struct
import time
import threading
import RPi.GPIO as GPIO
from gpiozero import PWMLED  # Import the PWMLED class for controlling the LED brightness

SLAVE_ADDR = 0x08  # I2C address for the Arduino

# Initialize the I2C bus
i2c = smbus2.SMBus(1)
GPIO.setmode(GPIO.BCM)
# Initialize a PWM LED on GPIO 4
led = PWMLED(4)

# Configuración de los pines GPIO
IN1_1= 14  # Pin GPIO conectado a IN1 del ULN2003
IN2_1= 15  # Pin GPIO conectado a IN2 del ULN2003
IN3_1= 18  # Pin GPIO conectado a IN3 del ULN2003
IN4_1= 23  # Pin GPIO conectado a IN4 del ULN2003
# Configuración de los pines GPIO para el motor 2 motor izquierdo
IN1_2 = 25  # Pin GPIO conectado a IN1 del ULN2003 para el motor 2
IN2_2 = 8   # Pin GPIO conectado a IN2 del ULN2003 para el motor 2
IN3_2 = 7   # Pin GPIO conectado a IN3 del ULN2003 para el motor 2
IN4_2 = 1   # Pin GPIO conectado a IN4 del ULN2003 para el motor 2
# Configuración de los pines


GPIO.setup(IN1_1, GPIO.OUT)
GPIO.setup(IN2_1, GPIO.OUT)
GPIO.setup(IN3_1, GPIO.OUT)
GPIO.setup(IN4_1, GPIO.OUT)
GPIO.setup(IN1_2, GPIO.OUT)
GPIO.setup(IN2_2, GPIO.OUT)
GPIO.setup(IN3_2, GPIO.OUT)
GPIO.setup(IN4_2, GPIO.OUT)
# Definición de la secuencia para el motor
step_sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]
def set_step_motor1(w1, w2, w3, w4):
    GPIO.output(IN1_1, w1)
    GPIO.output(IN2_1, w2)
    GPIO.output(IN3_1, w3)
    GPIO.output(IN4_1, w4)

# Función para controlar los pasos del motor 2
def set_step_motor2(w1, w2, w3, w4):
    GPIO.output(IN1_2, w1)
    GPIO.output(IN2_2, w2)
    GPIO.output(IN3_2, w3)
    GPIO.output(IN4_2, w4)
def move_steps_motor1(steps, delay, direction=1):
    for _ in range(steps):
        for step in (step_sequence if direction == 1 else reversed(step_sequence)):
            set_step_motor1(*step)
            time.sleep(delay)

# Función para mover el motor 2 en una dirección específica
def move_steps_motor2(steps, delay, direction=1):
    for _ in range(steps):
        for step in (step_sequence if direction == 1 else reversed(step_sequence)):
            set_step_motor2(*step)
            time.sleep(delay)


TOKEN = '7464400664:AAH6KvXIJnE3j-ft8jC8nVEf7BrXVIVkaM0'

async def iniciar(update: Update, context):
    # Crea el menú inicial
    teclado = [
        [InlineKeyboardButton("Reporte general (reporte)", callback_data='sensor_1')],
        [InlineKeyboardButton("Solución nutritiva hidropónica", callback_data='sensor_2')],
        [InlineKeyboardButton("Temperatura", callback_data='sensor_3')],
        [InlineKeyboardButton("Humedad", callback_data='sensor_4')],
        [InlineKeyboardButton("Iluminacion recibida", callback_data='sensor_5')],
        [InlineKeyboardButton("PH", callback_data='sensor_6_')],
        [InlineKeyboardButton("Turbidez", callback_data='sensor_7')],
        [InlineKeyboardButton("Abrir Compuertas", callback_data='sensor_8')],
        [InlineKeyboardButton("Apagado de luz", callback_data='sensor_9')],
    ]
    reply_markup = InlineKeyboardMarkup(teclado)
    await update.message.reply_text('Bienvenido, selecciona la opción de tu preferencia:', reply_markup=reply_markup)


async def boton(update: Update, context):
    consulta = update.callback_query
    await consulta.answer()  # Confirma que la consulta fue recibida
    await consulta.edit_message_text(text="Procesando... Por favor espera.")

    # Agregar un retraso no bloqueante (si es necesario)
    await asyncio.sleep(3)

    # Procesar según la opción seleccionada
    if consulta.data == 'sensor_1':
        await procesar_sensor_1(consulta)
    elif consulta.data == 'sensor_2':
        await procesar_sensor_2(consulta)
    elif consulta.data == 'sensor_3':
        await procesar_sensor_3(consulta)
    elif consulta.data == 'sensor_4':
        await procesar_sensor_4(consulta)
    elif consulta.data == 'sensor_5':
        await procesar_sensor_5(consulta)
    elif consulta.data == 'sensor_6':
        await procesar_sensor_6(consulta)
    elif consulta.data == 'sensor_7':
        await procesar_sensor_7(consulta)
    elif consulta.data == 'sensor_8':
        await procesar_sensor_8(consulta)
    elif consulta.data == 'sensor_9':
        await procesar_sensor_9(consulta)

    # Mostrar el menú principal después de procesar
    await mostrar_menu(consulta, context)


async def procesar_sensor_1(consulta):
    await consulta.edit_message_text(text="Procesando... Reporte.")
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"Conductividad: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de Conductividad: {str(e)}")
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"Temperatura: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de temperatura: {str(e)}")
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"Iluminacion recibida: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de Iluminacion: {str(e)}")
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"Turbidez: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de Turbidez: {str(e)}")
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"PH: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de PH: {str(e)}")


async def procesar_sensor_2(consulta):
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"Conductividad: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de Conductividad: {str(e)}")

async def procesar_sensor_3(consulta):
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"Temperatura: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de Temperatura: {str(e)}")


async def procesar_sensor_4(consulta):
    await consulta.edit_message_text(text="Procesando..Humedad")


async def procesar_sensor_5(consulta):
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"Iluminacion recibida: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de Iluminacion: {str(e)}")


async def procesar_sensor_6(consulta):
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"PH: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de PH: {str(e)}")


async def procesar_sensor_7(consulta):
    try:
        # Simular la lectura de valores de un sensor (esto debería ser reemplazado por la lectura real del sensor)
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el primer valor (por ejemplo, la conductividad)
        await consulta.edit_message_text(text=f"Turbidez: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de Turbidez: {str(e)}")


async def procesar_sensor_8(consulta):
    def rotate_motor1_to_initial_position():
        steps_per_rev = 507  # Pasos para una vuelta completa
        steps_to_move = int(90 / (360 / steps_per_rev))  # Pasos para 90 grados

        # Girar hacia atrás (nuevo sentido contrario)
        move_steps_motor1(steps_to_move, 0.002, direction=-1)
        time.sleep(60)
    # Regresar a la posición inicial hacia adelante
        move_steps_motor1(steps_to_move, 0.002, direction=1)

# Función para girar el motor 2 a 90° y regresar a su posición inicial en el sentido opuesto

    def rotate_motor2_to_initial_position():
        steps_per_rev = 507  # Pasos para una vuelta completa
        steps_to_move = int(90 / (360 / steps_per_rev))  # Pasos para 90 grados

    # Girar hacia adelante (sentido opuesto al motor 1)
        move_steps_motor2(steps_to_move, 0.002, direction=1)
        time.sleep(60)
    # Regresar a la posición inicial hacia atrás
        move_steps_motor2(steps_to_move, 0.002, direction=-1)

    try:
    # Crear hilos para que ambos motores se muevan al mismo tiempo
        motor1_thread = threading.Thread(target=rotate_motor1_to_initial_position)
        motor2_thread = threading.Thread(target=rotate_motor2_to_initial_position)

    # Iniciar ambos hilos
        motor1_thread.start()
        motor2_thread.start()

    # Esperar a que ambos hilos terminen
        motor1_thread.join()
        motor2_thread.join()

    finally:
        GPIO.cleanup()
async def procesar_sensor_9(consulta):
    await consulta.edit_message_text(text="LUZ")

async def mostrar_menu(consulta, context):
    # Crea el menú principal de nuevo después de cada consulta
    teclado = [
        [InlineKeyboardButton("Reporte general (reporte)", callback_data='sensor_1')],
        [InlineKeyboardButton("Solución nutritiva hidropónica", callback_data='sensor_2')],
        [InlineKeyboardButton("Temperatura", callback_data='sensor_3')],
        [InlineKeyboardButton("Humedad", callback_data='sensor_4')],
        [InlineKeyboardButton("Iluminacion recibida", callback_data='sensor_5')],
        [InlineKeyboardButton("PH", callback_data='sensor_6_')],
        [InlineKeyboardButton("Turbidez", callback_data='sensor_7')],
        [InlineKeyboardButton("Abrir Compuertas", callback_data='sensor_8')],
        [InlineKeyboardButton("Apagado de luz", callback_data='sensor_9')],
    ]

    reply_markup = InlineKeyboardMarkup(teclado)

    # Utiliza consulta.message en lugar de update.message
    await consulta.message.reply_text('Selecciona una opción:', reply_markup=reply_markup)


def main():
    application = Application.builder().token(TOKEN).build()

    # Comandos y manejadores de callbacks
    application.add_handler(CommandHandler("start", iniciar))
    application.add_handler(CallbackQueryHandler(boton))

    # Ejecutar la aplicación en modo de polling
    application.run_polling()


if __name__ == '__main__':
    main()

