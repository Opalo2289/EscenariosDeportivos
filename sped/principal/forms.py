from django import forms
from principal import models

# class CestaForm(forms.ModelForm):
#     class Meta:
#         model = Cesta
#         fields = [
#         'fecha',
#         'empleado',
#         'tipoServicio',
#         'tipoCesta']
#         widgets = {
#             'fecha': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
#             'empleado' : forms.Select(attrs={'class':'form-control'}),
#             'tipoServicio' : forms.Select(attrs={'class':'form-control'}),
#             'tipoCesta' : forms.Select(attrs={'class':'form-control'}),
#         }