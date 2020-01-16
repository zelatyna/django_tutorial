from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('one_liner/', include('one_liner.urls')),
    path('admin/', admin.site.urls),

]
