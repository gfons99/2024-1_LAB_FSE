import struct
import time
import threading

SLAVE_ADDR = 0x0A # I2C address

# Initialize the I2C bus;
# RPI version 1 requires smbus.SMBus(0)
i2c = smbus2.SMBus(1)

def readTemperature():
    try:
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 4)
        i2c.i2c_rdwr(msg)  # Performs write (read request)
        data = list(msg)   # Converts stream to list
        # list to array of bytes (required to decode)
        ba = bytearray()
        for c in data:
            ba.append(int(c))
        temp = struct.unpack('<f', ba)
        print('Received temp: {} = {}'.format(data, temp))
        return temp
    except Exception as e:
        print("Error reading temperature:", e)
        return None

def main():
    # Start temperature monitoring thread
    temp_thread = threading.Thread(target=readTemperature)
    temp_thread.daemon = True  # Set as daemon so it will exit when the main thread exits
    temp_thread.start()

if __name__ == '__main__':
    main()
