from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from . import settings
urlpatterns = [
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
