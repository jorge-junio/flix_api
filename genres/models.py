from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

    def __str__(self):
        return self.name
