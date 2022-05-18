from django.db import models

# Create your models here.

class Plate(models.Model):
    attendant=models.ForeignKey("auth.user",on_delete=models.CASCADE)       #Eğer bir kullanıcı silinirse ona ait tüm plakalar ve veriler yok olur.
    plate=models.CharField(max_length=10) #Başlık oluşturma,max uzunluk 50 karakter
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    content=models.CharField(max_length=50) #Başlık oluşturma,max uzunluk 50 karakter
    created_date=models.DateTimeField(auto_now_add=True)
    car_image=models.FileField(blank=True,null=True,verbose_name="Araç Fotoğrafı Yükleyiniz.")

    def __str__(self):
        return self.plate