from selenium import webdriver
import unittest

class TestNewAgent(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # he notices the page title and header mention 'real-estate' lists
        assert 'Real Estate' in self.browser.title, "Title was " + self.browser.title

        # he is invited to enter a new listing straight away

        # he types "4 dingley village" into a text box

        # when he hits enter, the page update, and the page lists
        #  "1: 4 dingley village" as an item in the list

        # there's still the text box to enter more listing, he 
        # enters "6 blackwood drive"

        # the page updates again, and shows both item on her list

        # Heng wants to make sure the list is there for him, he sees 
        # that the site generate a unique URL for him -- there is some
        # explainatory text to that effect

        # He visits that url - his listings is still there

        # satisfied, he's back to bed

if __name__ == '__main__':
    unittest.main(warnings='ignore')
