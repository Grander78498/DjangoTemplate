from login import views
from django.urls import path


urlpatterns = [
    path('login', views.login_page, name='login-page')
]