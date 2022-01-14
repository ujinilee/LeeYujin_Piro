from django import forms
from .models import Review

class PostForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__' ##모두 접근

        #form's' 오타!!