from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id"]

#class ClienteForm(forms.ModelForm):
 #   class Meta:
  #      model = Pais
   #     fields = '__all__'