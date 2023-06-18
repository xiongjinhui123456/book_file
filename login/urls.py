from django.urls import path
from . import views

urlpatterns = [
    path('logon/',views.logon),
    path('register/', views.RegisterView.as_view())
]