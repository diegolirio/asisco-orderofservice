# coding: utf-8
from django.test import TestCase
from model_mommy import mommy
from os_project.core.models import Equipe, Membro

class MembroModelTest(TestCase):    
    
    def test_exist_model(self):
        # espera que exista a classe model Membro criada
        try:
            from os_project.core.models import Membro
        except:
            self.fail(u'Não existe a classe de modelo Membro')        

    def test_membro_list(self):
        """
        quantidade esperada na lista deve ser 5
        """
        membros = mommy.make(Membro, _quantity=5)
        assert len(membros) == 5

