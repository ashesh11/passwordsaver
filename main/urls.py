from django.urls import path, include
from . import views

urlpatterns = [
    path('add_password', views.add_password, name='add-password'),
    path('see_password/', views.see_password, name='see-password'),
    path('', views.login_page, name='login-page'),
    path('logout/', views.logout_view, name='logout' ),
    path('register/', views.register_page, name='register-page'),
]