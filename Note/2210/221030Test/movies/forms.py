from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):

    title = forms.CharField(
        label='영화 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목'
            }
        )
    )

    poster_url = forms.URLField(
        label='영화 포스터 주소',
        widget=forms.TextInput(
            attrs={
                'placeholder': '포스터 이미지 주소'
            }
        )
    )

    CHOICES = [('--선택--','--선택--'),('코미디','코미디'),('SF','SF'),('드라마','드라마'),('로맨스','로맨스'),('스릴러','스릴러'),('애니','애니'),('판타지','판타지'),('전쟁','전쟁'),('범죄','범죄'),('느와르','느와르'),]
    genre = forms.ChoiceField(choices=CHOICES,
        label = '장르')
         
    release_date = forms.DateField(
        label='개봉일',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex) 연도-월-일'
            }
        )
    )

    score = forms.FloatField(
        label='평점',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex) 9.58'
            }
        )
    )

    audience = forms.CharField(
        label='관객수',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex) 210만명'
            }
        )
    )

    movie_plot = forms.CharField(
        label='영화 줄거리',
        widget=forms.Textarea(
            attrs={
                'placeholder': '줄거리'
            }
        )
    )

    

    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ('created_at')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('movie',) 