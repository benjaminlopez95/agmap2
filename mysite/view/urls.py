from django.conf.urls import url
from view.views import FieldListView

urlpatterns = [
    url(r'^list/', FieldListView.as_view(), name='agfields'),
]
