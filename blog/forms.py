from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

    def clean_title(self):
    	"""
    	Since the slugs are unique, check the title against all post titles
    	and raise error if there is a match.
    	"""
    	t = self.cleaned_data.get('title')

    	if t in [o.title for o in Post.objects.all()]:
            raise forms.ValidationError("Can't have two posts with the same title.")
        
        return t
