from djgeojson.fields import PolygonField
from django.db import models


class FieldPlot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    geom = PolygonField()

    def __unicode__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url
