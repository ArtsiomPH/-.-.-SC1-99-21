from django.utils import timezone
from django.db import models



class Medcine(models.Model):
    international_name = models.CharField(max_length=300, verbose_name="МНН", unique=True)
    general_url_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Название для URL")
    general_info = models.TextField(null=True, blank=True, verbose_name="Информация")
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    general_documentation = models.URLField(null=True, blank=True, verbose_name="Ссылка на документацию")
    class Meta:
        verbose_name_plural = "Препараты"
        verbose_name = "Препарат"
        ordering = ["international_name"]
    def __str__(self):
        return self.international_name


class Synonyms(models.Model):
    medcine = models.ForeignKey(Medcine, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Международное наименование")
    comm_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Торговое наименование")
    url_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Название для URL")
    pub_date = models.DateTimeField(auto_now=True, null=True, blank=True, db_index=True, verbose_name="Дата публикации")
    class Meta:
        verbose_name_plural = "Синонимы"
        verbose_name = "Синоним"
        ordering = ["comm_name"]
    def __str__(self):
        return self.comm_name

class General_sources(models.Model):
    medcine = models.ForeignKey(Medcine, on_delete=models.CASCADE, null=True, blank=True, verbose_name="МНН")
    source_name = models.CharField(max_length=300, null=True, blank=True, verbose_name="Название источника")
    class Meta:
        verbose_name_plural = "Источники"
        verbose_name = "Источник"
        ordering = ["source_name"]
    def __str__(self):
        return self.source_name

class Request_counter(models.Model):
    synonym = models.ForeignKey(Synonyms, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Синоним")
    count = models.PositiveIntegerField(default=0, verbose_name="Число запросов")
    date = models.DateField(default=timezone.now, verbose_name="Дата запроса")
    class Meta:
        verbose_name_plural = "Запросы"
        verbose_name = "Запрос"
        ordering = ["-date"]
    def __str__(self):
        return self.synonym.comm_name


