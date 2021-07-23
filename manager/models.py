from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Transactions(models.Model):
    title = models.CharField(max_length=80, db_index=True)
    slug = models.SlugField(max_length=80, unique=True)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=150, blank=True, db_index=True)
    date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('transaction_details_url', kwargs={'slug': self.slug})
    class Meta:
        verbose_name='Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ('-date',)


    def __str__(self):
        return self.title

class Categories(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField(max_length=150, blank=True)
    class Meta:
        verbose_name='Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('category_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title




