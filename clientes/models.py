from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome