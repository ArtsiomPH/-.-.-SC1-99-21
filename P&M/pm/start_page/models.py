from django.db import models
from django.utils import timezone
from django.urls import reverse



class Medcine(models.Model):
    international_name = models.CharField(max_length=300, verbose_name="МНН", unique=True)
    general_url_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Название для URL")
    general_info = models.TextField(null=True, blank=True, verbose_name="Информация")
    formula = models.ImageField(upload_to="formulas/%Y/%m/%d", blank=True, verbose_name="Химическая формула")
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name="Дата публикации")
    pub_update = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата изменения")
    general_documentation = models.URLField(blank=True, null=True, verbose_name="Ссылка на документацию")

    class Meta:
        verbose_name_plural = "Препараты"
        verbose_name = "Препарат"
        ordering = ["international_name"]

    def __str__(self):
        return self.international_name


class Synonyms(models.Model):
    medcine = models.ForeignKey(Medcine, on_delete=models.CASCADE, verbose_name="Международное наименование")
    comm_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Торговое наименование")
    url_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Название для URL")
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name="Дата публикации")
    pub_update = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name_plural = "Синонимы"
        verbose_name = "Синоним"
        ordering = ["comm_name"]

    def __str__(self):
        return self.comm_name

    def get_absolute_url(self):
        return reverse("start_page:search_param", kwargs={"url_name": self.url_name})

class General_sources(models.Model):
    medcine = models.ForeignKey(Medcine, on_delete=models.CASCADE, verbose_name="МНН")
    source_name = models.CharField(max_length=500, null=True, blank=True, verbose_name="Название источника")

    class Meta:
        verbose_name_plural = "Источники"
        verbose_name = "Источник"
        ordering = ["source_name"]

    def __str__(self):
        return self.source_name

class Request_counter(models.Model):
    synonym = models.ForeignKey(Synonyms, on_delete=models.CASCADE, verbose_name="Синоним")
    count = models.PositiveIntegerField(default=0, verbose_name="Число запросов")
    date = models.DateField(default=timezone.now, verbose_name="Дата запроса")

    class Meta:
        verbose_name_plural = "Запросы"
        verbose_name = "Запрос"
        ordering = ["-date"]

    def __str__(self):
        return self.synonym.comm_name


