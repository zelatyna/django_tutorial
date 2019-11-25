from django.urls import path, include
from django.conf.urls import url

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'one_liner_txt', views.updates_list)
router.register(r'users', views.UserViewSet)



app_name= 'one_liner'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('updates/', views.UpdatesList.as_view())
]