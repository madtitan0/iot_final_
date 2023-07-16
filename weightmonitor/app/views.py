from django.shortcuts import render
from .models import Weight
from django.http import JsonResponse
import serial

def home(request):
    weights = Weight.objects.all()
    return render(request, 'app/weight.html', {'weights': weights})

import json

def weight_api(request):
    # Configure the serial port
    ser = serial.Serial('COM7', 9600)  # Replace 'COM13' with the correct port name for your ESP32

    while True:
        # Read the weight value from the serial port
        line = ser.readline().decode('latin-1').strip()
        weight_value = float(line)

        # Save the weight data to the database
        weight = Weight(value=weight_value)
        weight.save()

    # You can optionally return a JSON response
    response_data = {'success': True}
    return JsonResponse(response_data)
