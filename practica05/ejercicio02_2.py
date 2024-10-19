import smbus2
import struct
import time
import threading
from gpiozero import PWMLED  # Import the PWMLED class for controlling the LED brightness

SLAVE_ADDR = 0x08  # I2C address for the voltage sensor

# Initialize the I2C bus. Use smbus.SMBus(0) for Raspberry Pi version 1.
i2c = smbus2.SMBus(1)

# Initialize a PWM LED on GPIO 4
led = PWMLED(4)

def readVoltage():
    while True:  # Continuously read voltage in a loop
        try:
            # Prepare to read 4 bytes from the I2C slave
            msg = smbus2.i2c_msg.read(SLAVE_ADDR, 4)
            # Execute the read request on the I2C bus
            i2c.i2c_rdwr(msg)
            # Convert the I2C message stream to a list of bytes
            data = list(msg)
            
            # Convert the list of bytes to a bytearray for decoding
            ba = bytearray(data)
            # Unpack the bytearray as a float value (voltage)
            voltage = struct.unpack('<f', ba)[0]
            
            # Print the received voltage value formatted to two decimal places
            print(f'Received voltage: {voltage:.2f} V')
            
            # Normalize the voltage to a value between 0 and 1 for PWM control
            # Assuming max voltage is 5V, change this value if different
            normalized_voltage = min(max(voltage / 5.0, 0), 1)
            
            # Set the LED brightness based on the normalized voltage
            led.value = normalized_voltage
        
        except Exception as e:
            # Handle any errors that occur during the reading process
            print("Error reading voltage:", e)
        
        time.sleep(1)  # Pause for 1 second before the next reading

def main():
    # Start the voltage monitoring thread
    voltage_thread = threading.Thread(target=readVoltage)
    voltage_thread.daemon = True  # Set as daemon thread to exit when the main program exits
    voltage_thread.start()

    # Keep the main program running indefinitely
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
