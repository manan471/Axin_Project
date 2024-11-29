import unittest
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time
import os
import openpyxl
from Page_login import Login_Page



class AXIN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://axin.plcgroup.io/")
        cls.driver.implicitly_wait(10)

    def test_Axin_A(self):
        driver = self.driver
        login = Login_Page(driver)
        time.sleep(2)
        login.EnterEmail('advisor@imarat.com')
        login.EnterPassword('123456789')
        login.ClickLoginBtn()
        self.check = login.DetectloginPage()
        if self.check == True:
            print("Test_01:Verify Axin  login page has been display successfully")
        else:
            self.assertFalse(True, msg="Test_03: Verify Axin login failed")

    def test_Axin_B(self):
        time.sleep(5)

