from django.shortcuts import render
from django.views import generic
from view.models import Field

class FieldListView(generic.ListView):
    model = Field
    template_name = 'view/agfield_list.html'
