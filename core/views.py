from django.shortcuts import render
from django.views.generic import TemplateView
from core.models.portfolio import *
from core.models.services import *
from core.models.home import *
# Create your views here.


def main_page(request):
    stats = StatsModel.objects.all()
    categories = PartnerCategoryModel.objects.all()
    partners = PartnersModel.objects.all()

    services1 = ServicesModel.objects.all()[0]
    services2 = ServicesModel.objects.all()[1]
    services3 = ServicesModel.objects.all()[2]
    services4 = ServicesModel.objects.all()[3]
    services5 = ServicesModel.objects.all()[4]
    services6 = ServicesModel.objects.all()[5]

    portfolios1 = PortfolioModel.objects.all()[0]
    portfolios2 = PortfolioModel.objects.all()[1]
    portfolios3 = PortfolioModel.objects.all()[2]
    portfolios4 = PortfolioModel.objects.all()[3]
    portfolios5 = PortfolioModel.objects.all()[4]
    portfolios6 = PortfolioModel.objects.all()[5]

    context = {
        'stats': stats,
        'categories': categories,
        'partners': partners,

        'services1': services1,
        'services2': services2,
        'services3': services3,
        'services4': services4,
        'services5': services5,
        'services6': services6,

        'portfolios1': portfolios1,
        'portfolios2': portfolios2,
        'portfolios3': portfolios3,
        'portfolios4': portfolios4,
        'portfolios5': portfolios5,
        'portfolios6': portfolios6,

    }

    return render(request,'core_pages/home.html', context)


class MainView(TemplateView):
    template_name = 'core_pages/index.html'