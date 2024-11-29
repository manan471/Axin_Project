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
from enoc_page import e_Noc_Page



class AXIN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://axin.plcgroup.io/app")
        cls.driver.implicitly_wait(5)

    def test_eNoc_A(self):
        driver = self.driver
        login = Login_Page(driver)
        enoc = e_Noc_Page(driver)
        login.EnterEmail("testingReport@PLC")
        time.sleep(1)
        login.EnterPassword("testingReport@plcgroup.com")
        time.sleep(1)
        login.ClickLoginBtn()
        time.sleep(2)
        self.check = login.DetectloginPage()
        if self.check == True:
            print("Test_01:Verify Axin login page has been display successfully")
        else:
            self.assertFalse(True, msg="Test_03: Verify Axin login failed")
        time.sleep(3)

    def test_eNoc_B(self):
        driver = self.driver
        enoc = e_Noc_Page(driver)
        enoc.Click_ENOC_BTN()
        time.sleep(1)
        enoc.Check_ENocTiles()
        time.sleep(2)
        self.check = enoc.DelectMyAlarmPage()
        if self.check == True:
            print("Test_02:Verify All Tiles is working properly and display successfully")
        else:
            self.assertFalse(True, msg="Verify All Tiles is not working properly and  display")

    def test_eNoc_C(self):
        driver = self.driver
        enoc = e_Noc_Page(driver)
        time.sleep(1)
        # enoc.Click_ENOC_BTN()
        time.sleep(2)
        enoc.Check_ENocTiles()
        time.sleep(2)
        self.check = enoc.DelectENocTiles()
        if self.check == True:
            print("Test_02:Verify ENoc Tiles is working and data has been display successfully")
        else:
            self.assertFalse(True, msg="Test_03: Verify ENoc Tiles is not working and data has not been display successfully")


    def test_eNoc_D(self):
        driver = self.driver
        enoc = e_Noc_Page(driver)
        enoc.Click_CriticalAlarm()
        time.sleep(2)
        enoc.Click_Search_Bar()
        time.sleep(2)
        enoc.Click_Specfic_Row()
        time.sleep(2)
        enoc.Click_Alarm_Count()
        time.sleep(2)
        enoc.Click_Alarm_Site_Specfic_Row()
        time.sleep(2)
        self.check = enoc.DelectENoc_Screen()
        if self.check == True:
            print("Test_03:Verify Critical Alarm Tiles is working and data has been display successfully")
        else:
            self.assertFalse(True, msg="Test_03: Verify Critical Alarm Tiles is not working and data has not been display successfully")


    def test_eNoc_E(self):
        driver = self.driver
        enoc = e_Noc_Page(driver)
        time.sleep(2)
        enoc.Click_CriticalAlarm()
        time.sleep(1)
        enoc.Click_Search_Bar()
        time.sleep(1)
        enoc.Click_Specfic_Row()
        enoc.Click_Go_To_Site()
        self.check = enoc.Delect_Critical_Alarm()
        if self.check == True:
            print("Test_04: Verify that the SSV dashboard is displayed successfully upon clicking Go to Site in e-NOC")
        else:
            self.assertFalse(True, msg="Test_04: Verify that the SSV dashboard is not displayed successfully upon clicking Go to Site in e-NOC")


    def test_eNoc_F(self):
        driver = self.driver
        enoc = e_Noc_Page(driver)
        time.sleep(2)
        # enoc.Click_ENOC_BTN()
        # enoc.Click_Site_Alarm_Count()
        enoc.Click_EnocFilter()
        time.sleep(2)
        enoc.Click_Select_Attribute()
        time.sleep(2)
        enoc.Click_Select_Value()
        time.sleep(2)
        enoc.Click_AddBtn()
        time.sleep(2)
        enoc.Click_EnocFilter()
        time.sleep(2)
        enoc.Click_AlarmName()
        time.sleep(2)
        enoc.Click_AddBtn()
        time.sleep(2)
        self.check = enoc.Delect_Critical_Alarm()
        if self.check == True:
            print("Test_04: Verify that E-Noc Filter is working properly")
        else:
            self.assertFalse(True, msg="Verify that E-Noc Filter has not been working properly")














