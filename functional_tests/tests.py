from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

from django.test import LiveServerTestCase

class TestNewAgent(LiveServerTestCase):

    """Test case docstring."""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """TODO: Docstring for check_for_row_in_list_table.

        :row_text: TODO
        :returns: TODO

        """
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        # he notices the page title and header mention 'real-estate' lists
        assert 'Property' in self.browser.title, "Title was " + self.browser.title

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Start a new',header_text)

        # he is invited to enter a new listing straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a listing')

        # he types "4 dingley village" into a text box
        inputbox.send_keys('4 dingley village')

        # when he hits enter, the page update, url also updated following rest
        # convention and the page lists
        #  "1: 4 dingley village" as an item in the list
        inputbox.send_keys(Keys.ENTER)
        heng_url = self.browser.current_url
        self.assertRegex(heng_url, '/lists/.+')
        self.check_for_row_in_list_table('1: 4 dingley village')

        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertTrue(any(row.text == '1: 4 dingley village' for row in rows),
                #'new listing item not appear, text was \n%s'%table.text)

        # there's still the text box to enter more listing, he 
        # enters "6 blackwood drive"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('6 blackwood drive')
        inputbox.send_keys(Keys.ENTER)

        # the page updates again, and shows both item on her list

        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertIn('1: 4 dingley village',[row.text for row in rows])
        #self.assertIn('2: 6 blackwood drive',[row.text for row in rows])
        self.check_for_row_in_list_table('1: 4 dingley village')
        self.check_for_row_in_list_table('2: 6 blackwood drive')

        # Kim comes, there is no sign of Heng's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('4 dingley village',page_text)
        self.assertNotIn('6 blackwood drive',page_text)

        # Kim starts entering her listings
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('narra waren')
        inputbox.send_keys(Keys.ENTER)
        # Kim gets her own url
        kim_url = self.browser.current_url
        self.assertRegex(kim_url, '/lists/.+')
        self.assertNotEqual(kim_url,heng_url)
        #again, no clue about listings of heng
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('dingley village',page_text)
        self.assertIn('narra waren',page_text)

        # Heng wants to make sure the list is there for him, he sees 
        # that the site generate a unique URL for him -- there is some
        # explainatory text to that effect
        self.fail('finish the test')

        # He visits that url - his listings is still there

        # satisfied, he's back to bed

if __name__ == '__main__':
    unittest.main(warnings='ignore')
