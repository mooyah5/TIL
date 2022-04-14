from django.urls import path
from . import views


app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
]
