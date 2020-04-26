from django.test import TestCase
from django.template.loader import render_to_string

class SimpleTest(TestCase):

    def test_simple_math(self):
        self.assertEqual(1+1, 2)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.asserEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Bank Account</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first name'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
    
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first name')
        self.assertEqual(second_saved_item.text, 'Item the second')
      
    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new  item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new  item')
        
    
   def test_displays_all_list_name(self):

        name.objects.create(text='name 1')

        name.objects.create(text='name 2') 
