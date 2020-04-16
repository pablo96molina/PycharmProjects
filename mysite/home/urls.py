from django.urls import path
from . import views
from snipcartwagtaildemo.home.models import canjear

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('tienda/', views.tienda, name='tienda'),
    #path('/<int:id>/canjear', canjear)
]