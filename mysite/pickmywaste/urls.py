from django.urls import path

from . import views

from .models import Donators

urlpatterns = [
    path('', views.index, name='index'),
    path('foodMap/', views.foodMap, name='foodMap'),
    path('create/', views.create, name='create'),

    # path('<int:donator_id>/', views.food, name='food'),
    # ex: /polls/5/results/
    #look for some interger in the path, 
    path('<int:donator_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:donator_id>/take/', views.take, name='take'),
    # path('specifics/<int:donator_id>/', views.detail, name='detail'),

]