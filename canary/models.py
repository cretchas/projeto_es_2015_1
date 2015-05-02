# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.template.defaulttags import verbatim


escolha = (
			('funcionamento', 'Funcionamento'),
			('confiabilidade', 'Confiabilidade'),
            ('usabilidade', 'Usabilidade'),
            ('eficiencia', 'Eficiência'),
            ('manutenibilidade', 'Manutenibilidade'),
            ('portabilidade', 'Portabilidade')
)

fator = (
					('1', 'Fator 1: 4 - 3'),
                    ('2', 'Fator 2: 4 - 2'),
                    ('3', 'Fator 3: 4 - 1'),
                    ('4', 'Fator 4: 4 - 0')
)

class Projeto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="nome")
    descricao = models.TextField(verbose_name="descrição")
    introducao = models.TextField(verbose_name="introdução")
    objetivo = models.TextField(verbose_name="objetivo")
    autores = models.ManyToManyField(User)
    tecnologias = models.ManyToManyField('Tecnologia')
    relacao1 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 1")
    relacao2 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 2")
    fator = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")

    def __unicode__(self):
        return '%s' % self.nome

# class Autor(models.Model):
#     nome = models.CharField(max_length=90)
#
#     def __unicode__(self):
#         return '%s' % self.nome

class Referencia(models.Model):
    projeto = models.ForeignKey(Projeto)
    titulo = models.CharField(max_length=90, verbose_name="título")
    autores = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, verbose_name="descrição")

    def __unicode__(self):
        return '%s' % self.titulo

    class Meta:
        verbose_name="Referência"

class Tecnologia(models.Model):
    api = models.ManyToManyField('API', verbose_name="API")
    descricao = models.CharField(max_length=100, verbose_name="descrição")
    razaoUso = models.CharField(max_length=100, verbose_name="razão de uso")

    def __unicode__(self):
        return '%s' % self.descricao

class API(models.Model):
    nome = models.CharField(max_length=50)
    versao = models.CharField(max_length=10, verbose_name="versão")
    especificacao = models.TextField(verbose_name="especificação")

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name="API"
        verbose_name_plural="APIs"

classificacao = (
                    ('0', '0'),
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4')
)

class AtributoDeQualidade(models.Model):
    projeto = models.OneToOneField(Projeto, blank=True)
    funcionamento = models.CharField(max_length=2, choices=classificacao, blank=True)
    confiabilidade = models.CharField(max_length=2, choices=classificacao, blank=True)
    usabilidade = models.CharField(max_length=2, choices=classificacao, blank=True)
    eficiencia = models.CharField(max_length=2, choices=classificacao, verbose_name="eficiência", blank=True)
    manutenibilidade = models.CharField(max_length=2, choices=classificacao, blank=True)
    portabilidade = models.CharField(max_length=2, choices=classificacao, blank=True)

    class Meta:
        verbose_name="Atributo de qualidade"
        verbose_name_plural="Atributos de qualidade"

class Feature(models.Model):
    class Meta:
        abstract = True

    projeto = models.ForeignKey(Projeto)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(verbose_name="descrição")

    def __unicode__(self):
        return '%s, %s' % self.nome, self.descricao

class NaoFuncional(Feature):
    fonte = models.TextField()
    estimulo = models.TextField(verbose_name="estímulo")
    ambiente = models.TextField()
    artefato = models.TextField()
    resposta = models.TextField()
    medicao = models.TextField(verbose_name="medição")

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name="Requisito não funcional"
        verbose_name_plural="Requisitos não funcionais"

class Funcional(Feature):

    def __unicode__(self):
        return '%s' % self.nome, self.descricao

    class Meta:
        verbose_name="Requisito funcional"
        verbose_name_plural="Requisitos funcionais"

optVisaoEstrutural = (
                    (1, 'Baixo'),
                    (2, 'Medio'),
                    (3, 'Alto')
)
VisaoComportamental = (
                    (1, 'Baixo'),
                    (2, 'Alto')
)

class PontoDeVista(models.Model):
    projeto = models.ForeignKey(Projeto)
    resumo = models.TextField()
    stakeholders = models.TextField()
    preocupacao = models.TextField(verbose_name="preocupação")
    detalheVisaoEstrutural = models.IntegerField(choices=optVisaoEstrutural, verbose_name="Detalhamento da visão estrutural")
    detalheVisaoComportamental = models.IntegerField(choices=VisaoComportamental, verbose_name="Detalhamento da visão comportamental")

    def __unicode__(self):
        return '%s' % self.resumo

    class Meta:
        verbose_name="Ponto de vista"
        verbose_name_plural="Pontos de vista"

class Elemento(models.Model):
    nome = models.CharField(max_length=40)
    pontoDeVista = models.ForeignKey(PontoDeVista, blank=True, null=True, verbose_name="ponto de vista")
    elementosRelacionados = models.ManyToManyField('self', blank=True, null=True, verbose_name="elementos relacionados")
    propriedades = models.TextField()
    restricoes = models.TextField(verbose_name="restrições")

    def __unicode__(self):
        return '%s' % self.nome