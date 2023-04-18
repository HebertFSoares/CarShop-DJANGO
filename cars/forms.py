from django import forms
from .models import Brand,Car

class CarFrom(forms.Form):
     model = forms.CharField(max_length=200)
     brand = forms.ModelChoiceField(Brand.objects.all())
     factory_year = forms.IntegerField()
     model_year = forms.IntegerField()
     place = forms.CharField(max_length=10)
     value = forms.FloatField()
     photo = forms.ImageField()
     
     def save(self):
          car = Car(
               model = self.cleaned_data['model'],
               brand = self.cleaned_data['brand'],
               factory_year = self.cleaned_data['factory_year'],
               model_year = self.cleaned_data['model_year'],
               place = self.cleaned_data['place'],
               value = self.cleaned_data['value'],
               photo = self.cleaned_data['photo'],
          )
          car.save()
          return car