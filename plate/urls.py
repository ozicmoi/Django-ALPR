from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="plate"
urlpatterns=[
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addplate/', views.addPlate, name="addplate"),
    path('plate/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.updatePlate, name="update"),
    path('delete/<int:id>', views.deletePlate, name="delete"),

]