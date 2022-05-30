from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.LoginView.as_view(), name='login'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('', views.PostCreateView.as_view(), name='image'),
    ]
