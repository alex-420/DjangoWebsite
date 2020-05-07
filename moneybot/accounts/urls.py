from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
# auth_views has been used to seperate the login and logout views from the project views. this keeps it more secure.

app_name = 'accounts'

# The URL patterns below are class based and map where the user will be sent when selecting an option.
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('registeruser/',views.RegisterUser.as_view(), name='register')
]
