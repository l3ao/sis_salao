from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=95, blank=True, null=True)
    rsocial = models.CharField(max_length=95, blank=True, null=True)
    ie = models.CharField(max_length=95, blank=True, null=True)
    cnpj = models.CharField(max_length=95, blank=True, null=True)
    cep = models.CharField(max_length=95, blank=True, null=True)
    endereco = models.CharField(max_length=95, blank=True, null=True)
    bairro = models.CharField(max_length=95, blank=True, null=True)
    fone = models.CharField(max_length=95, blank=True, null=True)
    cel = models.CharField(max_length=95, blank=True, null=True)
    email = models.CharField(max_length=95, blank=True, null=True)
    endnumero = models.CharField(max_length=95, blank=True, null=True)
    cidade = models.CharField(max_length=95, blank=True, null=True)
    estado = models.CharField(max_length=95, blank=True, null=True)

    def __str__(self):
        return self.rsocial