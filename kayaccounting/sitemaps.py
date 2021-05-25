from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'services', 'contact', 'privacy', 'terms']

    def location(self, item):
        return reverse(item)
