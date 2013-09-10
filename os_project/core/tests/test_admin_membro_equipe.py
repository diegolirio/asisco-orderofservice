# coding: utf-8
from django.contrib.auth.models import User
from model_mommy import mommy
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os_project.core.models import Membro

# class MembroTest(LiveServerTestCase):

#     def setUp(self):
#         User.objects.create_superuser(username='admin',
#                                       password='admin',
#                                       email='admin@admin.com')        
#         self.browser = webdriver.Firefox()
#         self.browser.implicitly_wait(5)

#     def tearDown(self):
#         self.browser.quit()

#     def test_create_new_membro_via_admin_site(self):        
#         # abri o browser na pagina do admin
#         self.browser.get(self.live_server_url + '/admin/')

#         # She types in her username and passwords and hits return
#         username_field = self.browser.find_element_by_name('username')
#         username_field.send_keys('admin')

#         password_field = self.browser.find_element_by_name('password')
#         password_field.send_keys('admin')
#         password_field.send_keys(Keys.RETURN)

#         # verifica se existe o texto Administração do Site no contexto
#         body = self.browser.find_element_by_tag_name('body')
#         self.assertIn(u'Administração do Django', body.text)

#         # She now sees a couple of hyperlink that says "Membros"
#         membros = self.browser.find_elements_by_link_text('Membros')
#         self.assertEquals(len(membros), 1)        

#         #self.fail('finish this test')