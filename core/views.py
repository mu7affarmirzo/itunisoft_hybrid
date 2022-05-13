from django.shortcuts import render
from django.views.generic import TemplateView
from core.models.portfolio import *
from core.models.services import *
from core.models.home import *
# Create your views here.


def main_page(request):
    carousel = CarouselModel.objects.all()
    stats = StatsModel.objects.all()
    services = ServicesModel.objects.all()
    portfolios = PortfolioModel.objects.all()

    context = {
        'carousel': carousel,
        'stats': stats,
        'services': services,
        'portfolios': portfolios

    }

    return render(request,'core_pages/home.html', context)


class MainView(TemplateView):
    template_name = 'core_pages/index.html'