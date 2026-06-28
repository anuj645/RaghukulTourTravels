from django import forms
from .models import TourPackage, Category


class TourPackageForm(forms.ModelForm):
    """
    ModelForm automatically creates form fields from the model.
    We just customize the widgets to add Bootstrap classes.
    """

    class Meta:
        model  = TourPackage
        fields = [
            'title', 'slug', 'category', 'description', 'highlights',
            'itinerary', 'price_per_person', 'discounted_price',
            'duration_days', 'max_group_size', 'difficulty',
            'destination', 'cover_image', 'is_featured', 'is_active'
        ]
        widgets = {
            'title':            forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Manali Adventure Trek'}),
            'slug':             forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. manali-adventure-trek'}),
            'category':         forms.Select(attrs={'class': 'form-select'}),
            'description':      forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'highlights':       forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'One highlight per line'}),
            'itinerary':        forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Day 1: Arrival...\nDay 2: Trek...'}),
            'price_per_person': forms.NumberInput(attrs={'class': 'form-control'}),
            'discounted_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration_days':    forms.NumberInput(attrs={'class': 'form-control'}),
            'max_group_size':   forms.NumberInput(attrs={'class': 'form-control'}),
            'difficulty':       forms.Select(attrs={'class': 'form-select'}),
            'destination':      forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Manali, Himachal Pradesh'}),
            'cover_image':      forms.FileInput(attrs={'class': 'form-control'}),
            'is_featured':      forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active':        forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_discounted_price(self):
        """
        Custom validation — discounted price must be less than regular price.
        Methods starting with clean_<fieldname> are called automatically by Django.
        """
        price      = self.cleaned_data.get('price_per_person')
        discounted = self.cleaned_data.get('discounted_price')

        if discounted and price and discounted >= price:
            raise forms.ValidationError('Discounted price must be less than the regular price.')

        return discounted