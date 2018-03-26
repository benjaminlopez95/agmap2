from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as fields_models


admin.site.register(fields_models.FieldPlot, LeafletGeoAdmin)
