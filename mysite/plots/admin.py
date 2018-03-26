from django.contrib import admin
from plots.models import Plot

class PlotsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'wet_date', 'grower')

admin.site.register(Plot)
