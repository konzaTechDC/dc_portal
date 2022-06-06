from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.app.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='index'),
    path('contact/', include('core.app.urls', namespace='core.app')),
    path('summernote/', include('django_summernote.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
