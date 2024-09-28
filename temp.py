### LIBRARIES ###
import telebot
from gpiozero import LED, DistanceSensor
from time import sleep

### PINS ###
led = LED(17)  # LED connected to GPIO 17
# Set up the ultrasonic sensor with GPIO pins (Echo on 15, Trigger on 18)
sensor = DistanceSensor(echo=15, trigger=18)

### TELEGRAM BOT ###
bot = telebot.TeleBot("7278491826:AAErSRgcXVHu3LE-JfIwqvwXuAY9XBnFjE8")

# Threshold distance in meters (adjust as needed for "short distance")
THRESHOLD_DISTANCE = 0.2  # 20 cm

# Store if an alert was sent to avoid repeated messages
alert_sent = False

# Global variable to store chat ID
started_chat_id = ""

@bot.message_handler(commands=['start'])
def send_start(message):
    global started_chat_id  # Declare as global to modify the global variable
    started_chat_id = message.chat.id  # Get the chat ID from the message object
    bot.reply_to(message, f"Welcome! Your chat ID is {started_chat_id}")

### PROXIMITY ALARM ###
def proximity_alarm():
    global alert_sent, started_chat_id
    while True:
        distance = sensor.distance  # distance in meters
        if started_chat_id != "":  # Check if chat_id is set
            if distance < THRESHOLD_DISTANCE:
                # If the LED is off, turn it on and send an alert
                if not alert_sent:
                    led.on()  # Turn on the LED
                    bot.send_message(chat_id=started_chat_id, text=f"¡Alerta! Distancia corta detectada: {distance*100:.2f} cm.")
                    alert_sent = True  # Mark that an alert has been sent
            else:
                # If the distance is safe, turn off the LED
                if alert_sent:
                    led.off()  # Turn off the LED
                    alert_sent = False  # Reset alert status
        sleep(1)  # Adjust sleep time for how often you want to check the distance

# Start proximity monitoring in the background
import threading
proximity_thread = threading.Thread(target=proximity_alarm)
proximity_thread.daemon = True
proximity_thread.start()

### TELEGRAM BOT POLLING ###
bot.infinity_polling()
