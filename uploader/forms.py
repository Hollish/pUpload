from django.forms import ModelForm
from .models import UserFile

class UploadFileForm(ModelForm):
    class Meta:
            model = UserFile
            fields = ['upload']