from django.urls import path
from . import views

app_name= 'chessCalc'
urlpatterns = [
    path('calc', views.elo_calculator, name='calculator'),
    path('result', views.results, name='results')
    ]