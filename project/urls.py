from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
# from django.contrib import admin

from core import views

# admin.autodiscover()

PREFIX = ''
urlpatterns = patterns(
    PREFIX,
    url(r'^$', views.IndexView.as_view(), name='test'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
