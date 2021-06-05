"""kayaccounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps import views
from django.views.decorators.cache import cache_page
from django.urls import path, include, re_path
from kayaccounting.sitemaps import StaticViewSitemap
from main.views import (
    AboutView, ContactView, HomeView, PrivacyView, ServicesView, TermsView, ComingSoonView
)

handler404 = 'main.views.error_404'


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # path('test/', HomeView.as_view(), name='home'),
    # path('test/about/', cache_page(120)(AboutView.as_view()), name='about'),
    # path('test/services/', cache_page(120)(ServicesView.as_view()), name='services'),
    # path('test/contact/', ContactView.as_view(), name='contact'),
    # path('test/privacy/', cache_page(120)(PrivacyView.as_view()), name='privacy'),
    # path('test/terms/', cache_page(120)(TermsView.as_view()), name='terms'),

    # re_path(r'^', ComingSoonView.as_view(), name='coming-soon'),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('about/', cache_page(120)(AboutView.as_view()), name='about'),
    path('services/', cache_page(120)(ServicesView.as_view()), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('privacy/', cache_page(120)(PrivacyView.as_view()), name='privacy'),
    path('terms/', cache_page(120)(TermsView.as_view()), name='terms'),

    path('sitemap.xml', views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]