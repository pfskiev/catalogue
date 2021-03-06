"""catalogue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from chart import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^(?P<pk>[0-9]+)/edit/$', views.Edit.as_view(), name='edit'),

    url(r'^catalogue/$', views.catalogue, name='catalogue'),
    url(r'^catalogue/(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^product/$', views.ProductView.as_view(), name='product'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^cooperation/$', views.cooperation_listing, name='cooperation'),
    url(r'^brands/$', views.BrandsView.as_view(), name='brands'),
    url(r'^certificates/$', views.CertificateView.as_view(), name='certificates'),
    url(r'^articles/$', views.ArticleView.as_view(), name='article'),
    url(r'^map/$', views.MapView.as_view(), name='map'),
    url(r'^contacts/$', views.ContactView.as_view(), name='contact'),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^brands/(?P<pk>[0-9]+)/$', views.BrandsDetailView.as_view(), name='detail'),
    url(r'^certificates/(?P<pk>[0-9]+)/$', views.CertificatesDetailView.as_view(), name='detail'),
    url(r'^accounts/', include('registration.backends.hmac.urls'))

]

urlpatterns = format_suffix_patterns(urlpatterns)
