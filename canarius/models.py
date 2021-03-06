# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from siliqua.models import Decisao

# Create your models here.
from django.db.models import permalink
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

qtdrelacoes = (
    ('1', '1 relação'),
    ('2', '2 relações'),
    ('3', '3 relações')

)

Metodo_Avaliacao = (
    ('faam','FAAM'),
    ('aqa','AQA'),
    ('reda','REDA'),
    ('d-saam','D-SAAM'),
    ('abordagem de gannod e lutz','Abordagem de Gannod e Lutz'),
    ('abordagem Maccari', 'Abordagem Maccari'),
    ('abordagem riva e rosso', 'Abordagem Riva e Rosso'),
    ('sba', 'SBA'),
    ('cosvam', 'COSVAM'),
    ('sacam', 'SACAM')
)

Fase_Avaliacao = (
    ('PLA evaluation', 'PLA evaluation '),
    ('PA evaluation ', 'PA evaluation ')
)

class Arquitetura(models.Model):
    nome = models.CharField(max_length=200, verbose_name="nome")
    descricao = models.TextField(verbose_name="descrição")
    introducao = models.TextField(verbose_name="introdução")
    objetivo = models.TextField(verbose_name="objetivo")
    autores = models.ManyToManyField(User)
    tecnologias = models.ManyToManyField('Tecnologia')
    introducao_qualidade = models.TextField(verbose_name="introdução aos cenários de qualidade")
    referencias_qualidade = models.TextField(verbose_name="referências aos cenários de qualidade")
    qtdrelacoes = models.CharField(max_length=2, choices=qtdrelacoes, verbose_name="quantidade de relações entre atributos")
    decisoes = models.ManyToManyField(Decisao, blank=True, related_name='decisoes', verbose_name='decisões de arquitetura')

    def __unicode__(self):
        return '%s' % self.nome

    def preview(self):
        return '<a href="/canarius/arquitetura/%s">Pré visualização</a>' % (self.pk)

    preview.allow_tags = True

# class Autor(models.Model):
#     nome = models.CharField(max_length=90)
#
#     def __unicode__(self):
#         return '%s' % self.nome

class Referencia(models.Model):
    arquitetura = models.ForeignKey(Arquitetura)
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
    arquitetura = models.OneToOneField(Arquitetura, related_name='attrQualidade')
    funcionamento = models.CharField(max_length=2, choices=classificacao)
    confiabilidade = models.CharField(max_length=2, choices=classificacao)
    usabilidade = models.CharField(max_length=2, choices=classificacao)
    eficiencia = models.CharField(max_length=2, choices=classificacao, verbose_name="eficiência")
    manutenibilidade = models.CharField(max_length=2, choices=classificacao)
    portabilidade = models.CharField(max_length=2, choices=classificacao)

    class Meta:
        verbose_name="Atributo de qualidade"
        verbose_name_plural="Atributos de qualidade"

    def __unicode__(self):
        return '%s' % self.arquitetura

class Feature(models.Model):
    class Meta:
        abstract = True

    arquitetura = models.ForeignKey(Arquitetura)
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
    arquitetura = models.ForeignKey(Arquitetura)
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

class Componente(models.Model):
    descricao = models.TextField(verbose_name="descrição")
    featuresRelacionadas = models.TextField(verbose_name="features relacionadas")
    padraoDesing = models.TextField(verbose_name="padrão de design")

    def __unicode__(self):
        return '%s' % self.descricao

class Modulo(models.Model):
    descricao = models.TextField(verbose_name="descrição")
    featuresRelacionadas = models.TextField(verbose_name="features relacionadas")
    componentes = models.ManyToManyField('componente')

    def __unicode__(self):
        return '%s' % self.descricao

    class Meta:
        verbose_name="módulo"
        verbose_name_plural="módulos"

class VisaoEstrutural(models.Model):
    apresentacao = models.TextField(verbose_name="apresentação")
    estilosArquitetura = models.TextField(verbose_name="estilos de arquitetura")
    modulos = models.ManyToManyField('Modulo', verbose_name="módulos")

    def __unicode__(self):
        return '%s' % self.apresentacao

    class Meta:
        verbose_name="visão estrutural"
        verbose_name_plural="visões estruturais"

class VisaoComportamental(models.Model):
    diagrama = models.ImageField(upload_to="fotos")
    feature = models.CharField(max_length=150)
    variavelID = models.CharField(max_length=150, verbose_name="ID da variável")
    featureRelacionadas = models.TextField(verbose_name="features relacionadas")

    def __unicode__(self):
        return '%s' % self.feature

    class Meta:
        verbose_name="visão comportamental"
        verbose_name_plural="visões comportamentais"
        
class Relacionamento2(models.Model):
    projeto = models.OneToOneField(Arquitetura, blank=True)
    relacao1 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 1")
    relacao2 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 2")
    fator = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")

    class Meta:
        verbose_name="Atributos de Qualidade - 1 Relacionamento"
        verbose_name_plural="Atributos de Qualidade - 1 Relacionamento"

class Relacionamento4(models.Model):
    projeto = models.OneToOneField(Arquitetura, blank=True)
    relacao1 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 1")
    relacao2 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 2")
    fator1 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")
    relacao3 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 3")
    relacao4 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 4")
    fator2 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")

    class Meta:
        verbose_name="Atributos de Qualidade - 2 Relacionamentos"
        verbose_name_plural="Atributos de Qualidade - 2 Relacionamentos"

class Relacionamento6(models.Model):
    projeto = models.OneToOneField(Arquitetura, blank=True)
    relacao1 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 1")
    relacao2 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 2")
    fator1 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")
    relacao3 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 3")
    relacao4 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 4")
    fator2 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")
    relacao5 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 5")
    relacao6 = models.CharField(max_length=250, choices = escolha, verbose_name="atributo 6")
    fator3 = models.CharField(max_length=2, choices=fator, verbose_name="fator de impacto")

    class Meta:
        verbose_name="Atributos de Qualidade - 3 Relacionamentos"
        verbose_name_plural="Atributos de Qualidade - 3 Relacionamentos"


    #################APÊNDICE B SIRIUS################
class ClassificacaoMetricaAvaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    metodoAvaliacao = models.CharField(max_length=300, blank=False, choices= Metodo_Avaliacao, verbose_name="Método de avaliação")
    objetivo = models.TextField(blank=False)
    tiposAtributo = models.CharField(max_length=300, blank=False, verbose_name="Tipos de atributo")
    faseAvaliacao = models.CharField(max_length=300, blank=False, choices= Fase_Avaliacao, verbose_name="Fase da avaliação")
    tecnicaAvaliacao = models.TextField(blank=False, verbose_name="Técnica de avaliação")
    descricaoProcesso = models.CharField(max_length=300, blank=False, verbose_name="Descrição do processo")
    validacaoMetodo = models.CharField(max_length=300, blank=False, verbose_name="Validação do método")
    relacaoMetodo = models.CharField(max_length=300, blank=True, verbose_name="Relação com outros métodos")

    class Meta:
        verbose_name = 'Classificação das métrica de avaliação'
        verbose_name_plural = 'Classificações das métricas de avaliação'


    def __unicode__(self):
        return '%s' % self.metodoAvaliacao

class InformacaoArquitetural(models.Model):
    id = models.AutoField(primary_key=True)
    nomeProjeto = models.CharField(max_length=200, blank=False, verbose_name="Nome do projeto")
    dominioProjeto = models.CharField(max_length=200, blank=False, verbose_name="Domínio do projeto")
    data = models.DateField(blank=False)
    objetivoNegocio = models.TextField(blank=False, verbose_name="Objetivos de negócio")
    stakeholders = models.CharField(max_length=400,blank=False)
    descricao = models.CharField(max_length=200, blank=False, verbose_name="Descrição")
    cenario=models.TextField(blank=False, verbose_name="Cenário")
    taticasDesign= models.CharField(max_length=200,blank=False, verbose_name="Táticas de design")
    designRacional = models.CharField(max_length=200, blank=False, verbose_name="Motivo do design")

    class Meta:
        verbose_name = 'Informação Arquitetural'
        verbose_name_plural = 'Informações Arquiteturais'

    def __unicode__(self):
        return '%s' % self.nomeProjeto

class ModeloArquiteturaAvaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    arquitetura = models.ForeignKey(Arquitetura, blank=False, null=False)
    descricao = models.TextField(blank=False, verbose_name="Descrição da arquitetura")
    abordagem_arquitetural = models.TextField(blank=False, verbose_name="Abordagem arquitetural ")
    descricao_cenario = models.TextField(blank=False, verbose_name="Cenários ")
    descricao_de_riscos = models.TextField(blank=False,verbose_name="Riscos")
    descricao_de_nao_riscos = models.TextField(blank=False, verbose_name="Não riscos")
    ponto_de_sensibilidade = models.TextField(blank=False, verbose_name="Pontos de sensibilidade")
    capacidade_de_evolucao = models.TextField(blank=True, verbose_name="Capacidade de evolução")
    cliques = models.IntegerField(editable=False, default=0)
    classificacao_metrica_avaliacao = models.ForeignKey(ClassificacaoMetricaAvaliacao,blank=True, null=True, verbose_name="Classicação das métricas de avaliação")
    informacao_arquitetural = models.ForeignKey(InformacaoArquitetural,blank=True, null=True, verbose_name="Informações arquiteturais")

    class Meta:
        verbose_name="Avaliação"
        verbose_name_plural="Avaliações"

    def pesquisaModeloArquiteturaAvaliacao(pesquisa):
        modeloArquiteturaAvaliacao = models.ModeloArquiteturaAvaliacao.objects.all(headline_contains=pesquisa);
        return modeloArquiteturaAvaliacao

    def __unicode__(self):
        return '%s' % self.descricao

