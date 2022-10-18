from django.shortcuts import render, redirect
from .forms import BukuForm
from .models import Buku

def index(request):
    buku_form = BukuForm(request.POST or None)
    if request.method == "POST":
        if buku_form.is_valid():
            buku_form.save()

            return redirect("/")
        else:
            pass
    else:
        pass

    context = {
        'title': 'Tambah Buku',
        'buku_form': buku_form,
    }
    return render(request, 'buku/index.html', context)

def edit(request, buku_id):
    update_buku = Buku.objects.get(id=buku_id)
    newData = {
        'judul': update_buku.judul,
        'sinopsis': update_buku.sinopsis,
        'author': update_buku.author,
    }
    buku_form = BukuForm(request.POST or None, instance=update_buku)
    if request.method == "POST":
        if buku_form.is_valid():
            buku_form.save()

            return redirect("/")
        else:
            pass
    else:
        pass

    context = {
        'title': 'Edit Buku',
        'buku_form': buku_form,
    }
    return render(request, 'buku/index.html', context)

def delete(request, buku_id):
    buku = Buku.objects.filter(id=buku_id)
    buku.delete()

    return redirect("/")