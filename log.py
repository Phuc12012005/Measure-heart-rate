import serial
import csv
import time

# Replace with the correct COM port (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux/Mac)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=2)  # Update this to your port
time.sleep(2)  # Wait for Arduino to initialize
with open('heart_rate_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'HeartRate_BPM'])

    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    # Read the heart rate directly
                    if "Heart rate:" in line:
                        bpm = float(line.split(":")[1])  # Extract the heart rate value
                    else:
                        bpm = float(line)  # In case the value is just sent directly
                    timestamp = time.time()
                    print(f"{timestamp}, BPM: {bpm}")
                    writer.writerow([timestamp, bpm])
                except ValueError:
                    print(f"Invalid data received: {line}")
    except KeyboardInterrupt:
        print("Logging stopped.")
        ser.close()
