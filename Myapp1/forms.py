from django import forms
from .models import UserProfile,Author,Book,Student,Course

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthdate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        }
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','published_date','author']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
            'published_date':forms.DateInput(attrs={'class':'form-control','type':'date','placeholder':'YYYY-MM-DD'}),
        }