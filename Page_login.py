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

class Login_Page():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
        self.loginbtn = "//button[text() = 'sign in']"
        self.visibilitylogin = "//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2']"

    def EnterEmail(self, email):
        self.driver.find_element(by=By.NAME, value=self.email).send_keys(email)
        time.sleep(2)


    def EnterPassword(self, password):
        self.driver.find_element(by=By.NAME, value=self.password).send_keys(password)
        time.sleep(2)

    def ClickLoginBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.loginbtn).click()
        time.sleep(2)

    def DetectloginPage(self):
        time.sleep(5)
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.visibilitylogin))):
            return True
        else:
            return False
