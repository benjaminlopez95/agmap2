from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from home.views import HomeView
from django.views.generic import TemplateView

from .models import FieldPlot


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
