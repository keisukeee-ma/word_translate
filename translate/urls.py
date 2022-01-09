from django.urls import path
from . import views

app = 'translate'
urlpatterns = [
    path('', views.kakikomi, name='kakikomi'),
    ]