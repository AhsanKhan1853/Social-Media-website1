from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.profile, name='profile')

    # path('login/',auth_views.LoginView.as_view(template_name='/users/login.html'),name='login')
]
