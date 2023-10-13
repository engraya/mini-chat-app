from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from socialApp import views
urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('social/', include('socialApp.urls')),  
    path('', views.home, name='home'),  
    path('', include('userApp.urls')), 
    path('chat/', include('chatApp.urls')), 

]  + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('social/', include('socialApp.urls')),  
    path('', views.home, name='home'),  
    path('', include('userApp.urls')), 
    path('chat/', include('chatApp.urls')), 

)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)