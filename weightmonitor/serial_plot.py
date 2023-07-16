import os
import django
import serial

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weightmonitor.settings')

# Initialize Django
django.setup()

from app.models import Weight

ser = serial.Serial('COM7', 9600)  # Replace 'COM13' with your ESP32's serial port

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        weight_value = float(line)
        print(weight_value)
        weight = Weight(value=weight_value)
        weight.save()
    except ValueError:
        print("Invalid weight value:", line)
