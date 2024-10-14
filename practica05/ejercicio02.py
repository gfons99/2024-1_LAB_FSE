import smbus2
import struct
import time
import threading

SLAVE_ADDR = 0x08  # I2C address for the voltage sensor

# Initialize the I2C bus. Use smbus.SMBus(0) for Raspberry Pi version 1.
i2c = smbus2.SMBus(1)

def readVoltage():
    while True:  # Continuously read voltage in a loop
        try:
            msg = smbus2.i2c_msg.read(SLAVE_ADDR, 4)  # Prepare to read 4 bytes from the I2C slave
            i2c.i2c_rdwr(msg)  # Execute the read request on the I2C bus
            data = list(msg)   # Convert the I2C message stream to a list of bytes
            
            # Convert the list of bytes to a bytearray for decoding
            ba = bytearray(data)
            voltage = struct.unpack('<f', ba)[0]  # Unpack the bytearray as a float value (voltage)
            
            # Print the received voltage value formatted to two decimal places
            print(f'Received voltage: {voltage:.2f} V')
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
