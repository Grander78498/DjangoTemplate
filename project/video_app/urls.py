from video_app import views
from django.urls import path


urlpatterns = [
    path('', views.root_page),
    path('main/', views.main_page, name='main-page')
]
