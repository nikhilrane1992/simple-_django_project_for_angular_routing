from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homepage/','angular_routing.views.home_page'),
)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
