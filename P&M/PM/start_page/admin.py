from django.contrib import admin
from .models import Medcine, Synonyms


# Register your models here.
@admin.register(Medcine)
class MedcineAdmin(admin.ModelAdmin):
    list_display = ["international_name", "general_info", "general_sources", "general_url_name", "general_documentation", "pub_date"]
    list_display_links = ["international_name"]
    search_fields = ["international_name", "pub_date"]

@admin.register(Synonyms)
class SynonymsAdmin(admin.ModelAdmin):
    list_display = ["comm_name", "url_name", "medcine", "pub_date"]
    list_display_links = ["comm_name"]
    search_fields = ["comm_name", "medcine__international_name"]

