from django import forms
from .models import Listing

class CreateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'start_bid', 'image_url', 'category', 'created_by']
