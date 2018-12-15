from django.conf.urls import url
# from .views import *
from django.conf.urls.static import static

urlpatterns = [

        url(r'^$', route, name="route"),
        url(r'^home-page/', home_page, name="home_page"),
        url(r'^users/', create_users, name="create_users"),
              
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
