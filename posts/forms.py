from django import forms
from categories.models import Category

class PostForm(forms.Form):
    title =forms.CharField(max_length=100, label='Title')
    description = forms.CharField(max_length=200)
    image= forms.FileField()
    version= forms.IntegerField()
    publisher_email =forms.EmailField(max_length=100, label='Email')
    privacy = forms.ChoiceField(
        choices=[('1', 'Public'), ('2', 'Private')])
    category =forms.ModelChoiceField(Category.get_all_categories())