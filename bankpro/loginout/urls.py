from . import views
from django.urls import path

app_name = 'LoginOut'

urlpatterns = [
    path("login", views.login, name='login'),
    path('register', views.register, name='register'),
    path("logout", views.logout, name="logout"),
    path("form", views.form, name="form"),
    path("formindex", views.formindex, name="formindex")

]
