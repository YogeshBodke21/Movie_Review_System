from django import forms 
from .models import Movie_Review

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = Movie_Review
        fields = "__all__"