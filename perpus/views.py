from django.shortcuts import render
from buku.models import Buku

def index(request):
    buku = Buku.objects.all()
    context = { 'buku': buku }
    return render(request, 'index.html', context)