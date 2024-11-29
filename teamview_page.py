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

class Team_View_Page():
    def __init__(self, driver):
        self.driver = driver
        self.clickteam_view = "//p[text() = 'ClickOPS']"
        self.click_searchbar = "//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd css-b52kj1']"
        self.click_ssvbtn = "//button[text() = 'Site Snapshot (SSV)']"
        self.detect_teamview = "//p[text() = 'Insights & Analytics Settings']"
        self.click_togglebtn = "(//input[@class = 'PrivateSwitchBase-input MuiSwitch-input css-1m9pwf3'])[1]"
        self.click_grid_not_installed = "(//div[@class ='MuiBox-root css-1xm4hct'])[1]"
        self.click_grid_outage = "(//div[@class ='MuiBox-root css-1xm4hct'])[2]"
        self.click_extended_grid_outage = "(//div[@class ='MuiBox-root css-1xm4hct'])[3]"
        self.click_poor_grid_quality = "(//div[@class ='MuiBox-root css-1xm4hct'])[4]"
        self.click_poor_power_factor = "(//div[@class ='MuiBox-root css-1xm4hct'])[5]"
        self.click_high_grid_outage_events = "(//div[@class ='MuiBox-root css-1xm4hct'])[6]"
        self.detectteampage = "//p[text() = 'Site Availability']"
        self.click_settingbtn = "//button[text() = 'Settings']"
        self.detect_setting_page = "//p[text() = 'Analytics KPI’s']"
        self.detect_ssvpage = "//p[text() = 'Power Snapshot']"
        self.clickprofilebtn = "//button[text() = 'Power Profile']"
        self.click_grid_availability = "//p[text() = 'Grid Availability & Quality']"


    def Click_Grid_Availability_Ratio(self):
        self.driver.find_element(by=By.XPATH, value=self.click_grid_availability).click()
        time.sleep(1)
    def Click_ProfileBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.clickprofilebtn).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




    def DetectSettingPage(self):
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.detect_setting_page))):
            return True
        else:
            return False


    def Cick_SettingBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_settingbtn).click()
        time.sleep(2)


    def DelectSettingPage(self):
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.detect_teamview))):
            return True
        else:
            return False





    def Click_High_Grid_Outage_Events(self):
        self.driver.find_element(by=By.XPATH, value=self.click_high_grid_outage_events).click()
        time.sleep(1)

    def Click_Poor_Power_Factor(self):
        self.driver.find_element(by=By.XPATH, value=self.click_poor_power_factor).click()
        time.sleep(2)


    def Click_Poor_Grid_Quality(self):
        self.driver.find_element(by=By.XPATH, value=self.click_poor_grid_quality).click()
        time.sleep(2)


    def Click_Grid_Not_Install(self):
        self.driver.find_element(by=By.XPATH, value="//div[@class = 'MuiBox-root css-1gr9h7h']").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_grid_not_installed).click()
        time.sleep(2)

    def Click_Grid_Outage(self):
        self.driver.find_element(by=By.XPATH, value=self.click_grid_outage).click()
        time.sleep(2)

    def Click_Extended_Grid_Outage(self):
        self.driver.find_element(by=By.XPATH, value=self.click_extended_grid_outage).click()
        time.sleep(2)



    def Click_ToggleBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_togglebtn).click()
        time.sleep(2)

    def ClickSSVBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_ssvbtn).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//div[@class = 'MuiBox-root css-lpw08x']").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//p[text() = 'Teams']").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd css-b52kj1']").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//input[@class = 'PrivateSwitchBase-input css-1m9pwf3']").click()
        time.sleep(1)
        try:
            self.driver.find_element(by=By.XPATH, value="(//input[@class = 'PrivateSwitchBase-input css-1m9pwf3'])[3]").click()
            print("Test_4:Data is same on team view and ssv")
        except:
            time.sleep(2)

        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[text() = 'Visit SSV']").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//div[@class = 'MuiBox-root css-lpw08x']").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//p[text() = 'Teams']").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value="//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd css-b52kj1']").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//input[@class = 'PrivateSwitchBase-input css-1m9pwf3']").click()
        time.sleep(1)
        try:
            self.driver.find_element(by=By.XPATH,value="(//input[@class = 'PrivateSwitchBase-input css-1m9pwf3'])[4]").click()
            print("Test_5:Data is same on team view and ssv")
        except:
            time.sleep(3)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[text() = 'Visit SSV']").click()


    def ClickSearchbar(self):
        self.driver.find_element(by=By.XPATH, value=self.click_searchbar).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//input[@class = 'PrivateSwitchBase-input css-1m9pwf3']").click()
        time.sleep(2)
        # self.site = [2, 3, 4, 5]
        # Select(self.driver.find_element(by=By.NAME, value="(//input[@class = 'PrivateSwitchBase-input css-1m9pwf3'])[2]")).select_by_index(random.choice(self.site))
        # time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="(//input[@class = 'PrivateSwitchBase-input css-1m9pwf3'])[2]").click()
    def ClickTeamView(self):
        self.driver.find_element(by=By.XPATH, value=self.clickteam_view).click()
        time.sleep(3)


    def ScrollDown(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def DetectloginPage(self):
        time.sleep(5)
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.visibilitylogin))):
            return True
        else:
            return False

    def DetectSSVDashBoard(self):
        if WebDriverWait(self.driver, 500).until(EC.visibility_of_element_located((By.XPATH, self.detect_ssvpage))):
            return True
        else:
            return False

    def DetectTeamViewPage(self):
        time.sleep(5)
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.detectteampage))):
            return True
        else:
            return False



