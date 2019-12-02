from . import views
from django.urls import path, include
from rest_framework.authtoken import views as rest_views
from rest_framework.routers import url

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


#app_name= 'one_liner'
urlpatterns += [
    path('', views.IndexView.as_view(), name='index'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('updates/', views.UpdatesList.as_view())
]

urlpatterns += [
    url(r'^api-token-auth/', rest_views.obtain_auth_token),
]
