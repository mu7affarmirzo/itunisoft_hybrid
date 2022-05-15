from django.urls import path

from core.views import main_page, portfolio_page, about_us_page, PortfolioDetailView

app_name = "core"

urlpatterns = [
    path('', main_page, name='home'),
    path('about', about_us_page, name='about us'),
    path('portfolio', portfolio_page, name='portfolio'),
    path('portfolio/<int:pk>', PortfolioDetailView.as_view(), name='portfolio-detail'),

]
