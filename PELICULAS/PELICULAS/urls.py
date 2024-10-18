"""
URL configuration for PELICULAS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from moduloPeliculas import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PeliculaListView, name='pelicula-list'),  
    path('agregarpelicula/', views.agregar_pelicula, name='agregarpelicula'),
    path('<int:id>/', views.pelicula_detail, name='pelicula-detail'),
    path('editar/<int:id>/', views.editar_pelicula, name='editar-pelicula'),
    path('eliminar/<int:id>/', views.eliminar_pelicula, name='eliminar-pelicula'),
    path('gestionpeliculas/', views.PeliculaListCrud, name='gestion_peliculas'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)