
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weightmonitor.settings')

# Initialize Django
django.setup()

from app.models import Weight

# Access your database and perform operations with the Weight model
weights = Weight.objects.all()
for weight in weights:
    print(weight.value, weight.timestamp)
