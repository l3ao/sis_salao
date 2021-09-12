from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    rsocial = models.CharField(max_length=50, default='')
    ie = models.CharField(max_length=20, blank=True, null=True)
    cnpj = models.CharField(max_length=20, default='')
    cep = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=20, blank=True, null=True)
    fone = models.CharField(max_length=20, blank=True, null=True)
    cel = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    endnumero = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.rsocial