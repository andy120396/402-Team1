from django.test import TestCase

class SimpleTest(TestCase):

    def test_simple_math(self):
        self.assertEqual(1+1, 2)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.asserEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Bank Account</title>, html')
        self.assertTrue(html.endswith('</html>'))
