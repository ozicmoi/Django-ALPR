from django.contrib import admin
from django.urls import path,include
from plate import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('process/', views.process, name="process"),
    path('plates/', views.plates,name="plates"),
    path('user/', include("user.urls")),
    path('plates/',include("plate.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

