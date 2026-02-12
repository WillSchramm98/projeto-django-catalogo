from django.contrib import admin
from .models import Questao, Alternativa


class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2


@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    inlines = [AlternativaInline]
