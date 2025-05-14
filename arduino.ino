#include <Wire.h>
#include "MAX30100_PulseOximeter.h"

#define REPORTING_PERIOD_MS     1000 // Time between data reports

// PulseOximeter object for reading heart rate and SpO2
PulseOximeter pox;

uint32_t tsLastReport = 0;

// Callback fired when a pulse is detected
void onBeatDetected()
{
    Serial.println("Beat!");
}

void setup()
{
    Serial.begin(115200);  // Start serial communication at 115200 baud

    Serial.print("Initializing pulse oximeter...");

    if (!pox.begin()) {
        Serial.println("FAILED");
        for(;;);
    } else {
        Serial.println("SUCCESS");
    }

    // Register the callback for beat detection
    pox.setOnBeatDetectedCallback(onBeatDetected);
}

void loop()
{
    // Update the sensor data
    pox.update();

    // Report heart rate once every second
    if (millis() - tsLastReport > REPORTING_PERIOD_MS) {
        int heartRate = pox.getHeartRate() - 5;
        
        // Only send data if the heart rate is valid
        if (heartRate > 0) {
            Serial.print("Heart rate: ");
            Serial.println(heartRate);
        }

        tsLastReport = millis();  // Update the last report timestamp
    }

    // Optional: Add a small delay to ensure smooth operation and prevent buffer overflow
    delay(10);  // Small delay (e.g., 10ms) to give enough time for the serial data to be processed
}