from  django import forms
from  django.forms import TextInput,Select,SelectDateWidget,ChoiceField
from movapp.models import Movie,Genre

class GenreForm(forms.ModelForm):
    Genre=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Genre', 'style': 'width: 300px;', 'class': 'form-control'}))
    Discription=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Discription', 'style': 'width: 300px;', 'class': 'form-control'}))
    class Meta:
        model= Genre 
        fields='__all__' 
        widgets= {
            'Genre': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Genre'
                }),
            'Discription': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Description'
                })
        }



class MovieForm(forms.ModelForm):
    class Meta:
        model= Movie
        fields= '__all__'
        widgets = {
            
            'Title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 410px;',
                'placeholder': 'Title'
                }),
            'Release_date': forms.DateInput(attrs={
                'class': "form-control",
                'type':'date'
                
                
                }),    
            'Duaration': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 410px;',
                'placeholder': 'Duaration'
                }),
            'Summary': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 410px;',
                'placeholder': 'Summary'
                }),
            'Movie_genre':Select(attrs={
                'class': "form-select",
                'style': 'max-width: 410px;',
                'placeholder': 'select',
                
                }), 
                      

                
        }
