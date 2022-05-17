from django import forms


# from .models import Image
#
#
# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ("caption", "image")
#
#         widgets = {
#             'caption': forms.TextInput(attrs={'class': 'caption'}),
#             'image': forms.FileInput(attrs={'class': 'image'})
#         }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.CharField(max_length=150)
    message = forms.CharField()
