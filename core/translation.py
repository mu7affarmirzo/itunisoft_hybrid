from modeltranslation.translator import register, TranslationOptions
from core.models.home import *
from core.models.services import *
from core.models.portfolio import *
from core.models.about import *


@register(PartnerCategoryModel)
class PartnerCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(StatsModel)
class StatsTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(InfoPageModel)
class InfoPageTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(PortfolioModel)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(ServicesModel)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(AboutInfoModel)
class AboutInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(VacancyModel)
class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
