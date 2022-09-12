from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'


# class AritlceForm(forms.Form):
#     city_a = 'bu'
#     city_b = 'ul'
#     city_c = 'ku'
#     CITY_CHOICES = [
#         (city_a, '부산'),
#         (city_b, '중국'),
#         (city_c, '울산'),
#     ]
    
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=CITY_CHOICES)

