from django.contrib import admin
from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "BachatBazar"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "devloped by Ashutosh patil"

urlpatterns = [
    path("",views.index, name='Home'),
    path("about",views.about, name='Home'),
    path("contact",views.contact, name='Home'),
    path("services",views.services, name='Home'),
    path("sell",views.sell, name='Home')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)