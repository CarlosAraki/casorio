from django.db import models

# TABELAS PRÉ FEITAS POR NÓS
class EstadoCivil(models.Model):
    # SOLTEIRO, COMPROMETIDO
    descricao = models.CharField(max_length = 10)
    
class Genero(models.Model):
    # MULHER, HOMEM, OUTRO
    descricao = models.CharField(max_length = 10)

class Tatuador(models.Model):
    # DADOS DE CADA TATUADOR
    nome = models.CharField(max_length=500)
    disponivel = models.BooleanField()

# TABELAS QUE SERAO INCREMENTADAS DURANTE A FESTA
class Perfil(models.Model):
    # INFORMACOES DE CADA CONVIDADO
    # CADA CONVIDADO IRÁ CRIAR SEU PERFIL
    nome = models.CharField(max_length=500)
    foto = models.CharField(max_length=500)  # ALTERAR DEPOIS PARA ARQUIVOS DE FOTO
    estadoCivil = models.ForeignKey(EstadoCivil, on_delete = models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE)
    idade = models.IntegerField()

class Pontos(models.Model):
    # QUANTOS PONTOS CADA PERFIL TEM
    # PONTOS SERAO INCREMENTADOS CONFORME DESAFIOS FOREM CONCLUIDOS
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    numero = models.IntegerField()

class Musica(models.Model):
    # ADICIONAR MUSICAS NA FILA DE REPRODUCAO
    # CONVIDADOS IRAO ADICIONAR CONFORME QUISEREM
    nome = models.CharField(max_length=500)  # INTEGRAR COM SPOTIFY
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    
class FilaTatuador(models.Model):
    # ADICIONAR CONVIDADOS NA FILA DO TATUADOR
    # CONVIDADOS IRAO SE ADICIONAR CONFORME QUISEREM
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    lugarFila = models.IntegerField()
    tatuador = models.ForeignKey(Tatuador, on_delete=models.CASCADE)