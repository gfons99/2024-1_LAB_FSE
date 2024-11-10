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

def read_analog_values():
    while True:
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
            for i, value in enumerate(analog_values):
                print(f'Received analog{i}: {value:.2f}')
            
            # Use the first analog value (analog0) to control the LED brightness
            # Normalize to a value between 0 and 1 for PWM control
            normalized_value = min(max(analog_values[0] / 5.0, 0), 1)
            led.value = normalized_value
        
        except Exception as e:
            # Handle any errors that occur during the reading process
            print("Error reading analog values:", e)
        
        time.sleep(1)  # Pause for 1 second before the next reading

def main():
    # Start the analog value monitoring thread
    analog_thread = threading.Thread(target=read_analog_values)
    analog_thread.daemon = True  # Set as daemon thread to exit when the main program exits
    analog_thread.start()

    # Keep the main program running indefinitely
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
