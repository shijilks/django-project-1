from django.urls import path
from .views import page1, page2
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('page1/', page1, name='page1'),
    path('page2/', page2, name='page2'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)