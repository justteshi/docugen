from django.contrib import admin
from .models import Proektant

# Register your models here.
@admin.register(Proektant)
class ProetantAdmin(admin.ModelAdmin):
    list_display = ('name',)