from django.db import models


class Recipe(models.Model):
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    title = models.CharField(max_length=250)
    description = models.TextField()
    steps_cooking = models.TextField()
    time_for_cooking = models.IntegerField(default=10)

    def __str__(self):
        return self.title
