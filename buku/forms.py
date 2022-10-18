from django.forms import ModelForm
from .models import Buku

class BukuForm(ModelForm):
    class Meta:
        model = Buku
        fields = [
            'judul',
            'sinopsis',
            'author',
        ]