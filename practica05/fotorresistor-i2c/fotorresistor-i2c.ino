#include <Wire.h>

// Constants
#define VAREF 5.0           // Reference voltage for the ADC (typically 5V on most Arduino boards)
#define I2C_SLAVE_ADDR 0x08 // I2C address of the slave device
#define BOARD_LED 13        // Pin number for the onboard LED

// Global variables
float light_intensity = 0;  // Variable to store the calculated light intensity (in volts)

// Function prototypes
void i2c_received_handler(int count); // Function to handle received I2C data
void i2c_request_handler();           // Function to handle I2C data requests
float read_light();                   // Function to read the light intensity from the sensor

/**
* Arduino setup function
* This function configures the necessary hardware, including ADC settings, I2C communication,
* and the serial port for debugging.
*/
void setup(void){
	// Set the ADC to use an external voltage reference (AREF pin) if connected
	analogReference(EXTERNAL);

	// Initialize the Arduino as an I2C slave with the defined address
	Wire.begin(I2C_SLAVE_ADDR);
	// Register the function to handle I2C data requests from the master
	Wire.onRequest(i2c_request_handler);
	// Register the function to handle incoming data via I2C
	Wire.onReceive(i2c_received_handler);

	// Initialize the serial port for debugging at 56,600 bps
	Serial.begin(56600);

	// Set the pin mode for the onboard LED as output
	pinMode(BOARD_LED, OUTPUT);
}

/**
* I2C request handler
* This function is called whenever the master device requests data from the slave.
* It sends the current light intensity as a float value over the I2C bus.
*/
void i2c_request_handler(){
	Wire.write((byte*) &light_intensity, sizeof(float)); // Send the light intensity via I2C
}

/**
* I2C received handler
* This function is called when data is received via the I2C bus.
* It reads the incoming data, prints it to the serial monitor, and controls the LED state.
*/
void i2c_received_handler(int count){
	char received = 0;
	while (Wire.available()){   // Check if data is available to read
		received = (char)Wire.read();  // Read the incoming byte
		// Control the LED: turn it on if data is non-zero, turn it off if zero
		digitalWrite(BOARD_LED, received ? HIGH : LOW);
		// Print the received data to the serial monitor for debugging
		Serial.println(received);
	}
}

/**
* Reads the light intensity from the analog sensor
* This function reads the analog value from pin A0, converts it to a voltage,
* and returns the result as a float.
* 
* @return The voltage corresponding to the light intensity (in volts).
*/
float read_light(void){
	int sensorValue = analogRead(0);   // Read the analog value from A0 (range 0 to 1023)
	// Convert the analog value to a voltage based on the reference voltage (VAREF)
	float voltage = VAREF * (sensorValue / 1024.0);
	return voltage;  // Return the calculated voltage
}

/**
* Arduino main loop function
* This function continuously reads the light intensity, stores the value, prints it for debugging,
* and adds a delay between readings.
*/
void loop(){
	// Read the current light intensity and store it in the global variable
	light_intensity = read_light();
	
	// Print the light intensity (in volts) to the serial monitor for debugging
	Serial.print("Light intensity (V): ");
	Serial.println(light_intensity);
	
	// Add a delay of 100 milliseconds before the next reading
	delay(100);
}
