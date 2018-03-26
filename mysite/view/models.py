from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Field(models.Model):
    ranch = models.ForeignKey('Ranch',on_delete=models.SET_NULL, null= True, max_length=100, default='')
    lot = models.CharField(max_length=100)
    _range = models.IntegerField(verbose_name="Range")
    section = models.IntegerField()
    township = models.CharField(max_length=100)
    grower = models.ForeignKey('Grower', on_delete=models.SET_NULL, null = True)
    shipper = models.ForeignKey('Shipper',on_delete=models.SET_NULL, null= True, max_length=100)
    pca = models.ForeignKey('PCA', on_delete=models.SET_NULL, null= True, max_length=100, verbose_name="PCA")
    wet_date = models.DateField()
    commodity = models.ForeignKey('Commodity', on_delete=models.SET_NULL, null= True, max_length=100)
    variety = models.CharField(default='', max_length=100)
    acreage = models.IntegerField()
    bed_count = models.IntegerField()
    lines_per_bed = models.IntegerField()
    bed_configuration = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["ranch", "lot"]

    def __str__(self):
        return '{0}, {1}'.format(self.ranch, self.lot)

    def get_absolute_url(self):
        return reverse('field-detail', args=[str(self.ranch, self.lot)])

class Ranch(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default = '')
    state = models.CharField(max_length=2, default = '')

    class Meta:
        ordering = ["state", "name", "city"]
        verbose_name_plural = "Ranches"


    def get_absolute_url(self):
        return reverse('ranch-details', args=[str(self.name)])

    def __str__(self):
        return self.name

class Grower(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)

    class Meta:
        ordering = ["state", "name", "city"]

    def get_absolute_url(self):
        return reverse('grower-details', args=[str(self.name)])

    def __str__(self):
        return self.name

class Shipper(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)

    class Meta:
        ordering = ["state", "name", "city"]

    def get_absolute_url(self):
        return reverse('shipper-details', args=[str(self.name)])

    def __str__(self):
        return self.name

class PCA(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)

    class Meta:
        ordering = ["state", "name", "city"]
        verbose_name_plural = "PCAs"

    def get_absolute_url(self):
        return reverse('pca-details', args=[str(self.name)])

    def __str__(self):
        return self.name

class Commodity(models.Model):
    commodity = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Commodities"

    def __str__(self):
        return self.commodity
