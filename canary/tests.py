"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
from django.test import TestCase
from models import API
from models import Tecnologia
from models import Referencia
from models import Arquitetura
from models import AtributoDeQualidade
from models import NaoFuncional
from models import Funcional
from models import Elemento
from models import PontoDeVista


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
def test_autores_vazio(self):
        self.assertTrue(len(self.referencia.autores) != 0)

        # Teste BD#


# Teste class  API
class ApiTest(TestCase):
    def setUp(self):
        self.api = API.objects.create(nome="maps", versao="1.0", especificacao="API desenvolvida pela Google")

    def test_models(self):
        api = API.objects.get(id=1)
        self.assertEqual(api.nome, "maps")


#Teste class Tecnologia
class TecnologiaTest(TestCase):
    def setUp(self):
        self.tecnologia = Tecnologia.objects.create(descricao="dasdasdasas", razaoUso="Deve ser usado por")
        self.tecnologia.api.create(nome="maps", versao="1.0", especificacao="dasdasdasdasdas")

    def test_model(self):
        apis = API.objects.all()
        tecnologias = Tecnologia.objects.all()
        self.assertEqual(apis.count(), 1)
        self.assertEqual(tecnologias.count(), 1)


class ProjetoTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.projeto.tecnologias.create(descricao="dasdasdasas", razaoUso="Deve ser usado por")
        self.projeto.autores.create(id=1)

    def test_model(self):
        projetos = Arquitetura.objects.all()
        self.assertEqual(projetos.count(), 1)


#Teste class Referencia
class ReferenciaTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.referencia = Referencia.objects.create(titulo="tituloreferencia", autores="autoresdareferencia",
                                                    descricao="issoeumareferencia", projeto=self.projeto)

    def test_model(self):
        referencias = Referencia.objects.all()
        self.assertEqual(referencias.count(), 1)


class AtributoQualidadeTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.atributo = AtributoDeQualidade.objects.create(funcionamento="01", confiabilidade="02", usabilidade="05",
                                                           eficiencia="03", manutenibilidade="02",
                                                           portabilidade="04", projeto=self.projeto)

    def test_model(self):
        atributos = AtributoDeQualidade.objects.all()
        self.assertEqual(atributos.count(), 1)


class NaoFuncionalTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.naofuncional = NaoFuncional.objects.create(nome="nomeFeature", descricao="descricaoFeature",
                                                        fonte="fontenaofuncional",
                                                        estimulo="estimulonaofuncional",
                                                        ambiente="ambientenaofuncional", artefato="artefatonaofuncional"
                                                        , resposta="respostanaofuncional",
                                                        medicao="medicaonaofuncional", projeto=self.projeto)

    def test_model(self):
        naofuncionais = NaoFuncional.objects.all()
        self.assertEqual(naofuncionais.count(), 1)


class FuncionalTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.funcional = Funcional.objects.create(nome="nomeFeature", descricao="descricaoFeature",
                                                  projeto=self.projeto)

    def test_model(self):
        funcionais = Funcional.objects.all()
        self.assertEqual(funcionais.count(), 1)


class PontoDeVistaTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.pontodevista = PontoDeVista.objects.create(projeto=self.projeto, resumo="resumoPonto",
                                                        stakeholders="stakeholdersPonto",
                                                        preocupacao="preocupacaoPonto", detalheVisaoEstrutural=1,
                                                        detalheVisaoComportamental=2)
    def test_model(self):
        pontos = PontoDeVista.objects.all()
        self.assertEqual(pontos.count(), 1)


class ElementoTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.pontodevista = PontoDeVista.objects.create(projeto=self.projeto, resumo="resumoPonto",
                                                        stakeholders="stakeholdersPonto",
                                                        preocupacao="preocupacaoPonto", detalheVisaoEstrutural=1,
                                                        detalheVisaoComportamental=2)

        self.elemento = Elemento.objects.create(nome="nomeElemento", pontoDeVista=self.pontodevista,
                                                propriedades="propriedadesElemento", restricoes="restricoesElemento")

    def test_model(self):
        elementos = Elemento.objects.all()
        self.assertEquals(elementos.count(), 1)


######################################################### Teste URLS ##################################################


class HomePageTest(TestCase):

    def test_url(self):
      c = Client()
      response = c.get('/admin/')
      self.assertEqual(response.status_code, 200)

class CanaryUrl(TestCase):

    def test_url(self):
        c = Client()
        response = c.get('/admin/canary/')
        self.assertEqual(response.status_code, 200)

class ProjetoUrl(TestCase):

    def test_url(self):
        c = Client()
        response = c.get('/admin/canary/arquitetura/')
        self.assertEqual(response.status_code, 200)

    def test_url_addprojeto(self):
        c = Client()
        response = c.get('/admin/canary/arquitetura/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_projeto(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.projeto.tecnologias.create(descricao="dasdasdasas", razaoUso="Deve ser usado por")
        self.projeto.autores.create(id=1)

        c = Client()
        response = c.get('/admin/canary/arquitetura/1/')
        self.assertEqual(response.status_code, 200)

    def test_cadastro_projeto(self):
        c = Client()
        self.tecnologia = Tecnologia.objects.create(descricao="dasdasdasas", razaoUso="Deve ser usado por")
        response = c.post('/admin/canary/arquitetura/add/', {'nome':'nomedoProjeto', 'descricao':'descricaoProjeto',
                                                                                                'introducao':'introducaoProjeto', 'objetivo':'objetivoProjeto', 'autores':1, 'tecnologias':1})
        self.assertEqual(response.status_code, 200)

class ElementoUrl(TestCase):

    def test_url(self):
        c = Client()
        response = c.get('/admin/canary/elemento/')
        self.assertEqual(response.status_code, 200)

    def test_url_add(self):
        c = Client()
        response = c.get('/admin/canary/elemento/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_elemento(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.pontodevista = PontoDeVista.objects.create(projeto=self.projeto, resumo="resumoPonto",
                                                        stakeholders="stakeholdersPonto",
                                                        preocupacao="preocupacaoPonto", detalheVisaoEstrutural=1,
                                                        detalheVisaoComportamental=2)

        self.elemento = Elemento.objects.create(nome="nomeElemento", pontoDeVista=self.pontodevista,
                                                propriedades="propriedadesElemento", restricoes="restricoesElemento")
        c = Client()
        response = c.get('/admin/canary/elemento/1/')
        self.assertEqual(response.status_code, 200)

    def test_cadastro_elemento(self):
        c = Client()
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.pontodevista = PontoDeVista.objects.create(projeto=self.projeto, resumo="resumoPonto",
                                                        stakeholders="stakeholdersPonto",
                                                        preocupacao="preocupacaoPonto", detalheVisaoEstrutural=1,
                                                        detalheVisaoComportamental=2)

        response = c.post('/admin/canary/arquitetura/elemento/add/', {'nome':'nomeElemento', 'pontodeVista':1,
                                                              'propriedades':'propriedadesElemento', 'restricoes':'restricoesElemento'})
        self.assertEqual(response.status_code, 200)



class APIUrl(TestCase):

    def test_url(self):
        c = Client()
        response = c.get('/admin/canary/api/')
        self.assertEqual(response.status_code, 200)

    def test_url_add(self):
        c = Client()
        response = c.get('/admin/canary/api/add/')
        self.assertEqual(response.status_code, 200)


    def test_url_API(self):
        self.api = API.objects.create(nome="maps", versao="1.0", especificacao="API desenvolvida pela Google")
        c = Client()
        response = c.get('/admin/canary/api/1/')
        self.assertEqual(response.status_code, 200)


    def test_cadastra_api(self):
        self.api = API.objects.create(nome="maps", versao="1.0", especificacao="API desenvolvida pela Google")
        c = Client()
        response = c.post('/admin/canary/arquitetura/api/add/', {'nome': 'nomeApi', 'versao': 'versaoApi', 'especificacao': 'especificaoApi'})
        self.assertEqual(response.status_code, 200)


class TecnologiaUrl(TestCase):

    def test_url(self):
        c = Client()
        response = c.get('/admin/canary/tecnologia/')
        self.assertEqual(response.status_code, 200)

    def test_url_add(self):
        c = Client()
        response = c.get('/admin/canary/tecnologia/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_Tecnologia(self):
        self.tecnologia = Tecnologia.objects.create(descricao="dasdasdasas", razaoUso="Deve ser usado por")
        self.tecnologia.api.create(nome="maps", versao="1.0", especificacao="dasdasdasdasdas")
        c = Client()
        response = c.get('/admin/canary/tecnologia/1/')
        self.assertEqual(response.status_code, 200)


    def test_url_cadastrar(self):
        self.api = API.objects.create(nome="maps", versao="1.0", especificacao="dasdasdasdasdas")
        self.tecnologia = Tecnologia.objects.create(descricao="dasdasdasas", razaoUso="Deve ser usado por")
        c = Client()
        response = c.post('/admin/canary/arquitetura/tecnologia/add/', {'descricao': 'descricaoTecnologia', 'razaoUso': 'razaousoTecnologia','api':1})
        self.assertEqual(response.status_code, 200)


class AutoresUrl(TestCase):

    def test_url(self):
        c = Client()
        response = c.get('/admin/auth/user/add/')
        self.assertEqual(response.status_code, 200)

    def test_url_add(self):
        c = Client()
        response = c.get('/admin/auth/user/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        c = Client()
        response = c.post('/admin/', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)


################################################# Teste campos  ######################################



################################################# Cenario Positivo ####################################
class ApiDadosTest(TestCase):
    def setUp(self):
        self.api = API.objects.create(nome="maps", versao="1", especificacao="API desenvolvida pela Google")

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.api.nome) <= 50)

    def test_nome_vazio(self):
        self.assertTrue(len(self.api.nome) != 0)

    def test_vesao_maxcaracteres(self):
        self.assertTrue(len(self.api.versao) <= 2)

    def test_vesao_vazio(self):
        self.assertTrue(len(self.api.versao) != 2)

    def test_especificacao_vazio(self):
        self.assertTrue(len(self.api.especificacao) != 0)

class TecnologiaDadosTest(TestCase):
    def setUp(self):
        self.tecnologia = Tecnologia.objects.create(descricao="descricaoTecnologia", razaoUso="Deve ser usado por")
        self.tecnologia.api.create(nome="maps", versao="1.0", especificacao="dasdasdasdasdas")

    def test_descricao_maxcaracteres(self):
        self.assertTrue(len(self.tecnologia.descricao) <= 100)

    def test_descricao_vazio(self):
        self.assertTrue(len(self.tecnologia.descricao) != 0)

    def test_razaoUso_maxcaracteres(self):
        self.assertTrue(len(self.tecnologia.razaoUso) <= 100)

    def test_razaoUso_vazio(self):
        self.assertTrue(len(self.tecnologia.razaoUso) != 0)

class ProjetoDadosTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.projeto.tecnologias.create(descricao="dasdasdasas", razaoUso="Deve ser usado por")
        self.projeto.autores.create(id=1)

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.projeto.nome) <= 200)

    def test_nome_vazio(self):
        self.assertTrue(len(self.projeto.nome) != 0)

    def test_descricao_vazio(self):
        self.assertTrue(len(self.projeto.descricao) != 0)

    def test_introducao_vazio(self):
        self.assertTrue(len(self.projeto.introducao) != 0)

    def test_objetivo_vazio(self):
        self.assertTrue(len(self.projeto.objetivo) != 0)

class ReferenciaDadosTest(TestCase):
     def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.referencia = Referencia.objects.create(titulo="tituloreferencia", autores="autoresdareferencia",
                                                    descricao="issoeumareferencia", projeto=self.projeto)
     def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.referencia.titulo) <= 90)

     def test_nome_vazio(self):
        self.assertTrue(len(self.referencia.titulo) != 0)

     def test_autores_maxcaracteres(self):
        self.assertTrue(len(self.referencia.autores) <= 150)

     def test_autores_vazio(self):
        self.assertTrue(len(self.referencia.autores) != 0)

     def test_descricao_maxcaracteres(self):
        self.assertTrue(len(self.referencia.descricao) <= 90)

     def test_autores_vazio(self):
        self.assertTrue(len(self.referencia.autores) != 0)


class AtributosDadosTest(TestCase):
     opcoes = ['0', '1', '2', '3', '4']
     def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.atributo = AtributoDeQualidade.objects.create(funcionamento='2', confiabilidade='2', usabilidade='4',
                                                           eficiencia='3', manutenibilidade='2',
                                                           portabilidade='4', projeto=self.projeto)
     def test_funcionamento_valor(self):
        self.assertIn(self.atributo.funcionamento, self.opcoes)

     def test_confiabilidade_valor(self):
        self.assertIn(self.atributo.funcionamento, self.opcoes)

     def test_usabilidade_valor(self):
        self.assertIn(self.atributo.usabilidade, self.opcoes)

     def test_eficiencia_valor(self):
        self.assertIn(self.atributo.eficiencia, self.opcoes)

     def test_manutenibilidade_valor(self):
        self.assertIn(self.atributo.manutenibilidade, self.opcoes)

     def test_portabilidade_valor(self):
        self.assertIn(self.atributo.portabilidade, self.opcoes)

class NaoFuncionaDadoslTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.naofuncional = NaoFuncional.objects.create(nome="nomeFeature", descricao="descricaoFeature",
                                                        fonte="fontenaofuncional",
                                                        estimulo="estimulonaofuncional",
                                                        ambiente="ambientenaofuncional", artefato="artefatonaofuncional"
                                                        , resposta="respostanaofuncional",
                                                        medicao="medicaonaofuncional", projeto=self.projeto)
    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.naofuncional.nome) <= 50)

    def test_nome_vazio(self):
        self.assertTrue(len(self.naofuncional.nome) != 0)

    def test_descricao_vazio(self):
        self.assertTrue(len(self.naofuncional.descricao) != 0)

    def test_fonte_vazio(self):
        self.assertTrue(len(self.naofuncional.fonte) != 0)

    def test_estimulo_vazio(self):
        self.assertTrue(len(self.naofuncional.estimulo) != 0)

    def test_ambiente_vazio(self):
        self.assertTrue(len(self.naofuncional.ambiente) != 0)

    def test_artefato_vazio(self):
        self.assertTrue(len(self.naofuncional.artefato) != 0)

    def test_resposta_vazio(self):
        self.assertTrue(len(self.naofuncional.resposta) != 0)

    def test_medicao_vazio(self):
        self.assertTrue(len(self.naofuncional.medicao) != 0)


class FuncionalDadosTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.funcional = Funcional.objects.create(nome="nomeFeature", descricao="descricaoFeature",
                                                  projeto=self.projeto)
    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.funcional.nome) <= 50)

    def test_nome_vazio(self):
        self.assertTrue(len(self.funcional.nome) != 0)

    def test_descricao_vazio(self):
        self.assertTrue(len(self.funcional.descricao) != 0)

class PontoDeVistaDadosTest(TestCase):
    visaoEstrutural= [1, 2, 3]
    visaoComportamental = [1, 2]

    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.pontodevista = PontoDeVista.objects.create(projeto=self.projeto, resumo="resumoPonto",
                                                        stakeholders="stakeholdersPonto",
                                                        preocupacao="preocupacaoPonto", detalheVisaoEstrutural=1,
                                                        detalheVisaoComportamental=2)
    def test_nome_vazio(self):
        self.assertTrue(len(self.pontodevista.resumo) != 0)

    def test_nome_vazio(self):
        self.assertTrue(len(self.pontodevista.stakeholders) != 0)

    def test_nome_vazio(self):
        self.assertTrue(len(self.pontodevista.preocupacao) != 0)

    def test_detalheVisaoEstrutural_valor(self):
        self.assertIn(self.pontodevista.detalheVisaoEstrutural, self.visaoEstrutural)

    def test_detalheVisaoComportamental_valor(self):
        self.assertIn(self.pontodevista.detalheVisaoComportamental, self.visaoComportamental)

class ElementoTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.pontodevista = PontoDeVista.objects.create(projeto=self.projeto, resumo="resumoPonto",
                                                        stakeholders="stakeholdersPonto",
                                                        preocupacao="preocupacaoPonto", detalheVisaoEstrutural=1,
                                                        detalheVisaoComportamental=2)

        self.elemento = Elemento.objects.create(nome="nomeElemento", pontoDeVista=self.pontodevista,
                                                propriedades="propriedadesElemento", restricoes="restricoesElemento")
    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.elemento.nome) <= 40)

    def test_nome_vazio(self):
        self.assertTrue(len(self.elemento.nome) != 0)

    def test_propriedades_vazio(self):
        self.assertTrue(len(self.elemento.propriedades) != 0)

    def test_restricoes_vazio(self):
        self.assertTrue(len(self.elemento.restricoes) != 0)



################################################# Cenario Negativo ####################################

class ApiDadosTestNegativo(TestCase):
    def setUp(self):
        self.api = API.objects.create(nome="Lorem ipsum dolor sit amet, vel ea nullam recusabo, mea ea eius eirmod. Te omittam honestatis ius. Id magna congue mel, semper intellegat id ius, nobis dolorum deserunt in his. Detracto complectitur an his. Nemore accumsan ut nam, vim dicit fuisset hendrerit ex."
                                      , versao="1000", especificacao="")

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.api.nome) <= 50)

    def test_nome_vazio(self):
        self.assertTrue(len(self.api.nome) != 0)

    def test_vesao_maxcaracteres(self):
        self.assertTrue(len(self.api.versao) <= 2)

    def test_vesao_vazio(self):
        self.assertTrue(len(self.api.versao) != 0)

    def test_especificacao_vazio(self):
        self.assertTrue(len(self.api.especificacao) != 0)

class TecnologiaDadosTestNegativo(TestCase):
    def setUp(self):
        self.tecnologia = Tecnologia.objects.create(descricao="Lorem ipsum dolor sit amet, vel ea nullam recusabo, mea ea eius eirmod. Te omittam honestatis ius. Id magna congue mel, semper intellegat id ius, nobis dolorum deserunt in his. Detracto complectitur an his. Nemore accumsan ut nam, vim dicit fuisset hendrerit ex.",
                                                    razaoUso="")
        self.tecnologia.api.create(nome="maps", versao="1.0", especificacao="dasdasdasdasdas")

    def test_descricao_maxcaracteres(self):
        self.assertTrue(len(self.tecnologia.descricao) <= 100)

    def test_descricao_vazio(self):
        self.assertTrue(len(self.tecnologia.descricao) != 0)

    def test_razaoUso_maxcaracteres(self):
        self.assertTrue(len(self.tecnologia.razaoUso) <= 100)

    def test_razaoUso_vazio(self):
        self.assertTrue(len(self.tecnologia.razaoUso) != 0)


class ProjetoDadosTestNegativo(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="Lorem ipsum dolor sit amet, vel ea nullam recusabo, mea ea eius eirmod. Te omittam honestatis ius. Id magna congue mel, semper intellegat id ius, nobis dolorum deserunt in his. Detracto complectitur an his. Nemore accumsan ut nam, vim dicit fuisset hendrerit ex.",
                                              descricao="",
                                              introducao="",
                                              objetivo="")
        self.projeto.tecnologias.create(descricao="dasdasdasas", razaoUso="Deve ser usado por")
        self.projeto.autores.create(id=1)

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.projeto.nome) <= 200)

    def test_nome_vazio(self):
        self.assertTrue(len(self.projeto.nome) != 0)

    def test_descricao_vazio(self):
        self.assertTrue(len(self.projeto.descricao) != 0)

    def test_introducao_vazio(self):
        self.assertTrue(len(self.projeto.introducao) != 0)

    def test_objetivo_vazio(self):
        self.assertTrue(len(self.projeto.objetivo) != 0)

class ReferenciaDadosTestNegativo(TestCase):
     def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.referencia = Referencia.objects.create(titulo="Lorem ipsum dolor sit amet, vel ea nullam recusabo, mea ea eius eirmod. Te omittam honestatis ius. Id magna congue mel, semper intellegat id ius, nobis dolorum deserunt in his. Detracto complectitur an his. Nemore accumsan ut nam, vim dicit fuisset hendrerit ex.",
                                                    autores="Lorem ipsum dolor sit amet, vel ea nullam recusabo, mea ea eius eirmod. Te omittam honestatis ius. Id magna congue mel, semper intellegat id ius, nobis dolorum deserunt in his. Detracto complectitur an his. Nemore accumsan ut nam, vim dicit fuisset hendrerit ex.",
                                                    descricao="Lorem ipsum dolor sit amet, vel ea nullam recusabo, mea ea eius eirmod. Te omittam honestatis ius. Id magna congue mel, semper intellegat id ius, nobis dolorum deserunt in his. Detracto complectitur an his. Nemore accumsan ut nam, vim dicit fuisset hendrerit ex.",
                                                    projeto=self.projeto)
     def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.referencia.titulo) <= 90)

     def test_nome_vazio(self):
        self.assertTrue(len(self.referencia.titulo) != 0)

     def test_autores_maxcaracteres(self):
        self.assertTrue(len(self.referencia.autores) <= 150)

     def test_autores_vazio(self):
        self.assertTrue(len(self.referencia.autores) != 0)

     def test_descricao_maxcaracteres(self):
        self.assertTrue(len(self.referencia.descricao) <= 90)

     def test_descricao_vazio(self):
        self.assertTrue(len(self.referencia.descricao) != 0)


class AtributosDadosTestNegativo(TestCase):
     opcoes = ['0', '1', '2', '3', '4']
     def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.atributo = AtributoDeQualidade.objects.create(funcionamento='5', confiabilidade='8', usabilidade='10',
                                                           eficiencia='', manutenibilidade='8',
                                                           portabilidade='b', projeto=self.projeto)
     def test_funcionamento_valor(self):
        self.assertIn(self.atributo.funcionamento, self.opcoes)

     def test_confiabilidade_valor(self):
        self.assertIn(self.atributo.funcionamento, self.opcoes)

     def test_usabilidade_valor(self):
        self.assertIn(self.atributo.usabilidade, self.opcoes)

     def test_eficiencia_valor(self):
        self.assertIn(self.atributo.eficiencia, self.opcoes)

     def test_manutenibilidade_valor(self):
        self.assertIn(self.atributo.manutenibilidade, self.opcoes)

     def test_portabilidade_valor(self):
        self.assertIn(self.atributo.portabilidade, self.opcoes)

class NaoFuncionaDadoslTestNegativo(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.naofuncional = NaoFuncional.objects.create(nome="Lorem ipsum dolor sit amet, vel ea nullam recusabo, mea ea eius eirmod. Te omittam honestatis ius. Id magna congue mel, semper intellegat id ius, nobis dolorum deserunt in his. Detracto complectitur an his. Nemore accumsan ut nam, vim dicit fuisset hendrerit ex.",
                                                        descricao="",
                                                        fonte="",
                                                        estimulo="",
                                                        ambiente="",
                                                        artefato="",
                                                        resposta="",
                                                        medicao="", projeto=self.projeto)
    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.naofuncional.nome) <= 50)

    def test_nome_vazio(self):
        self.assertTrue(len(self.naofuncional.nome) != 0)

    def test_descricao_vazio(self):
        self.assertTrue(len(self.naofuncional.descricao) != 0)

    def test_fonte_vazio(self):
        self.assertTrue(len(self.naofuncional.fonte) != 0)

    def test_estimulo_vazio(self):
        self.assertTrue(len(self.naofuncional.estimulo) != 0)

    def test_ambiente_vazio(self):
        self.assertTrue(len(self.naofuncional.ambiente) != 0)

    def test_artefato_vazio(self):
        self.assertTrue(len(self.naofuncional.artefato) != 0)

    def test_resposta_vazio(self):
        self.assertTrue(len(self.naofuncional.resposta) != 0)

    def test_medicao_vazio(self):
        self.assertTrue(len(self.naofuncional.medicao) != 0)

class FuncionalDadosTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto",
                                              descricao="descricaoProjeto",
                                              introducao="introducaoProjeto",
                                              objetivo="objetivoProjeto")
        self.funcional = Funcional.objects.create(nome="Lorem ipsum dolor sit amet, vel ea nullam recusabo, mea ea eius eirmod. Te omittam honestatis ius. Id magna congue mel, semper intellegat id ius, nobis dolorum deserunt in his. Detracto complectitur an his. Nemore accumsan ut nam, vim dicit fuisset hendrerit ex.",
                                                  descricao="",
                                                  projeto=self.projeto)
    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.funcional.nome) <= 50)

    def test_nome_vazio(self):
        self.assertTrue(len(self.funcional.nome) != 0)

    def test_descricao_vazio(self):
        self.assertTrue(len(self.funcional.descricao) != 0)


class PontoDeVistaDadosTestNegativo(TestCase):
    visaoEstrutural= [1, 2, 3]
    visaoComportamental = [1, 2]

    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")

        self.pontodevista = PontoDeVista.objects.create(projeto=self.projeto,
                                                        resumo="",
                                                        stakeholders="",
                                                        preocupacao="",
                                                        detalheVisaoEstrutural=5,
                                                        detalheVisaoComportamental=10)
    def test_nome_vazio(self):
        self.assertTrue(len(self.pontodevista.resumo) != 0)

    def test_nome_vazio(self):
        self.assertTrue(len(self.pontodevista.stakeholders) != 0)

    def test_nome_vazio(self):
        self.assertTrue(len(self.pontodevista.preocupacao) != 0)

    def test_detalheVisaoEstrutural_valor(self):
        self.assertIn(self.pontodevista.detalheVisaoEstrutural, self.visaoEstrutural)

    def test_detalheVisaoComportamental_valor(self):
        self.assertIn(self.pontodevista.detalheVisaoComportamental, self.visaoComportamental)


class ElementoTest(TestCase):
    def setUp(self):
        self.projeto = Arquitetura.objects.create(nome="nomedoProjeto", descricao="descricaoProjeto",
                                              introducao="introducaoProjeto", objetivo="objetivoProjeto")
        self.pontodevista = PontoDeVista.objects.create(projeto=self.projeto, resumo="resumoPonto",
                                                        stakeholders="stakeholdersPonto",
                                                        preocupacao="preocupacaoPonto", detalheVisaoEstrutural=1,
                                                        detalheVisaoComportamental=2)

        self.elemento = Elemento.objects.create(nome="Lorem ipsum dolor sit amet, vel ea nullam recusabo, mea ea eius eirmod. Te omittam honestatis ius. Id magna congue mel, semper intellegat id ius, nobis dolorum deserunt in his. Detracto complectitur an his. Nemore accumsan ut nam, vim dicit fuisset hendrerit ex.",
                                                pontoDeVista=self.pontodevista,
                                                propriedades="",
                                                restricoes="")

    def test_nome_maxcaracteres(self):
        self.assertTrue(len(self.elemento.nome) <= 40)

    def test_nome_vazio(self):
        self.assertTrue(len(self.elemento.nome) != 0)

    def test_propriedades_vazio(self):
        self.assertTrue(len(self.elemento.propriedades) != 0)

    def test_restricoes_vazio(self):
        self.assertTrue(len(self.elemento.restricoes) != 0)