from django.test import TestCase
from django.template.loader import render_to_string
from lists.views import home_page
from lists.views import subpage
from django.urls import resolve
from django.http import HttpRequest

class SimpleTest(TestCase):

    def test_simple_math(self):
        self.assertEqual(1+1, 2)
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Bank Account</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')

    def test_sub_page_returns_correct_html(self):
        request = HttpRequest()
        response = subpage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Bank Account</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('lists/subpage')
        self.assertEqual(found.func, subpage)


    
