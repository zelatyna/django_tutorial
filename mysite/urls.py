from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import url


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('one_liner/', include('one_liner.urls')),
    path('admin/', admin.site.urls),

]
# urlpatterns += patterns('',
#
#     url(r'^api-auth/', include('rest_framework.urls',
#
#                                namespace='rest_framework')),
# )
from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)