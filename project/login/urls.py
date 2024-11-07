from login import views
from django.urls import path


urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login-page'),
    path('register', views.register_page, name='register-page')
]