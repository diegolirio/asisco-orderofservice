# coding: utf-8
from django.test import TestCase
from model_mommy import mommy
from os_project.core.models import Pessoa

class PessoaModelTest(TestCase):    
        
    def test_exist_model(self):
        # espera que exista a classe model Pessoa criada
        try:
            from os_project.core.models import Pessoa
        except:
            self.fail(u'Não existe a classe de modelo Pessoa')

    def test_pessoa_list(self):
        """
        quantidade esperada na lista deve ser 5
        """
        pessoas = mommy.make(Pessoa, _quantity=5)
        assert len(pessoas) == 5

