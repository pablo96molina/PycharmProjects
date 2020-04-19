from django.urls import path
from . import views

app_name = 'polls'

#Desde aca se definen los url, se combierten los datos tomados del url a enteros ya que los datos sacados del url se obtienen como string

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
