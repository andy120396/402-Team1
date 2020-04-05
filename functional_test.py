import time
from django.test import LiveServerTestCase
from selenium import webdriver
import unittest

class NewUserTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def sample_test(self):
        #Dan decides to create an online bank account on a bank’s website.
        self.assertIn('Bank Account', self.browser.title)

        #When he opens the site, he sees a sign-up button

        #He clicks sign up and is prompted to enter his first name, last name.

        #The website tells him that his account is approved and shows dan a screen with his username and bank account balance that starts at zero

        #On the site main page, there are two buttons “deposit” and “withdraw”

        #Dan now clicks on “deposit” and deposits $1000 and we see the balance reflect that change

        #Dan now clicks on “withdraw” and withdraw $500 and we see the balance show the withdrawal’s details.
