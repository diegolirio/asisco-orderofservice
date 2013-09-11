# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from os_project.core.models import OrdemServico
from model_mommy import mommy

class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('home'))
        self.os = mommy.make(OrdemServico)

    def test_get(self):
        'Get / must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Reponse should be a rendered template index.html'
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        'Html must contain controls...'
        self.assertContains(self.resp, u'<title>OrderOfService')
        self.assertContains(self.resp, u'<h1>OrderOfService')
        self.assertContains(self.resp, u'<a href="/admin/core/ordemservico/add/"')

    def test_context(self):
        'Context must contain data...'
        lista = self.resp.context['lista']
        self.assertIn('lista', self.resp.context)