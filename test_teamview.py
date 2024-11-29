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
import pandas as pd

from Page_login import Login_Page
from teamview_page import Team_View_Page



class AXIN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://axin.plcgroup.io/login")
        cls.driver.implicitly_wait(10)

    def test_Axin_A(self):
        driver = self.driver
        login = Login_Page(driver)
        time.sleep(2)
        login.EnterEmail("testingReport@PLC")
        login.EnterPassword("testingReport@plcgroup.com")
        login.ClickLoginBtn()
        self.check = login.DetectloginPage()
        if self.check == True:
            print("Test_01:Verify Axin login page has been display successfully")
        else:
            self.assertFalse(True, msg="Test_03: Verify Axin login failed")

        time.sleep(6)

    def test_Axin_B(self):
        driver = self.driver
        teamview = Team_View_Page(driver)
        time.sleep(2)
        teamview.ClickTeamView()
        time.sleep(4)
        self.check = teamview.DetectTeamViewPage()
        if self.check == True:
            print("Test_02:Verify Team view page has been display successfully")
        else:
            self.assertFalse(True, msg="Test_02: Verify Team view failed")

    def test_Axin_C(self):
        driver = self.driver
        teamview = Team_View_Page(driver)
        time.sleep(2)
        teamview.Cick_SettingBtn()
        time.sleep(2)
        self.check = teamview.DetectSettingPage()
        if self.check == True:
            print("Test_03:Verify Setting page has been display successfully")
        else:
            self.assertFalse(True, msg="Verify setting page view failed ")
        time.sleep(4)


    def test_Axin_D(self):
        driver = self.driver
        teamview = Team_View_Page(driver)
        time.sleep(3)
        # teamview.ClickTeamView()
        # teamview.Click_ToggleBtn()
        teamview.Click_Grid_Availability_Ratio()
        time.sleep(1)
        teamview.Click_Grid_Not_Install()
        time.sleep(1)
        teamview.Click_Grid_Outage()
        time.sleep(1)
        teamview.Click_Extended_Grid_Outage()
        time.sleep(1)
        teamview.Click_Poor_Grid_Quality()
        time.sleep(1)
        teamview.Click_Poor_Power_Factor()
        time.sleep(1)
        teamview.Click_High_Grid_Outage_Events()
        time.sleep(2)
        teamview.ClickSearchbar()
        time.sleep(5)
        teamview.ClickSSVBtn()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(3)
        self.check = teamview.DetectSSVDashBoard()
        if self.check == True:
            print("Test_03:PH-BAN-01091 site Verify SSV page has been display successfully")
        else:
            self.assertFalse(True, msg="Test_03: Verify SSV failed")
        time.sleep(5)
        teamview.Click_ProfileBtn()
        time.sleep(10)






