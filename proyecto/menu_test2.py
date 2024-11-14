from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import asyncio
import smbus2
import struct
from gpiozero import PWMLED  # Import the PWMLED class for controlling the LED brightness

SLAVE_ADDR = 0x08  # I2C address for the Arduino

# Initialize the I2C bus
i2c = smbus2.SMBus(1)

# Initialize a PWM LED on GPIO 4
led = PWMLED(4)

TOKEN = '7464400664:AAH6KvXIJnE3j-ft8jC8nVEf7BrXVIVkaM0'


async def iniciar(update: Update, context):
    # Crea el menú inicial
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

    # Mostrar el menú principal después de procesar
    await mostrar_menu(consulta, context)


async def procesar_sensor_1(consulta):
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


async def procesar_sensor_2(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de altura de plantas.")


async def procesar_sensor_3(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de temperatura.")


async def procesar_sensor_4(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de movimiento.")


async def procesar_sensor_5(consulta):
    await consulta.edit_message_text(text="Procesando... Sensor de presión.")


async def mostrar_menu(consulta, context):
    # Crea el menú principal de nuevo después de cada consulta
    teclado = [
        [InlineKeyboardButton("Revisa Conductividad", callback_data='sensor_1')],
        [InlineKeyboardButton("Altura de plantas", callback_data='sensor_2')],
        [InlineKeyboardButton("Temperatura", callback_data='sensor_3')],
        [InlineKeyboardButton("Abrir puertas: Movimiento", callback_data='sensor_4')],
        [InlineKeyboardButton("Encender luz interior", callback_data='sensor_5')]
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
