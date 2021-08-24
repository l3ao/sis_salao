from django.db import models

# Create your models here.
class Servico(models.Model):
    descricao = models.CharField(verbose_name='Descrição', max_length=50)
    preco = models.DecimalField(verbose_name='Preço', max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']
