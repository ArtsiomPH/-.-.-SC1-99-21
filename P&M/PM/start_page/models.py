import datetime
from django.db import models


class Medcine(models.Model):
    international_name = models.CharField(max_length=50, verbose_name="МНН")
    general_info = models.TextField(null=True, blank=True, verbose_name="Информация")
    general_sources = models.TextField(null=True, blank=True, verbose_name="Литература")
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата публикации")
    general_documentation = models.URLField(null=True, blank=True, verbose_name="Ссылка на документацию")
    class Meta:
        verbose_name_plural = "Препараты"
        verbose_name = "Препарат"
        ordering = ["international_name"]
    def __str__(self):
        return self.international_name


class Synonyms(models.Model):
    medcine = models.ForeignKey(Medcine, on_delete=models.PROTECT, verbose_name="Международное наименование")
    comm_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Торговое наименование")
    info = models.TextField(null=True, blank=True, verbose_name="Информация")
    documentation = models.URLField(null=True, blank=True, verbose_name="Ссылка на документацию")
    sources = models.TextField(null=True, blank=True, verbose_name="Литература")
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата публикации")
    class Meta:
        verbose_name_plural = "Синонимы"
        verbose_name = "Синоним"
        ordering = ["comm_name"]
    def __str__(self):
        return self.comm_name


