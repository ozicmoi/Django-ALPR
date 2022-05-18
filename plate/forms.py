from django import forms
from .models import Plate
class PlateForm(forms.ModelForm):
    class Meta:
        model=Plate
        fields=["plate","name","surname","content","car_image"]
    pass