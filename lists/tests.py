from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

from lists.models import Item, List

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
        
    #def test_home_page_can_save_a_post_request(self):
        #request = HttpRequest()
        #request.method = 'POST'
        #request.POST['item_text'] = '4 Minjah ct'

        #response = home_page(request)

        #self.assertEqual(Item.objects.count(),1)
        #new_item = Item.objects.first()
        #self.assertEqual(new_item.text,'4 Minjah ct')

        #self.assertEqual(response.status_code,302)
        #self.assertEqual(response['location'],'/lists/the-only-list/')

        #self.assertIn('4 Minjah ct',response.content.decode())


        #expected_html = render_to_string('home.html',
                #{'new_item_text': '4 Minjah ct'})
        #self.assertEqual(expected_html,response.content.decode())

    #def test_home_page_display_all_items(self):
        #Item.objects.create(text='item 1')
        #Item.objects.create(text='item 2')

        #request = HttpRequest()
        #response = home_page(request)

        #self.assertIn('item 1',response.content.decode())
        #self.assertIn('item 2',response.content.decode())
        

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

    #def test_saving_and_retrieving_items(self):
        #first_item = Item()
        #first_item.text = 'The first item'
        #first_item.save()

        #second_item = Item()
        #second_item.text = 'Second item'
        #second_item.save()

        #saved_items = Item.objects.all()
        #self.assertEqual(saved_items.count(),2)

        #first_saved = saved_items[0]
        #self.assertEqual(first_saved.text,'The first item')

class TestListView(TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #def test_displays_all_items(self):
        #lis = List.objects.create()
        #Item.objects.create(text='item1', list = lis)
        #Item.objects.create(text='item2', list = lis)

        #response = self.client.get('/lists/the-only-list/')
        #self.assertContains(response,'item1')
        #self.assertContains(response,'item2')

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/'%(list_.id,))
        self.assertTemplateUsed(response,'list.html')

    def test_display_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='item1', list = correct_list)
        Item.objects.create(text='item2', list = correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='other item1', list = other_list)
        Item.objects.create(text='other item2', list = other_list)

        response = self.client.get('/lists/%d/'%(correct_list.id))
        self.assertContains(response, 'item1')
        self.assertContains(response, 'item2')
        self.assertNotContains(response,'other item1')
        self.assertNotContains(response,'other item2')

    def test_pass_correct_list_to_template(self):
        correct_list = List.objects.create()
        other_list = List.objects.create()
        response = self.client.get('/lists/%d/'%(correct_list.id))
        self.assertEqual(response.context['list'],correct_list)
        
        
        
class TestNewList(TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_saving_a_POST_request(self):
        lis = List.objects.create()
        self.client.post('/lists/new',data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

    def test_redirect_after_post(self):
        response = self.client.post('/lists/new',data={'item_text': 'A new list item'})
        #self.assertEqual(response.status_code,302)
        #self.assertEqual(response['location'],'/lists/the-only-list')
        new_list = List.objects.first()
        self.assertRedirects(response,'/lists/%d/'%(new_list.id))
        
class TestListAndItem(TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_saving_and_retrieving_items_list(self):
        lis = List()
        lis.save()

        first_item = Item()
        first_item.text = 'first item'
        first_item.list = lis
        first_item.save()

        second_item = Item()
        second_item.text = 'second item'
        second_item.list = lis
        second_item.save()
        
        saved_list = List.objects.first()
        self.assertEqual(saved_list,lis)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        saved1 = saved_items[0]
        self.assertEqual(saved1.text,'first item')
        self.assertEqual(saved1.list,lis)

class TestNewItem(TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_save_a_Post_request_to_an_existing_list(self):
        correct_list = List.objects.create()
        other_list = List.objects.create()

        self.client.post('/lists/%d/add_item'%(correct_list.id,),
                data={'item_text':'new item for existing list'})

        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'new item for existing list')
        self.assertEqual(new_item.list,correct_list)

    def test_redirect_to_list_view(self):
        correct_list = List.objects.create()
        other_list = List.objects.create()

        response = self.client.post('/lists/%d/add_item'%(correct_list.id,),
                data={'item_text':'new item for existing list'})

        self.assertRedirects(response, 'lists/%d/'%(correct_list.id))

