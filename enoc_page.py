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

class e_Noc_Page():
    def __init__(self, driver):
        self.driver = driver
        self.click_enoc = "(//div[@class = 'MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiCard-root css-1gq1s8i'])[3]"
        self.click_settingbtn = "(//button[@class = 'MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeSmall MuiButton-outlinedSizeSmall MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeSmall MuiButton-outlinedSizeSmall css-lsym87'])[2]"
        self.enter_criticalalarm = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1'])[4]"
        self.enter_majoralarm = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1'])[5]"
        self.enterminor = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1'])[6]"
        self.click_applybtn = "//button[@class = 'MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-1iy499v']"
        self.click_my_alarm = "//p[text() = 'e-NOC']"
        self.click_all_site = "//p[text() = 'All Sites']"
        self.click_online_site = "//p[text() = 'Online']"
        self.click_RMS_Office = "//p[text() = 'RMS Offline']"
        self.clcik_site_down = "//p[text() = 'Site Down']"
        self.clcik_active_alarms =  "//p[text() = 'Alarms']"
        self.click_critical = "//p[text() = 'Critical']"
        self.click_major = "//p[text() = 'Major']"
        self.click_minor = "//p[text() = 'Minor']"
        self.click_snoozed = "//p[text() = 'Snoozed']"
        self.click_acknowledged = "//p[text() = 'Acknowledged']"
        self.click_active = "//p[text() = 'Active']"
        self.specfic_row = "(//tr[@class = 'MuiTableRow-root MuiTableRow-hover css-18emc2i'])[1]"
        self.click_search_bar = "(//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1yxmbwk'])[2]"
        self.click_alarm_site_count = "//p[@class = 'MuiTypography-root MuiTypography-body1 css-uem8cj']"
        self.click_alarm_site_specfic_row = "(//tr[@class = 'MuiTableRow-root MuiTableRow-hover css-18emc2i'])[1]"
        self.detect_enoc_screen = "//p[@class = 'MuiTypography-root MuiTypography-body1 css-z3ibk8']"
        self.click_go_to_site = "//p[text() = 'Go To Site']"
        self.detect_critical_alarm = "//p[text() = 'Historic']"
        self.click_site_alarm_count = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1'])[2]"
        self.click_filter = "//button[text() = 'Filter']"
        self.click_select_attribute = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1'])[1]"
        self.click_select_value = "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1'])[2]"
        self.addbtn = "//button[text() = 'Add']"
        self.detect_enoc = "//p[@class = 'MuiTypography-root MuiTypography-body1 css-z3ibk8']"


    def Detect_Filter(self):
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.detect_enoc))):
            return True
        else:
            return False

    def Click_AlarmName(self):
        self.driver.find_element(by=By.XPATH, value=self.click_select_attribute).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_select_attribute).send_keys(Keys.ARROW_UP + Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_select_value).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_select_value).send_keys(Keys.ARROW_UP  + Keys.ENTER)



    def Click_AddBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.addbtn).click()

    def Click_Select_Value(self):
        self.driver.find_element(by=By.XPATH, value=self.click_select_value).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_select_value).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(2)

    def Click_Select_Attribute(self):
        self.driver.find_element(by=By.XPATH, value=self.click_select_attribute).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.click_select_attribute).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(2)

    def Click_EnocFilter(self):
        self.driver.find_element(by=By.XPATH, value=self.click_filter).click()
        time.sleep(2)

    def Click_Site_Alarm_Count(self):
        self.driver.find_element(by=By.XPATH, value=self.click_site_alarm_count).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//tr[@class = 'MuiTableRow-root css-ehq6ys'])[1]").click()
        time.sleep(2)
        # element = self.driver.find_element(By.ID, "your-element-id")
        #
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
        #

    def Delect_Critical_Alarm(self):
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.detect_critical_alarm))):
            return True
        else:
            return False


    def Click_Go_To_Site(self):
        self.driver.find_element(by=By.XPATH, value=self.click_go_to_site).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value= "//h6[@class = 'MuiTypography-root MuiTypography-h6 css-4gfn8t']").click()
        time.sleep(2)

    def DelectENoc_Screen(self):
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.detect_enoc_screen))):
            return True
        else:
            return False

    def Click_Alarm_Site_Specfic_Row(self):
        self.driver.find_element(by=By.XPATH, value=self.click_alarm_site_specfic_row).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value= "//p[@class = 'MuiTypography-root MuiTypography-body1 css-svhwd6']").click()
        time.sleep(2)

    def Click_Alarm_Count(self):
        self.driver.find_element(by=By.XPATH, value=self.click_alarm_site_count).click()
        time.sleep(2)


    def Click_Search_Bar(self):
        self.driver.find_element(by=By.XPATH, value=self.click_search_bar).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//input[@class = 'MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd css-mnn31']").send_keys("00711")
        time.sleep(2)

    def Click_Specfic_Row(self):
        self.driver.find_element(by=By.XPATH, value=self.specfic_row).click()
        time.sleep(2)



    def Click_CriticalAlarm(self):
        self.driver.find_element(by=By.XPATH, value=self.click_critical).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_active).click()
        time.sleep(2)


    def DelectENocTiles(self):
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.click_active))):
            return True
        else:
            return False

    def Check_ENocTiles(self):
        self.driver.find_element(by=By.XPATH, value=self.click_all_site).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_active).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_online_site).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_RMS_Office).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.clcik_site_down).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.clcik_active_alarms).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_critical).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_major).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_minor).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_snoozed).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.click_acknowledged).click()

    def DelectMyAlarmPage(self):
        if WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located((By.XPATH, self.click_my_alarm))):
            return True
        else:
            return False

    # def Click_MyAlram(self):
    #     time.sleep(2)
    #     self.driver.find_element(by=By.XPATH, value=self.click_my_alarm).click()
    #     time.sleep(2)


    def Click_ENOC_BTN(self):
        self.driver.find_element(by=By.XPATH, value=self.click_enoc).click()
        time.sleep(1)

    def Enter_MinorAlarm(self):
        self.driver.find_element(by=By.XPATH, value=self.enterminor).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.enterminor).send_keys("abdulmanan" + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[@class = 'MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary Mui-selected css-1n7jl2w']").click()
        time.sleep(2)
    def Click_SettingBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_settingbtn).click()
        time.sleep(2)


    def Enter_CriticalAlarm(self):
        self.driver.find_element(by=By.XPATH, value=self.enter_criticalalarm).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.enter_criticalalarm).send_keys("abdulmanan" + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[@class = 'MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary Mui-selected css-1n7jl2w']").click()

    def Enter_MajorAlarm(self):
        self.driver.find_element(by=By.XPATH, value=self.enter_majoralarm).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.enter_majoralarm).send_keys("abdulmanan" + Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[@class = 'MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary Mui-selected css-1n7jl2w']").click()

    def Click_ApplyBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_applybtn).click()
        time.sleep(1)

