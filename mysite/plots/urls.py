from django.conf.urls import url
from plots.views import CreateNewPlotView, PlotView

urlpatterns = [
    url(r'^create/$', CreateNewPlotView.as_view(), name='plots'),
    url(r'^create-map/$', PlotView.as_view(), name='plotview'),
]
