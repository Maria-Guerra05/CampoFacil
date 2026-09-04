from django.contrib.auth.models import User
from django.db import models

class Produtor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="produtor")
    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=30, blank=True)
    propriedade = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE, related_name="receitas")
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100, blank=True)
    observacao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data", "-id"]

class Despesa(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE, related_name="despesas")
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100, blank=True)
    observacao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data", "-id"]

class Documento(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE, related_name="documentos")
    nome = models.CharField(max_length=200)
    data = models.DateField()
    categoria = models.CharField(max_length=100, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    arquivo = models.FileField(upload_to="documentos/")
    observacao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data", "-id"]
