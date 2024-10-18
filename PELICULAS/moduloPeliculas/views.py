from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula
from .forms import PeliculaForm
from django.contrib import messages

# Create your views here.

def PeliculaListView(request):
    peliculas = Pelicula.objects.all()
    peliculas = peliculas.order_by('nombre')
    peliculas = {"peliculas":peliculas}
    return render(request, "peliculas_list.html", peliculas)

def PeliculaListCrud(request):
    peliculas = Pelicula.objects.all()
    peliculas = peliculas.order_by('nombre')
    peliculas = {"peliculas":peliculas}
    return render(request, "peliculas_crud.html", peliculas)

def pelicula_detail(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'pelicula_details.html', {'pelicula': pelicula}) 

def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #redirige a la vista lista_articulos
            return PeliculaListView(request)
    else:
        form = PeliculaForm()
    return render(request, 'pelicula_form.html', {'form': form})

def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    # Agrega un mensaje de confirmación
    messages.success(request, f'Se haeliminado a {pelicula.nombre}')
    return redirect('pelicula-list')

def editar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            print('Formulario válido. Película guardada.')
            return redirect('pelicula-list') 
        else:
            print('Formulario no inválido. Errores:', form.errors)
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'pelicula_form.html', {'form': form})

