# coding: utf-8
from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from os_project.core.models import OrdemServico
#from model_mommy import mommy

class HomeTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('admin', 'admin@gmail.com', 'admin')
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
        #self.assertContains(self.resp, u'<title>OrderOfService')
        #self.assertContains(self.resp, u'<h1>OrderOfService')
        #self.assertContains(self.resp, u'<a href="/admin/core/ordemservico/add/"')
        pass

    def test_context(self):
        'Context must contain data...'
        #lista = self.resp.context['lista']
        user = self.resp.context['user']
        self.assertIn('lista', self.resp.context)
        self.assertIsInstance(user, User)

class OsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('orderservice', kwargs={'pk':0,}))        

    def test_get(self):
        'Get / must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Reponse should be a rendered template index.html'
        self.assertTemplateUsed(self.resp, 'orderservice.html')

