from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    # path('', views.simple_upload, name='image')
    ]
