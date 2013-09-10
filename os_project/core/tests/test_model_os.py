# coding: utf-8
from django.test import TestCase
from model_mommy import mommy
from os_project.core.models import *

class OrdemServiceModelTest(TestCase):    

    def test_exist_model(self):
        # espera que exista a classe model OrdemService criada
        try:
            from os_project.core.models import OrdemServico
        except:
            self.fail(u'Não existe a classe de modelo OrdemServico')    
        
    def test_os_list(self):
        """
        quantidade esperada na lista deve ser 5
        """
        oss = mommy.make(OrdemServico, _quantity=5)
        assert len(oss) == 5     