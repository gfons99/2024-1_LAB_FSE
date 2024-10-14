import smbus2
import struct
import time
import threading

SLAVE_ADDR = 0x08  # I2C address

# Initialize the I2C bus; RPI version 1 requires smbus.SMBus(0)
i2c = smbus2.SMBus(1)

def readTemperature():
    while True:  # Keep reading temperature in a loop
        try:
            msg = smbus2.i2c_msg.read(SLAVE_ADDR, 4)
            i2c.i2c_rdwr(msg)  # Performs write (read request)
            data = list(msg)   # Converts stream to list
            # list to array of bytes (required to decode)
            ba = bytearray(data)
            temp = struct.unpack('<f', ba)[0]  # Unpack the float value
            print(f'Received temp: {temp:.2f}°C')
        except Exception as e:
            print("Error reading temperature:", e)
        
        time.sleep(1)  # Wait for 1 second before reading again

def main():
    # Start temperature monitoring thread
    temp_thread = threading.Thread(target=readTemperature)
    temp_thread.daemon = True  # Set as daemon so it will exit when the main thread exits
    temp_thread.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
