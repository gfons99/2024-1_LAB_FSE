### LIBRERÍAS ###
import telebot
from gpiozero import LED, DistanceSensor
from time import sleep

### PINES ###
led = LED(17)
sensor = DistanceSensor(echo=15, trigger=18)

### TELEGRAM BOT ###
bot = telebot.TeleBot("7278491826:AAErSRgcXVHu3LE-JfIwqvwXuAY9XBnFjE8")

# Umbral de distancia en metros
THRESHOLD_DISTANCE = 0.2  # 20 cm


# VARIABLES GLOBALES
alert_sent = False # Solo se envían alertas si la distancia pasa de ser mayor al umbral a menor del umbral
started_chat_id = ""

@bot.message_handler(commands=['start'])
def send_start(message):
    global started_chat_id
    started_chat_id = message.chat.id  # Obtener la ID del chat actual
    bot.reply_to(message, f"Welcome! Your chat ID is {started_chat_id}")

### ALARMA DE PROXIMIDAD ###
def proximity_alarm():
    global alert_sent, started_chat_id
    while True:
        distance = sensor.distance  # Distancia en metros
        if started_chat_id != "":  # Ver que exista un chat
            if distance < THRESHOLD_DISTANCE:
                # Si el LED está apagado entonces no hay alerta, hay que encenderlo y enviar una alerta
                if not alert_sent:
                    led.on()
                    bot.send_message(chat_id=started_chat_id, text=f"¡Alerta! Distancia corta detectada: {distance*100:.2f} cm.")
                    alert_sent = True
            else:
                # # Si la distancia es mayor al umbral, encendemos el LED
                if alert_sent:
                    led.off()  # Turn off the LED
                    alert_sent = False  # Habilitar en envío de alertas (reiniciar el sistema)
        sleep(1)  # Tiempo de espera en cada muestreo

# Monitoreo de la proximidad en un hilo diferente
import threading
proximity_thread = threading.Thread(target=proximity_alarm)
proximity_thread.daemon = True
proximity_thread.start()

### TELEGRAM BOT POLLING ###
bot.infinity_polling()
