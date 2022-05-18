from django.contrib import admin
from core.models import home, portfolio, services, about

from modeltranslation.admin import TranslationAdmin


class PartnerCategoryCustomAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'name_en', 'name_ru')

    class Meta:
        verbose_name = "Partner Category"


@admin.register(home.PartnerCategoryModel)
class PartnerCategoryAdmin(PartnerCategoryCustomAdmin, TranslationAdmin):
    pass


# class InfoPageCustomAdmin(admin.ModelAdmin):
#     list_display = ('title_uz', 'title_en', 'title_ru')
#
#     class Meta:
#         verbose_name = "Info Page"
#
#
# @admin.register(home.InfoPageModel)
# class InfoPageAdmin(InfoPageCustomAdmin, TranslationAdmin):
#     pass


class StatsCustomAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Stats Page"


@admin.register(home.StatsModel)
class StatsAdmin(StatsCustomAdmin, TranslationAdmin):
    pass


admin.site.register(home.PartnersModel)


class PortfolioCustomAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Portfolio"


@admin.register(portfolio.PortfolioModel)
class PortfolioAdmin(PortfolioCustomAdmin, TranslationAdmin):
    pass


class ServicesCustomAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Services"


@admin.register(services.ServicesModel)
class ServicesAdmin(ServicesCustomAdmin, TranslationAdmin):
    pass


class AboutInfoCustomAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "About Info"


@admin.register(about.AboutInfoModel)
class AboutInfoAdmin(AboutInfoCustomAdmin, TranslationAdmin):
    pass


admin.site.register(about.CertificatesModel)
admin.site.register(services.ProjectFormModel)


class VacancyCustomAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Vacancy"


@admin.register(about.VacancyModel)
class VacancyAdmin(VacancyCustomAdmin, TranslationAdmin):
    pass
