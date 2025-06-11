from django.db import models
from datetime import date

# Create your models here.
class homepage(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=800)
    logo = models.ImageField(upload_to='homepage/')

    def __str__(self):
        return self.titulo
    

class quarto(models.Model):
    
    tipo_quarto = [
        ("Solteiro", "Solteiro"),
        ("Premium", "Premium"),
        ("Plus", "Plus"),
    ]

    num_Quarto = models.IntegerField()
    qtd_Hospedes = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=tipo_quarto)
    valor = models.FloatField()
    descricao = models.TextField(max_length=300)
    img = models.ImageField(upload_to='quarto/')

    def __str__(self):
        x = f"{self.tipo} - {self.num_Quarto}"
        return x

    
class hospede(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20)
    data_inicio = models.DateField(default=date.today)
    data_final = models.DateField(default=date.today)
    status = models.BooleanField(default=True)

    
    # Relação de chave estrangeira com o modelo 'quarto'
    # Vai manter os registros mesmo se o quarto for removido do banco de dados 
    quarto = models.ForeignKey(quarto, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.nome
