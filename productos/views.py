from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from categorias.models import Categoria

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar.html', {'productos': productos})

def crear_producto(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            categoria_id=request.POST['categoria'],
            stock=request.POST['stock']
        )
        return redirect('listar_productos')

    return render(request, 'productos/crear.html', {'categorias': categorias})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.categoria_id = request.POST['categoria']
        producto.stock = request.POST['stock']
        producto.save()

        return redirect('listar_productos')

    return render(request, 'productos/editar.html', {'producto': producto, 'categorias': categorias})
