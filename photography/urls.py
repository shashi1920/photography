"""photography URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','pankpix.views.homepage'),
    url(r'^about_us/$','pankpix.views.about_us'),
    url(r'^gallery/$','pankpix.views.gallery'),
    url(r'^personal_album/$','pankpix.views.dashboard'),
    url(r'^contact_us/$','pankpix.views.contact_us'),
    url(r'^login/$','pankpix.views.login_view'),
    url(r'^logout/$','pankpix.views.logout_user'),
    url(r'^login/submit/$','pankpix.views.login_user'),
    url(r'^contact_us/submit/$','pankpix.views.contact_mail'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT})



]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))



