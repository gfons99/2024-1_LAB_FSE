/*
* arduino-photoresistor.cpp
*
* Author:  Mauricio Matamoros
* Date:    2020.03.01
* License: MIT
*
* Reads the analog input from A0 using a photoresistor with a voltage divider
* and sends the value via I2C bus.
*
*/

#include <Wire.h>

// Constants
#define VAREF 5.0           // Reference voltage for the ADC
#define I2C_SLAVE_ADDR 0x0A
#define BOARD_LED 13

// Global variables
float light_intensity = 0;

// Prototypes
void i2c_received_handler(int count);
void i2c_request_handler(int count);
float read_light(void);

/**
* Setup the Arduino
*/
void setup(void){
	// Configure ADC to use voltage reference from AREF pin (external)
	analogReference(EXTERNAL);

	// Configure I2C to run in slave mode with the defined address
	Wire.begin(I2C_SLAVE_ADDR);
	// Configure the handler for received I2C data
	Wire.onReceive(i2c_received_handler);
	// Configure the handler for request of data via I2C
	Wire.onRequest(i2c_request_handler);

	// Setup the serial port to operate at 56.6kbps
	Serial.begin(56600);

	// Setup board led
	pinMode(BOARD_LED, OUTPUT);
}

/**
* Handles data requests received via the I2C bus
* It will immediately send the light intensity read as a float value
*/
void i2c_request_handler(){
	Wire.write((byte*) &light_intensity, sizeof(float));
}

/**
* Handles received data via the I2C bus.
* Data is forwarded to the Serial port and makes the board led blink
*/
void i2c_received_handler(int count){
	char received = 0;
	while (Wire.available()){
		received = (char)Wire.read();
		digitalWrite(BOARD_LED, received ? HIGH : LOW);
		Serial.println(received);
	}
}

// 
float read_light(void){
	int sensorValue = analogRead(0);
	float voltage = VAREF * (sensorValue / 1024.0);
	return voltage;
}

void loop(){
	// Read the light intensity and store it
	light_intensity = read_light();
	// Print the light intensity for debugging
	Serial.print("Light intensity (V): ");
	Serial.println(light_intensity);
	delay(100);
}
