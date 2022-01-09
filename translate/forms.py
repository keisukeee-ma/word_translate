from django import forms

class KakikomiForm(forms.Form):
     word = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'翻訳したい言葉を入れてください。'}))