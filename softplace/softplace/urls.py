from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import urls
from item import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('item/', include('item.urls'))

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
