from django import forms 
from . import models 

class CreateCommunitie(forms.ModelForm): 
    class Meta: 
        model = models.Communitie
        fields = ['title','body','slug','banner']