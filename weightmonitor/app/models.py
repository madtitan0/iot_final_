from django.db import models

class Weight(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
