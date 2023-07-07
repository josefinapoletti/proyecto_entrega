from django.contrib import admin

# Register your models here.
from .models import Cliente, Pais
admin.site.register(Cliente)
admin.site.register(Pais)

