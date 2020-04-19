import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
browser = webdriver.Firefox()

class NewUserTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def sample_test(self):
        #Dan decides to create an online bank account on a bank’s website.
        self.browser.get('http://localhost:8000')

        #When he opens the site, he sees a that the title has to do with Bank Accounts
        self.assert('Bank Account', self.browser.title)

        #He clicks sign up and is prompted to enter his first name, last name.
        inputbox = self.browser.find_element_by_id('id_new_user')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your first and last name'

        )

        #Dan enters his name and presses Enter
        inputbox.send_keys('Dan Miles')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #The website tells him that his account is approved and shows dan a screen with his username and bank account balance that starts at zero
        #Dan now clicks on “deposit” and deposits $1000 and we see the balance reflect that change


        #Dan now clicks on “withdraw” and withdraw $500 and we see the balance show the withdrawal’s details.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
