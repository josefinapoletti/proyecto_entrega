from django.db import models

# Create your models here.
class ProductoCategoria(models.Model):
    nombre= models.CharField(max_length=100,unique=True)
    descripcion=models.CharField(max_length=250,null=True,blank=True )

    class Meta:
        verbose_name = 'Categoria de productos'
        verbose_name_plural='Categorias de productos'
    def __str__(self) :
        return self.nombre
