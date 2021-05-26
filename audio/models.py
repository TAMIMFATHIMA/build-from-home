from django.db import models

# Create your models here.
class audio(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=2500)
    

class Audio_store(models.Model):
    record=models.FileField(upload_to='documents/')
    class Meta:
        db_table='Audio_store'