from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.common.exceptions import StaleElementReferenceException
from random import randint
# -*- coding: utf-8 -*- 

class LoginTest(unittest.TestCase):

    def SetUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2) # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.manager.dir', 'c:\\dist')
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'c:\\dist\\log')
        
        self.driver = webdriver.Firefox()
        self.driver.get(url)

    def test_login4(self):
        url = "https://10.100.10.240/Account/Login"
        SetUp(self, url)
        driver = self.driver
############Login in
        errc = 0
        Username = "adminSept"
        Password = "123qwe"
        UserXpath="//*[@id='UserName']"
        passXpath="//*[@id='Password']"
        registrXpath="//*[@id='loginForm']/form/div[4]/div/input"

        UserSignUpElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(UserXpath))
        passSignUpElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passXpath))
        registrElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(registrXpath))

        UserSignUpElement.send_keys(Username)
        passSignUpElement.send_keys(Password)
        registrElement.click()
        print("Entering in system is correct!")
###################        
        def clik(Xpath):
            Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(Xpath))
            Element.click()
    #########################Create agent build
        #self.driver.get("https://10.100.10.240/UserFiles/UploadedFiles")
        #self.assertIn("Uploaded", driver.title)

        #browser.find_element_by_xpath(".//*[@id='DataTables_Table_0']/tbody/tr[1]/td[8]/a[1]").click()

    def tearDown(self):
        time.sleep(10)
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
    