from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page

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
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Property list</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
