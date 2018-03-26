from django.conf.urls import url, include
from django.contrib import admin
from mysite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name = 'login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^plots/', include('plots.urls')),
    url(r'^view/', include('view.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
