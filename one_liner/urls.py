from django.urls import path

from . import views

app_name= 'one_liner'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]