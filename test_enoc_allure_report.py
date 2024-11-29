import unittest
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from Page_login import Login_Page
from enoc_page import e_Noc_Page


@allure.feature("AXIN E-NOC Module")
class AXIN(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://axin.plcgroup.io/app")
        cls.driver.implicitly_wait(10)

    @allure.story("Login Functionality")
    @allure.title("Verify successful login to AXIN")
    def login_page(self):
        driver = self.driver
        login = Login_Page(driver)
        login.EnterEmail("testingReport@PLC")
        time.sleep(1)
        login.EnterPassword("testingReport@plcgroup.com")
        time.sleep(1)
        login.ClickLoginBtn()
        time.sleep(2)

        self.check = login.DetectloginPage()
        with allure.step("Check if login page displays successfully"):
            if self.check:
                allure.attach(driver.get_screenshot_as_png(), name="Login Success", attachment_type=allure.attachment_type.PNG)
                print("Test_01: Verify Axin login page has been displayed successfully")
            else:
                allure.attach(driver.get_screenshot_as_png(), name="Login Failed", attachment_type=allure.attachment_type.PNG)
                self.assertFalse(True, msg="Test_03: Verify Axin login failed")

    @allure.story("E-NOC Tiles Functionality")
    @allure.title("Verify E-NOC Tiles are working properly")
    def E_NOC_tiles_functionality(self):
        driver = self.driver
        enoc = e_Noc_Page(driver)
        enoc.Click_ENOC_BTN()
        time.sleep(1)
        enoc.Check_ENocTiles()
        time.sleep(2)

        self.check = enoc.DelectMyAlarmPage()
        with allure.step("Verify all tiles functionality in E-NOC"):
            if self.check:
                allure.attach(driver.get_screenshot_as_png(), name="Tiles Working", attachment_type=allure.attachment_type.PNG)
                print("Test_02: Verify all tiles are working and displayed successfully")
            else:
                allure.attach(driver.get_screenshot_as_png(), name="Tiles Issue", attachment_type=allure.attachment_type.PNG)
                self.assertFalse(True, msg="Verify all tiles are not working and displayed")

    @allure.story("E-NOC Critical Alarms")
    @allure.title("Verify critical alarms display and filter")
    def Validate_critical_alarms(self):
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
        with allure.step("Validate critical alarms display and filter"):
            if self.check:
                allure.attach(driver.get_screenshot_as_png(), name="Critical Alarm Success", attachment_type=allure.attachment_type.PNG)
                print("Test_03: Verify critical alarm tiles are working and data displayed successfully")
            else:
                allure.attach(driver.get_screenshot_as_png(), name="Critical Alarm Failure", attachment_type=allure.attachment_type.PNG)
                self.assertFalse(True, msg="Test_03: Verify critical alarm tiles are not working and data not displayed successfully")

    @allure.title("Verify Go to Site functionality in E-NOC Critical Alarms")
    @allure.severity(allure.severity_level.CRITICAL)
    def Verify_Go_to_Site_functionality(self):
        driver = self.driver
        enoc = e_Noc_Page(driver)
        with allure.step("Navigate to Critical Alarm section"):
            enoc.Click_CriticalAlarm()
            time.sleep(1)
        with allure.step("Perform search and interact with a specific row"):
            enoc.Click_Search_Bar()
            time.sleep(1)
            enoc.Click_Specfic_Row()
        with allure.step("Click 'Go to Site' button and verify redirection"):
            enoc.Click_Go_To_Site()
            self.check = enoc.Delect_Critical_Alarm()
            allure.attach(driver.get_screenshot_as_png(), name="Go To Site", attachment_type=allure.attachment_type.PNG)
            self.assertTrue(self.check, "Test_04: SSV dashboard did not display successfully.")

    @allure.title("Verify E-NOC Filters are working properly")
    @allure.severity(allure.severity_level.NORMAL)
    def E_NOC_Filters(self):
        driver = self.driver
        enoc = e_Noc_Page(driver)
        with allure.step("Apply filters in E-NOC section"):
            enoc.Click_EnocFilter()
            time.sleep(1)
            enoc.Click_Select_Attribute()
            time.sleep(1)
            enoc.Click_Select_Value()
            time.sleep(1)
            enoc.Click_AddBtn()
            time.sleep(1)
        with allure.step("Add additional filter by Alarm Name"):
            enoc.Click_EnocFilter()
            time.sleep(1)
            enoc.Click_AlarmName()
            time.sleep(1)
            enoc.Click_AddBtn()
            time.sleep(1)
        with allure.step("Verify filters are applied and data is displayed"):
            self.check = enoc.Delect_Critical_Alarm()
            allure.attach(driver.get_screenshot_as_png(), name="E-NOC Filters",
                          attachment_type=allure.attachment_type.PNG)
            self.assertTrue(self.check, "Test_05: E-NOC Filters did not work as expected.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()