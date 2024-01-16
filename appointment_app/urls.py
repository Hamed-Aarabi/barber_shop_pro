from . import views
from django.urls import path


app_name = 'appointment'
urlpatterns = [
    path('', views.AppointmentView.as_view(), name='book')
]