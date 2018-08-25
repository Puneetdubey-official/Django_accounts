from django.conf.urls import url, include
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.login_redirect, name='name_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^home/', include('home.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
