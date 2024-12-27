from django.db import models


class Recipe(models.Model):
    class Meta:
        # ordering = ('-time_for_cooking',) можно сортировку делать и во вью, и в моделе
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    title = models.CharField(max_length=250)
    description = models.TextField()
    steps_cooking = models.TextField()
    time_for_cooking = models.IntegerField(default=10)
    # favorites = models.BooleanField(default=False)
    def __str__(self):
        return self.title
