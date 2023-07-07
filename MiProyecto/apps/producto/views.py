from django.shortcuts import render, redirect
from . import models
from django.template import context
from . import forms

# Create your views here.
def index (request):
    return render(request, 'producto/index.html')

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    template_name = 'producto/producto_categoria_list.html'
    context_object_name = 'categorias'


def producto_categoria_list(request):
    categorias=models.ProductoCategoria.objects.all()
    context={'categorias':categorias}
    return render(request, 'producto/producto_categoria_list.html', context)

def producto_categoria_pedido(request):
    if request.method =='POST':
      form = forms.ProductoCategoriaForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect ('producto:index')
    else:
        form= forms.ProductoCategoriaForm()
    return render(request, 'producto/producto_categoria_pedido.html', {'form':form})

def producto_categoria_delete(request,id):
    categoria=models.ProductoCategoria.objects.get(id=id)
    if request.method=='POST':
        categoria.delete()
        return redirect('producto:index')
    return render(request, 'producto/producto_categoria_delete.html',{'categoria': categoria})

def producto_categoria_update(request,id):
    categoria=models.ProductoCategoria.objects.get(id=id)
    if request.method =='POST':
      form = forms.ProductoCategoriaForm(request.POST,instance=categoria)
      if form.is_valid():
          form.save()
          return redirect ('producto:index')
    else:
        form= forms.ProductoCategoriaForm(instance=categoria)
    return render(request, 'producto/producto_categoria_update.html', {'form':form})
