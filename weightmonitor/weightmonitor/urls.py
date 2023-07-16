from django.urls import path, include
from app import views
urlpatterns = [
    path('',views.home,name='home'),
    path('weight/api/', views.weight_api, name='weight_api'),
]
