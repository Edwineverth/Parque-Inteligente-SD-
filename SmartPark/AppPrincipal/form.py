from django import forms
from AppPrincipal.models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    is_superuser = forms.BooleanField(initial=True)
    is_staff = forms.BooleanField(required=True, initial=True)
    is_active = forms.BooleanField(required=True, initial=True)
    telefono = forms.CharField(max_length=10)
    parque = forms.ModelChoiceField(queryset=Parque.objects.all())

class UserEditForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    telefono = forms.CharField(max_length=10)
    #parque = forms.ModelChoiceField(queryset=Parque.objects.all())

class UserForm1(forms.ModelForm):
   class Meta:
      model = User
      fields =('username','email', 'password')

class UserForm2(forms.ModelForm):
  class Meta:
    model = User
    fields = '__all__' 

class ParqueForm(forms.ModelForm):
  class Meta:
    model = Parque
    fields = '__all__'

class DispositivoForm(forms.ModelForm):
   class Meta:
      model = Dispositivo
      fields ='__all__'

class TopicoForm(forms.ModelForm):
  class Meta:
    model = Topico
    fields = '__all__'

class TipoSensorForm(forms.ModelForm):
  class Meta:
    model = TipoSensor
    fields = '__all__'

class SensorForm(forms.ModelForm):
   class Meta:
      model = Sensor
      fields ='__all__'


class PublicidadForm(forms.ModelForm):
  class Meta:
    model = Publicidad
    fields = '__all__'