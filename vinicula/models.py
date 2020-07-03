from django.db import models

class Vinicula(models.Model):
    nomeVinicula = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    vinho = models.CharField(max_length=100)
    produtor = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeVinicula

    def save(self, *args, **kwargs):
        super(Vinicula, self).save(*args, **kwargs)