  GNU nano 4.6                                                                                                                  functional_test.py
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import unittest

class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_main_page_to_sub(self):
        #Dan decides to create an online bank account on a bank’s website.
        self.browser.get('http://localhost:8000')

        #When he opens the site, he sees a that the title has to do with Bank Accounts
        self.assertEqual('Bank Account', self.browser.title)

        #He clicks sign up and is prompted to enter his first name, last name.
        inputbox = self.browser.find_element_by_id('id_new_user')

        #Dan enters his name and presses Enter
        inputbox.send_keys('Dan Miles')
        clickbox = self.browser.find_element_by_id('id_sign_up')
        actions = ActionChains(self.browser)
        actions.move_to_element(clickbox)
        actions.click(clickbox)
        actions.perform()
        time.sleep(5)

    def test_sub(self):
        self.browser.get('http://localhost:8000/lists/subpage')
        time.sleep(1)

        #The website tells him that his account is approved and shows dan a screen with his username

        #Dan now clicks on “deposit” and deposits $1000 and we see the balance reflect that change
        depobox = self.browser.find_element_by_id('depoButton')
        actions = ActionChains(self.browser)
        actions.click(depobox)
        actions.perform()
        time.sleep(5)
        obj = self.browser.switch_to.alert
        time.sleep(1)
        obj.send_keys('1000')
        actions.send_keys(Keys.ENTER)
        time.sleep(5)

        #Dan now clicks on “withdraw” and withdraw $500 and we see the balance show the withdrawal’s details.
        #withBox = self.browser.find_element_by_id('withButton')
        #move_to_button = ActionChains(self.browser).move_to_element(withbox)
        #move_to_button.click()
        #send_keys('500')
        #send_keys(Keys.ENTER)

        #self.fail('testing')


if __name__ == '__main__':
    unittest.main()

