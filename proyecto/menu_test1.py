from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import time
import smbus2
import struct
import threading
from gpiozero import PWMLED

SLAVE_ADDR = 0x08  # Dirección I2C para el Arduino
i2c = smbus2.SMBus(1)
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
    await update.message.reply_text('Bienvenido, selecciona la opción de tu preferencia:', reply_markup=reply_markup)

async def boton(update: Update, context):
    consulta = update.callback_query
    await consulta.answer()
    await consulta.edit_message_text(text="Procesando... Por favor espera.")
    time.sleep(3)

    # Procesar la opción seleccionada por el usuario
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

    # Volver a mostrar el menú principal
    await mostrar_menu(consulta, update, context)

async def procesar_sensor_1(consulta):
    try:
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 20)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        ba = bytearray(data)
        analog_values = struct.unpack('<fffff', ba)
        # Mostrar el valor de conductividad (por ejemplo, el primer sensor)
        await consulta.edit_message_text(text=f"Sensor de Conductividad: {analog_values[0]:.2f} V")
    except Exception as e:
        await consulta.edit_message_text(text=f"Error al leer el sensor de Conductividad: {str(e)}")

async def procesar_sensor_2(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de Altura de plantas.")

async def procesar_sensor_3(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de Temperatura.")

async def procesar_sensor_4(consulta):
    await consulta.edit_message_text(text="Pr
