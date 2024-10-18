from django import forms
from .models import Pelicula
from datetime import date

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['sucursal', 'nombre', 'genero', 'clasificacion', 'duracion', 
                  'resena', 'sala', 'fecha_exhibicion', 'hora_exhibicion', 'valor_ticket', 'imagen']
        widgets = {
            'sucursal': forms.Select(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la pelicula'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'clasificacion': forms.Select(attrs={'class':'form-control'}),
            'duracion': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Tiempo de duración en minutos'}),
            'resena': forms.Textarea(attrs={'class':'form-control', 'rows' : 3, 'placeholder':'Breve reseña del contenido de la pelicula'}),
            'sala': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Sala en la que se exhibe'}),
            'fecha_exhibicion': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'hora_exhibicion': forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'valor_ticket': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Valor del ticket'}),
            'imagen': forms.ClearableFileInput(attrs={'accept':'image/*', 'directory': 'peliculas'}),
        }

    def clean_salas(self):
        sala = self.cleaned_data['sala']
        if sala < 1 or sala > 15:
            raise forms.ValidationError("El número de sala debe estar entre 1 y 15")
        return sala
    
    def clean_fecha_exhibicion(self):
        fecha_exhibicion = self.cleaned_data['fecha_exhibicion']
        if fecha_exhibicion <= date.today():
            raise forms.ValidationError("La fecha de exhibición debe ser posterior a la fecha actual")
        return fecha_exhibicion