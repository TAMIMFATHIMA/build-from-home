from django.contrib import admin
from . models import audio 

class AudioAdmin(admin.ModelAdmin):
    list_display = ('name','image')

# Register your models here.
admin.site.register(audio,AudioAdmin)
