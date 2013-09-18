# coding: utf-8
from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet

from os_project.core.models import OrdemServico, Equipe
from os_project.core.forms import EquipeForm

class HomeTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin', 'admin@gmail.com', 'admin')
        self.client.login(username='admin', password='admin')
        self.resp = self.client.get(reverse('home'))

    def test_get(self):
        'Get / must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Reponse should be a rendered template index.html'
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        'Html must contain controls...'
        self.assertContains(self.resp, u'<h1>OrderOfService')
        self.assertContains(self.resp, u'<p>Controle de Ordem de Serviços')

        self.assertContains(self.resp, u'Cadastrar Order de Serviço')
        self.assertContains(self.resp, u'Cadastro de Cliente')
        self.assertContains(self.resp, u'Cadastro de Equipe')        

        self.assertContains(self.resp, u'<a href="/cliente/list/')
        self.assertContains(self.resp, u'<a href="/equipe/list/')
        pass

    def test_context(self):
        'Context must contain data...'
        user = self.resp.context['user']
        self.assertIn('lista', self.resp.context)
        self.assertIsInstance(user, User)

class EquipeListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('equipe_list'))

    def test_get(self):
        'Get / must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Reponse should be a rendered template equipe.html'
        self.assertTemplateUsed(self.resp, 'equipe.html')


    def test_context(self):
        'Context must contain data...'
        self.assertIn('equipes', self.resp.context)

        equipes = self.resp.context['equipes']
        self.assertIsInstance(equipes, QuerySet)

    def test_html(self):
        'Html must contain controls...'
        self.assertContains(self.resp, u'<legend>Cadastro de Equipes')
        self.assertContains(self.resp, u'<a href="/equipe/add/"')
        self.assertContains(self.resp, u'Adicionar nova Equipe')

class EquipeAddTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('equipe_add'))

    def test_get(self):
        'Get / must return status code 200'
        self.assertEqual(200, self.resp.status_code)        

    def test_template(self):
        'Reponse should be a rendered template equipe.html'
        self.assertTemplateUsed(self.resp, 'equipe.html')

    def test_context(self):
        'Context must contain data...'
        self.assertIn('form', self.resp.context)   
        
        form = self.resp.context['form']
        self.assertIsInstance(form, EquipeForm)             

    def test_html(self):
        'Html must contain controls...'
        self.assertContains(self.resp, u'<a href="/equipe/list/"')

class EquipeEditTest(TestCase):
    def setUp(self):
        equipe = Equipe.objects.create(nome='equipe teste')
        self.resp = self.client.get(reverse('equipe_edit', args=[equipe.pk]))

    def test_get(self):
        'Get / must return status code 200'
        self.assertEqual(200, self.resp.status_code)        

    def test_template(self):
        'Reponse should be a rendered template equipe.html'
        self.assertTemplateUsed(self.resp, 'equipe.html')

    def test_context(self):
        'Context must contain data...'
        
        # testo se existe no contexto uma chave: form
        self.assertIn('form', self.resp.context)   
        
        # testo se o form é do tipo EquipeForm
        form = self.resp.context['form']
        self.assertIsInstance(form, EquipeForm)        

        # testo se o form tem uma instancia preenchida para edição
        self.assertEqual(True, form.instance.id > 0)     

    def test_html(self):
        'Html must contain controls...'
        self.assertContains(self.resp, u'<a href="/equipe/list/"')        
