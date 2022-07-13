from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Food Blog'
admin.site.site_title = 'Food Blog'
admin.site.index_title = 'Food Blog Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('editor/', include('django_summernote.urls')),
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)