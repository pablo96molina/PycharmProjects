from django.urls import path
from . import views
""" from snipcartwagtaildemo.home.views import canjear
from mysite.snipcartwagtaildemo.home import views as views_tienda """

# import snipcartwagtaildemo.home.views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('tienda/', views.tienda, name='tienda'),
    path('saldo/<int:id_user>/<int:saldo>/', views.saldo, name='saldo'),
    #path('/<int:id>/canjear', canjear)
    # path('<int:page_ptr_id>/canjear/', snipcartwagtaildemo.home.views.canjear, name='canjear'),

]