from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

from lists.models import Item

# Create your tests here.
class TestSmoke(TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual(1, 1)

class TestHomePage(TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_roor_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        #self.assertTrue(response.content.startswith(b'<html>'))
        #self.assertIn(b'Property Listing',response.content)
        #self.assertTrue(response.content.strip().endswith(b'</html>'))
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)
        
    def test_home_page_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '4 Minjah ct'

        response = home_page(request)

        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'4 Minjah ct')

        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/')

        #self.assertIn('4 Minjah ct',response.content.decode())


        #expected_html = render_to_string('home.html',
                #{'new_item_text': '4 Minjah ct'})
        #self.assertEqual(expected_html,response.content.decode())

    def test_home_page_display_all_items(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('item 1',response.content.decode())
        self.assertIn('item 2',response.content.decode())
        

    def test_dont_save_blank_item(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(),0)
        

class TestItemModel(TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved = saved_items[0]
        self.assertEqual(first_saved.text,'The first item')
