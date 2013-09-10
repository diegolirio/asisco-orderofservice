# coding: utf-8
from django.test import TestCase
from model_mommy import mommy
from os_project.core.models import Equipe

class EquipeModelTest(TestCase):    

    def test_exist_model(self):
        # espera que exista a classe model Equipe criada
        try:
            from os_project.core.models import Equipe
        except:
            self.fail(u'Não existe a classe de modelo Equipe') 
        
    def test_equipe_list(self):
        """
        quantidade esperada na lista deve ser 5
        """
        equipes = mommy.make(Equipe, _quantity=5)
        assert len(equipes) == 5

