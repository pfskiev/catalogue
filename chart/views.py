from django.views import generic
from django.views.generic import ListView

from chart.models import Article, Catalogue, Product, About, Cooperation, Brand, Certificate, Map, Contact, Menu


class IndexView(generic.ListView):
    template_name = 'chart/partials/home.html'

    def get_queryset(self):
        return Menu.objects.order_by('title')[:100]


class CatalogueView(ListView):
    queryset = Catalogue.objects.order_by('title')[:100]
    template_name = 'chart/partials/catalogue.html'
    context_object_name = 'object_list'
    paginate_by = 3


class ProductView(generic.ListView):
    template_name = 'chart/partials/product.html'

    def get_queryset(self):
        return Product.objects.order_by('title')[:100]


class AboutView(generic.ListView):
    template_name = 'chart/partials/about.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return About.objects.order_by('paragraph')[:100]


class CooperationView(generic.ListView):
    template_name = 'chart/partials/cooperation.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Cooperation.objects.order_by('paragraph')[:100]


class BrandsView(generic.ListView):
    template_name = 'chart/partials/brands.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Brand.objects.order_by('title')[:100]


class CertificateView(generic.ListView):
    template_name = 'chart/partials/certificates.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Certificate.objects.order_by('title')[:100]


class ArticleView(generic.ListView):
    template_name = 'chart/partials/articles.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Article.objects.order_by('title')[:100]


class MapView(generic.ListView):
    template_name = 'chart/partials/map.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Map.objects.order_by('title')[:100]


class ContactView(generic.ListView):
    template_name = 'chart/partials/contact.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Contact.objects.order_by('title')[:100]


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'chart/partials/detail.html'
    context_object_name = 'object'


class BrandsDetailView(generic.DetailView):
    model = Brand
    template_name = 'chart/partials/detail.html'
    context_object_name = 'object'


class CertificatesDetailView(generic.DetailView):
    model = Certificate
    template_name = 'chart/partials/detail.html'
    context_object_name = 'object'


class ProductDetailView(generic.DetailView):
    model = Catalogue
    template_name = 'chart/partials/product.html'
    context_object_name = 'object_list'


class NavView(generic.DetailView):
    model = Menu
    template_name = 'chart/templates/nav-test.html'
    context_object_name = 'object_list'
