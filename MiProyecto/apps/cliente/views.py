from django.shortcuts import render, redirect
from .models import Cliente, Pais

# Create your views here.
def index(request):
    clientes_registro= Cliente.objects.all()
    datos= {'clientes': clientes_registro}
    return render(request, 'cliente/index_cliente.html', datos)


def crear_clientes_predeterminados(request): 
    from datetime import date 
    #crear instancias de paises
    p1=Pais.objects.create(nombre="colombia")
    p2=Pais.objects.create(nombre='EStados Unidos')
    p3=Pais.objects.create(nombre='Argentina')

    #crear clientes
    Cliente.objects.create(nombre='Almendra',apellido="Ruisenor", nacimiento=date(2015,1,1),pais_origen_id=p1)
    Cliente.objects.create(nombre='Martina',apellido="Martinez", nacimiento=date(2008,7,3),pais_origen_id=None)
    Cliente.objects.create(nombre='Julian',apellido="Alvarez", nacimiento=date(2000,1,31),pais_origen_id=None)
    Cliente.objects.create(nombre='Aldana',apellido="Gonzalez", nacimiento=date(2004,7,4),pais_origen_id=p2)

    #return render(request, 'cliente/index_cliente.html')
    return redirect('cliente:index')

def prueba_busqueda(request):
    from datetime import date 
    contexto={}
    #busqueda por nombre que contenga "dana"
    clientes_nombre = Cliente.objects.filter(nombre__contains="dana")
    contexto['clientes_nombre']= clientes_nombre
    
    #busqueda por fecha de nacimiento mayor a 2000
    clientes_nacimiento = Cliente.objects.filter(nacimiento__gte=date(2000,1,1))   
    contexto['clientes_nacimiento']= clientes_nacimiento
    

    #busqueda por cliente que no tenga pais
    clientes_sin_pais = Cliente.objects.filter(pais_origen_id=None)
    contexto['clientes_sin_pais']= clientes_sin_pais
    
    return render(request, 'cliente/resultado_busqueda.html', contexto)

def crear_cliente(request):
    from .forms import ClienteForm 
    if request.method == 'POST':
        form= ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:index')
    else: #method==GET
        form= ClienteForm()
    return render(request, 'cliente/crear.html',{'form':form})