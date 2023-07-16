from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path(' ', views.weight_view, name='weight'),
]
