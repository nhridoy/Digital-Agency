from django import forms
from homeapp import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.ReviewModel
        fields = '__all__'
        widgets = {
            'comment': forms.Textarea(attrs={'style': 'resize: none;'}),
        }
