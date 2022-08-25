from django import forms
from .models import Category, status_choices

choices_category = Category.objects.values_list('category','category')

class CreateListingForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    start_price = forms.FloatField(label="Start bid price", min_value=0, required=True)
    image = forms.ImageField(label="Auction image", required=False)
    category = forms.ChoiceField(label="Category", choices=choices_category)

class UpdateStatus(forms.Form):
    status = forms.ChoiceField(label="Status", choices=status_choices)

class AddComment(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)