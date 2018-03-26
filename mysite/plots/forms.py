from django import forms
from plots.models import Plot

class CreateNewPlotForm(forms.ModelForm):
    ranch = forms.CharField
    _range = forms.CharField()
    section = forms.CharField()
    township = forms.CharField()
    grower = forms.CharField()
    shipper = forms.CharField()
    pca = forms.CharField()
    wet_date = forms.DateField(widget = forms.SelectDateWidget)
    commodity = forms.CharField()
    variety = forms.CharField()
    acreage = forms.IntegerField()
    bed_count = forms.IntegerField()
    lines_per_bed = forms.IntegerField()
    bed_configuration = forms.CharField()

    class Meta:
        model = Plot
        fields = ('ranch','_range', 'section', 'township', 'grower', 'shipper', 'pca', 'wet_date', 'commodity',
        'variety', 'acreage', 'bed_count', 'lines_per_bed', 'bed_configuration',)
