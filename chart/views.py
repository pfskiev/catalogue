from django.views import generic
from chart.models import Article


class IndexView(generic.ListView):
    template_name = 'chart/partials/home.html'

    def get_queryset(self):
        return Article.objects.all()
