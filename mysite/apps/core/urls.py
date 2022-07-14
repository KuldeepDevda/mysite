from django.urls import path
from core import views
from .views import SignUp, PostCreateView, HomeView

app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('login/', views.LoginView.as_view(), name='login'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('create/', views.PostCreateView.as_view(), name='image'),
    ]
