from django.db import models
from django.contrib.auth.models import User


class Plot(models.Model):
    ranch = models.CharField(max_length=100)
    _range = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    township = models.CharField(max_length=100)
    grower = models.CharField(max_length=100)
    shipper = models.CharField(max_length=100)
    pca = models.CharField(max_length=100)
    wet_date = models.DateField()
    commodity = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    acreage = models.IntegerField()
    bed_count = models.IntegerField()
    lines_per_bed = models.IntegerField()
    bed_configuration = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.section
