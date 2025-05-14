# Measure-heart-rate
This is a small DIY project build by a group of HUST student. The project using max30100 sensor to measure the heart rate, arduino uno as controller. You should have arduino ide to upload code. The project also include two files analyze the output of the sensor.

## How to connect sensor with arduino

GND - GND

SCL - A5

SDA - A4

VIN - 3.3V

## Upload the code

1. Copy and upload the arduino.ino file to your arduino
2. Install the max30100 library from Oxullo in library manager

3. You should see the output on serial monitor

## Get the output and put it on CSV file
1. Create virtual env and install library

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

2. Get the output

- Connect arduino and computer. See the port on the Arduino IDE. Change the port in source code as it is.
- Turn off arduino ide
- Run the log.py

3. Check if the output is on CSV file or not
4. Run the analyze file