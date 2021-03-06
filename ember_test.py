# -*- coding: utf-8 -*-
from pyvirtualdisplay import Display
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Testember(unittest.TestCase):
    #display = Display(visible=0, size=(800, 600))
    #display.start()
    def setUp(self):
        display = Display(visible=0, size=(1366, 768))
        display.start()
        #self.driver.set_window_size(1366, 768)
        #firefoxPath="/home/cb/Downloads/geckodriver"
        firefoxPath="/home/ci/geckodriver"
        self.driver = webdriver.Firefox(executable_path=firefoxPath)
        #phantomjsPath="/home/cb/Desktop/temp/phantomjs-1.9.8-linux-x86_64/bin/phantomjs"
        #self.driver = webdriver.PhantomJS(executable_path=phantomjsPath)
    	#chromePath="/usr/bin/chromedriver"
    	#self.driver = webdriver.Chrome(executable_path=chromePath)
        #firefoxPath="/usr/bin/geckodriver"
        #self.driver = webdriver.Firefox(executable_path=firefoxPath)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://20.10.83.21:4200/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ember(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("ember258").click()
        driver.find_element_by_id("ember263").click()
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("abc@fff.com")
        driver.find_element_by_id("inputComments").clear()
        driver.find_element_by_id("inputComments").send_keys("gggfgfg")
        driver.find_element_by_css_selector("button.btn.btn-default").click()
    
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
