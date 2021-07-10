# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BMC(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_b_m_c(self):
        driver = self.driver
        driver.get("http://jwebhome.jcpenney.com/")
        driver.find_element_by_link_text("IT Service Request").click()
        driver.find_element_by_xpath("//div[@id='loginbody']/form/div[2]/label").click()
        driver.find_element_by_id("username-id").clear()
        driver.find_element_by_id("username-id").send_keys("")
        driver.find_element_by_xpath("//div[@id='loginbody']/form/div").click()
        driver.find_element_by_id("username-id").click()
        driver.find_element_by_id("username-id").clear()
        driver.find_element_by_id("username-id").send_keys("kdevegow")
        driver.find_element_by_id("pwd-id").click()
        driver.find_element_by_id("pwd-id").clear()
        driver.find_element_by_id("pwd-id").send_keys("Mypassword6.")
        driver.find_element_by_xpath("//div[@id='loginbody']/form/div/div").click()
        driver.find_element_by_id("login").click()
        driver.find_element_by_xpath("//a[@id='WIN_0_303053400']/div").click()
        driver.find_element_by_xpath("//a[@id='WIN_0_304324300']/div/div").click()
        driver.find_element_by_id("arid_WIN_0_302258625").click()
        driver.find_element_by_id("arid_WIN_0_302258625").clear()
        driver.find_element_by_id("arid_WIN_0_302258625").send_keys("INC000005455579")
        driver.find_element_by_xpath("//a[@id='WIN_0_302259032']/div").click()
        driver.find_element_by_xpath("//table[@id='T1000003952']/tbody/tr[2]/td[3]/nobr/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=//table[@id='T1000003952']/tbody/tr[2]/td[3]/nobr/span | ]]
        driver.find_element_by_xpath("//div[@id='WIN_4_7']/div/a/img").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Resolved'])[1]/following::td[2]").click()
        driver.find_element_by_id("arid_WIN_4_7").clear()
        driver.find_element_by_id("arid_WIN_4_7").send_keys("Closed")
        driver.find_element_by_id("arid_WIN_4_7").clear()
        driver.find_element_by_id("arid_WIN_4_7").send_keys("Closed")
        driver.find_element_by_xpath("//img[@alt='Menu for Status Reason']").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Infrastructure Change Created'])[1]/following::td[2]").click()
        driver.find_element_by_id("arid_WIN_4_1000000881").clear()
        driver.find_element_by_id("arid_WIN_4_1000000881").send_keys("Automated Resolution Reported")
        driver.find_element_by_xpath("//img[@alt='Menu for Status Reason']").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Infrastructure Change Created'])[1]/following::td[2]").click()
        driver.find_element_by_id("arid_WIN_4_1000000156").click()
        driver.find_element_by_id("arid_WIN_4_1000000156").clear()
        driver.find_element_by_id("arid_WIN_4_1000000156").send_keys("Issue has been resolved")
        driver.find_element_by_link_text("Categorization").click()
        driver.find_element_by_xpath("//a[@id='WIN_4_304287770']/div/div").click()
        driver.find_element_by_xpath("//img[@alt='Menu for Resolution Category']").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Authentication Services'])[1]/following::td[2]").click()
        driver.find_element_by_id("arid_WIN_4_1000002488").clear()
        driver.find_element_by_id("arid_WIN_4_1000002488").send_keys("Batch Processing")
        driver.find_element_by_xpath("//img[@alt='Menu for Resolution Category Tier 2']").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Transmission'])[1]/following::td[2]").click()
        driver.find_element_by_id("arid_WIN_4_1000003889").clear()
        driver.find_element_by_id("arid_WIN_4_1000003889").send_keys("UNIX")
        driver.find_element_by_xpath("//img[@alt='Menu for Resolution Category Tier 3']").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='▲'])[1]/following::td[1]").click()
        driver.find_element_by_id("arid_WIN_4_1000003890").clear()
        driver.find_element_by_id("arid_WIN_4_1000003890").send_keys("Application Erorr")
        driver.find_element_by_xpath("//img[@alt='Menu for Closure Product Category Tier1']").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Service'])[4]/following::td[2]").click()
        driver.find_element_by_id("arid_WIN_4_1000003891").clear()
        driver.find_element_by_id("arid_WIN_4_1000003891").send_keys("Software")
        driver.find_element_by_xpath("//img[@alt='Menu for Closure Product Category Tier2']").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='▲'])[1]/following::td[1]").click()
        driver.find_element_by_id("arid_WIN_4_1000003892").clear()
        driver.find_element_by_id("arid_WIN_4_1000003892").send_keys("Application")
        driver.find_element_by_xpath("//img[@alt='Menu for Closure Product Category Tier3']").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Operating system software'])[1]/following::td[2]").click()
        driver.find_element_by_id("arid_WIN_4_1000003893").clear()
        driver.find_element_by_id("arid_WIN_4_1000003893").send_keys("Other")
        driver.find_element_by_xpath("//img[@alt='Menu for Product Name (R)+']").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='▲'])[1]/following::td[1]").click()
        driver.find_element_by_id("arid_WIN_4_1000003894").clear()
        driver.find_element_by_id("arid_WIN_4_1000003894").send_keys("Active Directory Janitor")
        driver.find_element_by_xpath("//img[@alt='Menu for Model/Version (R)']").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='▲'])[1]/following::td[1]").click()
        driver.find_element_by_id("arid_WIN_4_1000003895").clear()
        driver.find_element_by_id("arid_WIN_4_1000003895").send_keys("1.2")
        driver.find_element_by_xpath("//a[@id='WIN_4_301614800']/div/div").click()
        driver.find_element_by_xpath("//a[@id='WIN_0_300000044']/div/div").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
