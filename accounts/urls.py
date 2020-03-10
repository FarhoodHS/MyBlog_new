from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signin/', views.login, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
