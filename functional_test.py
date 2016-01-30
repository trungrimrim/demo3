from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        assert 'Property' in self.browser.title, "Title was " + self.browser.title

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Property',header_text)

        # he is invited to enter a new listing straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a listing')

        # he types "4 dingley village" into a text box
        inputbox.send_keys('4 dingley village')

        # when he hits enter, the page update, and the page lists
        #  "1: 4 dingley village" as an item in the list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: 4 dingley village' for row in rows))

        # there's still the text box to enter more listing, he 
        # enters "6 blackwood drive"

        # the page updates again, and shows both item on her list
        self.fail('finish the test')

        # Heng wants to make sure the list is there for him, he sees 
        # that the site generate a unique URL for him -- there is some
        # explainatory text to that effect

        # He visits that url - his listings is still there

        # satisfied, he's back to bed

if __name__ == '__main__':
    unittest.main(warnings='ignore')
