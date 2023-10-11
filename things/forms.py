"""Forms of the project."""
from .models import Thing
from django import forms

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing        
        fields =["name", "description", "quantity"]
        widgets = {'description': forms.Textarea(), 'quantity': forms.NumberInput()}
 
    def clean(self):
 
        super(ThingForm, self).clean()
         
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        quantity = self.cleaned_data.get('quantity')
 
        if len(name) > 35:
            self._errors['username'] = self.error_class([
                'Maximum 35 characters allowed'])
        if len(description) > 120:
            self._errors['description'] = self.error_class([
                'Description should contain a maximum of 120 characters'])
        if int(quantity) < 0 and int(quantity) > 50:
            self.errors['quantity'] = self.error_class([
                'Quantity should be between 0 and 50 (inclusive)'])
 
        return self.cleaned_data