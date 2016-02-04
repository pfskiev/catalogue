from django.views import generic
from chart.models import Article


class IndexView(generic.ListView):
    template_name = 'chart/partials/home.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class CatalogueView(generic.ListView):
    template_name = 'chart/partials/catalogue.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class ProductView(generic.ListView):
    template_name = 'chart/partials/product.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class AboutView(generic.ListView):
    template_name = 'chart/partials/about.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class CooperationView(generic.ListView):
    template_name = 'chart/partials/cooperation.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class BrandsView(generic.ListView):
    template_name = 'chart/partials/brands.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class CertificateView(generic.ListView):
    template_name = 'chart/partials/certificates.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class ArticleView(generic.ListView):
    template_name = 'chart/partials/articles.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class MapView(generic.ListView):
    template_name = 'chart/partials/map.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class ContactView(generic.ListView):
    template_name = 'chart/partials/contact.html'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]