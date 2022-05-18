from django.contrib import admin
from plate.models import Plate

from django.contrib.auth.models import User
# Register your models here.

@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ["plate","name","surname","content","created_date"]  #Diğer özellikleri gösterme
    search_fields = ["plate"]
    list_display_links = ["content"]
    list_filter = ["created_date"]
    class Meta: #Django tarafından verilern özellik
        model=Plate