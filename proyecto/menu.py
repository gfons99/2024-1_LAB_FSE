from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import time
import smbus2
import struct
import time
import threading
from gpiozero import PWMLED  # Import the PWMLED class for controlling the LED brightness

SLAVE_ADDR = 0x08  # I2C address for the Arduino

# Initialize the I2C bus. Use smbus.SMBus(0) for Raspberry Pi version 1.
i2c = smbus2.SMBus(1)

# Initialize a PWM LED on GPIO 4
led = PWMLED(4)

TOKEN = '7464400664:AAH6KvXIJnE3j-ft8jC8nVEf7BrXVIVkaM0'

async def iniciar(update: Update, context):
    teclado = [
        [InlineKeyboardButton("Revisa Conductividad", callback_data='sensor_1')],
        [InlineKeyboardButton("Altura de plantas", callback_data='sensor_2')],
        [InlineKeyboardButton("Temperatura", callback_data='sensor_3')],
        [InlineKeyboardButton("Abrir puertas: Movimiento", callback_data='sensor_4')],
        [InlineKeyboardButton("Encender luz interior", callback_data='sensor_5')]
    ]
    reply_markup = InlineKeyboardMarkup(teclado)
    await update.message.reply_text('Bienvenido, selecciona la opcion de tu preferencia:', reply_markup=reply_markup)

async def boton(update: Update, context):
    consulta = update.callback_query
    await consulta.answer()
    await consulta.edit_message_text(text="Procesando... Por favor espera.")
    time.sleep(3)

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

    await mostrar_menu(update, context)

async def procesar_sensor_1(consulta):
	 try:
            # Prepare to read 20 bytes from the I2C slave (5 floats * 4 bytes each)
            msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
            # Execute the read request on the I2C bus
            i2c.i2c_rdwr(msg)
            # Convert the I2C message stream to a list of bytes
            data = list(msg)
            
            # Convert the list of bytes to a bytearray for decoding
            ba = bytearray(data)
            # Unpack the bytearray as five float values
            analog_values = struct.unpack('<fffff', ba)
            
            # Print each received analog value formatted to two decimal places
            
            print(analog_values[0])            
            # Use the first analog value (analog0) to control the LED brightness
            # Normalize to a value between 0 and 1 for PWM control
            normalized_value = min(max(analog_values[0] / 5.0, 0), 1)
            led.value = normalized_value
        
          except Exception as e:
            # Handle any errors that occur during the reading process
            print("Error reading analog values:", e)
        
       	  time.sleep(1)  # Pause for 1 second before the next reading

async def procesar_sensor_2(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de humedad.")

async def procesar_sensor_3(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de luz.")

async def procesar_sensor_4(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de movimiento.")

async def procesar_sensor_5(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de presión.")

async def mostrar_menu(update: Update, context):
    teclado = [
        [InlineKeyboardButton("Revisa Conductividad", callback_data='sensor_1')],
        [InlineKeyboardButton("Altura de plantas", callback_data='sensor_2')],
        [InlineKeyboardButton("Temperatura", callback_data='sensor_3')],
        [InlineKeyboardButton("Abrir puertas: Movimiento", callback_data='sensor_4')],
        [InlineKeyboardButton("Encender luz interior", callback_data='sensor_5')]
    ]
    reply_markup = InlineKeyboardMarkup(teclado)
    await update.callback_query.message.edit_text('Bienvenido, selecciona la opcion de tu preferencia:', reply_markup=reply_markup)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", iniciar))
    application.add_handler(CallbackQueryHandler(boton))

    application.run_polling()

    analog_thread = threading.Thread(target=read_analog_values)
    analog_thread.daemon = True  # Set as daemon thread to exit when the main program exits
    analog_thread.start()

    # Keep the main program running indefinitely
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
