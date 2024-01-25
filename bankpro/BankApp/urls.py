from .import views
from django.urls import path

app_name = 'BankApp'

urlpatterns = [
    path("",views.home,name = 'home')
     ]