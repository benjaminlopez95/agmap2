from django.contrib import admin
from .models import Field, Grower, Ranch, Commodity, PCA, Shipper


class FieldAdmin(admin.ModelAdmin):
    list_display = ('lot', 'ranch', '_range', 'township', 'section', 'commodity', 'grower', 'shipper', 'pca')
    list_filter = ('ranch', 'township', 'commodity',)

    search_fields = ('ranch__name', 'commodity__commodity', 'grower__name', )

    fieldsets = (
        (None, {
            'fields': ('ranch', 'lot', 'township', 'section', '_range',)
        }),

        ('Grower and Shipper', {
            'fields': ('grower', 'shipper', 'pca',)
        }),
        ('Field Info', {
            'fields': ('wet_date', 'acreage', 'bed_count', 'lines_per_bed', 'bed_configuration',)
        }),
        ('Crop Info', {
            'fields': ('commodity', 'variety',)
        }),
        (None, {
            'fields': ('user',)
        }),



    )

class GrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    list_filter = ('state', 'city')

class RanchAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    list_filter = ('state', 'city')

class PCAAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    list_filter = ('state', 'city')

class ShipperAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    list_filter = ('state', 'city')

admin.site.register(Field, FieldAdmin)
admin.site.register(Grower, GrowerAdmin)
admin.site.register(Ranch, RanchAdmin)
admin.site.register(Commodity)
admin.site.register(PCA, PCAAdmin)
admin.site.register(Shipper, ShipperAdmin)
