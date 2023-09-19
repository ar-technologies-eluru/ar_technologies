from django.urls import path,include
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homepage),
    path('about',about),
    path('service',service),
    path('contact',contact),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)