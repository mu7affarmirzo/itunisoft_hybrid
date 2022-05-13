from django.urls import path

from core.views import main_page

app_name = "core"

urlpatterns = [
    path('', main_page, name='home'),

]
