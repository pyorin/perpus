from django.db import models

class Buku(models.Model):
    judul = models.CharField(max_length=30)
    sinopsis = models.TextField()
    author = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.judul)