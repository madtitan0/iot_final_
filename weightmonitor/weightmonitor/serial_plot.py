import os
import django
import serial

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weight_monitor.settings')

# Initialize Django
django.setup()

from weight_app.models import Weight

ser = serial.Serial('COM13', 9600)  # Replace 'COM13' with your ESP32's serial port

while True:
    line = ser.readline().decode('utf-8').strip()
    weight_value = float(line)
    weight = Weight(value=weight_value)
    weight.save()
