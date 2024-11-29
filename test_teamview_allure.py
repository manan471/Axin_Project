import unittest
import allure
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
from teamview_page import Team_View_Page


@allure.feature('AXIN Test Suite')
class AXIN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://axin.plcgroup.io/login")
        cls.driver.implicitly_wait(10)

    @allure.story('Login Page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Axin_A(self):
        driver = self.driver
        login = Login_Page(driver)
        time.sleep(2)

        with allure.step('Enter email and password'):
            login.EnterEmail("testingReport@PLC")
            login.EnterPassword("testingReport@plcgroup.com")

        with allure.step('Click Login button'):
            login.ClickLoginBtn()

        with allure.step('Verify login page detection'):
            self.check = login.DetectloginPage()
            if self.check:
                allure.attach(driver.get_screenshot_as_png(), name="LoginSuccess",
                              attachment_type=allure.attachment_type.PNG)
                print("Test_01: Verify Axin login page has been displayed successfully")
            else:
                allure.attach(driver.get_screenshot_as_png(), name="LoginFailed",
                              attachment_type=allure.attachment_type.PNG)
                self.assertFalse(True, msg="Test_03: Verify Axin login failed")

        time.sleep(6)

    @allure.story('Team View Page')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Axin_B(self):
        driver = self.driver
        teamview = Team_View_Page(driver)
        time.sleep(2)

        with allure.step('Click on Team View'):
            teamview.ClickTeamView()
            time.sleep(4)

        with allure.step('Verify Team View page detection'):
            self.check = teamview.DetectTeamViewPage()
            if self.check:
                allure.attach(driver.get_screenshot_as_png(), name="TeamViewSuccess",
                              attachment_type=allure.attachment_type.PNG)
                print("Test_02: Verify Team view page has been displayed successfully")
            else:
                allure.attach(driver.get_screenshot_as_png(), name="TeamViewFailed",
                              attachment_type=allure.attachment_type.PNG)
                self.assertFalse(True, msg="Test_02: Verify Team view failed")

    @allure.story('Settings Page')
    @allure.severity(allure.severity_level.MINOR)
    def test_Axin_C(self):
        driver = self.driver
        teamview = Team_View_Page(driver)
        time.sleep(2)

        with allure.step('Click on Settings button'):
            teamview.Cick_SettingBtn()
            time.sleep(2)

        with allure.step('Verify Settings page detection'):
            self.check = teamview.DetectSettingPage()
            if self.check:
                allure.attach(driver.get_screenshot_as_png(), name="SettingsSuccess",
                              attachment_type=allure.attachment_type.PNG)
                print("Test_03: Verify Settings page has been displayed successfully")
            else:
                allure.attach(driver.get_screenshot_as_png(), name="SettingsFailed",
                              attachment_type=allure.attachment_type.PNG)
                self.assertFalse(True, msg="Verify Settings page view failed ")

        time.sleep(4)

    @allure.story('SSV Dashboard')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Axin_D(self):
        driver = self.driver
        teamview = Team_View_Page(driver)
        time.sleep(3)

        with allure.step('Click on filters and search'):
            teamview.Click_Grid_Not_Install()
            time.sleep(1)
            teamview.Click_Grid_Outage()
            time.sleep(1)
            teamview.Click_Extended_Grid_Outage()
            time.sleep(1)
            teamview.Click_Poor_Grid_Quality()
            time.sleep(1)
            teamview.Click_Poor_Power_Factor()
            time.sleep(2)
            teamview.ClickSearchbar()
            time.sleep(5)
            teamview.ClickSSVBtn()
            time.sleep(5)

        with allure.step('Scroll to the SSV dashboard'):
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(3)

        with allure.step('Verify SSV dashboard detection'):
            self.check = teamview.DetectSSVDashBoard()
            if self.check:
                allure.attach(driver.get_screenshot_as_png(), name="SSVSuccess",
                              attachment_type=allure.attachment_type.PNG)
                print("Test_03: PH-BAN-01091 site Verify SSV page has been displayed successfully")
            else:
                allure.attach(driver.get_screenshot_as_png(), name="SSVFailed",
                              attachment_type=allure.attachment_type.PNG)
                self.assertFalse(True, msg="Test_03: Verify SSV failed")

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
