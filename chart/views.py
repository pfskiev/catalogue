from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
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


def cooperation_listing(request):
    queryset_list = Cooperation.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                Q(paragraph__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 10)  # Show 10 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "Сотрудничество",
        "page_request_var": page_request_var,
    }
    return render(request, "chart/partials/cooperation.html", context)


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
