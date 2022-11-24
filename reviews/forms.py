from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label="Name")
#     review_text=forms.CharField(label="review",widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(label="Your rating",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        labels={
            "user_name":"Your Name"
        }
        