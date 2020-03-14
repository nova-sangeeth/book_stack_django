from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    pages = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
