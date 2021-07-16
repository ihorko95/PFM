from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Transactions(models.Model):
    title = models.CharField(max_length=80, db_index=True)
    slug = models.SlugField(max_length=80, unique=True)
    category = models.ManyToManyField('Categories', blank=True, related_name='gifts')
    total = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=150, blank=True, db_index=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
    def get_absolute_url(self):
        return reverse('transactions_list_url', kwargs={'slag': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

class Categories(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField(max_length=150, blank=True)

    def get_absolute_url(self):
        return reverse('category_details_url', kwargs={'slag': self.slug})

    def __str__(self):
        return '{}'.format(self.title)




