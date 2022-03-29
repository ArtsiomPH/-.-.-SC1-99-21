from django.db import models

class Medcine(models.Model):
    international_name = models.CharField(max_length=50)
    info = models.TextField()
    sources = models.TextField()



class Synonyms(models.Model):
    name = models.CharField(max_length=50)
    documentation = models.URLField()
    medcine = models.ForeignKey(Medcine, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


