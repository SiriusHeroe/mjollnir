# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest
import time


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://10.100.10.248/Account/Login")

    def test_login(self):
        driver = self.driver

############Login in
        Username = "adminSept"
        Password = "123qwe"
        UserXpath = "//*[@id='UserName']"
        passXpath = "//*[@id='Password']"
        registrXpath = "//*[@id='loginForm']/form/div[4]/div/input"

        UserSignUpElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(UserXpath))
        passSignUpElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passXpath))
        registrElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(registrXpath))

        UserSignUpElement.send_keys(Username)
        passSignUpElement.send_keys(Password)
        registrElement.click()
        print("Entering in system is correct!")
        time.sleep(10)
###################
       
        def clik(Xpath):
            Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(Xpath))
            Element.click()
####################Create php build
        self.driver.get("https://10.100.10.248/PhpBuild/Create")
        self.assertIn("Create", driver.title)
        
        PhpName = "Autotest00"
        PhpXpath = "//*[@id='Name']"
        SubmitXpath = "/html/body/div[2]/form/div/div[8]/div/input"
        
        PhpSignUpElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(PhpXpath))
        SubmitElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(SubmitXpath))
        
        PhpSignUpElement.clear()
        PhpSignUpElement.send_keys(PhpName)
        SubmitElement.click()
        print("Creating php build is succesfully")
        time.sleep(3)
###################Create dll profile
        self.driver.get("https://10.100.10.248/DllProfile/Create")
        self.assertIn("Create", driver.title)
        
        DLLprofName = "Autotest00"
        Infodll = "!This program cannot be run in DOS mode.Microsoft Tablet PC Component6.1.7600.16385 (win7_rtm.090713-1255) Microsoft Corporation. All rights reserved."
        PoName = "Autotest00"
        DPXpath = "//*[@id='Name']"
        InXpath = "//*[@id='DllStrings']"
        PoXpath = ".//*[@id='fnName_1']"
        
        DPElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(DPXpath))
        InElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(InXpath))
        
        DPElement.send_keys(DLLprofName)
        InElement.send_keys(Infodll)
        clik(".//*[@id='dll_profile_form']/div/div[3]/div/a")
        
        FunNameElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(PoXpath))
        clik(".//*[@id='DllEntryPoints_IsRealEntryPoint__']")
        FunNameElement.send_keys(PoName)
        clik(".//*[@id='dll_profile_form']/div/div[6]/div/input")
        print("Creating dll profile is succesfully")
        time.sleep(3)
####################Create agent config
        self.driver.get("https://10.100.10.248/AgentConfig/Create")
        self.assertIn("Create", driver.title)            
            
        AgentName = "Autotest00"
        Serveradress = "http://10.100.10.245:80/nikolya_test/"
        AgentXpath = "//*[@id='ConfigName']"
        ServerXpath = "//*[@id='ServerAddress']"
        SubAgXpath = "/html/body/div[2]/form/div/div[5]/div/input"
        
        AgentSignUpElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(AgentXpath))
        ServerSignUpElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ServerXpath))
        SubmitAgElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(SubAgXpath))
        
        AgentSignUpElement.send_keys(AgentName)
        ServerSignUpElement.send_keys(Serveradress)
        clik(".//*[@id='PhpBuildId_chosen']/a/span")
        clik(".//*[@id='PhpBuildId_chosen']/div/ul/li[1]")
        SubmitAgElement.click()
        print("Creating agent config is succesfully")
        time.sleep(20)
#########################Create agent build
        self.driver.get("https://10.100.10.248/AgentBuild/Create")
        self.assertIn("Create", driver.title)
        AgBName = "Autotest00"
        AgBXpath = "//*[@id='Description']"
        AgSername = "Autotest00"
        AgSerXpath = "//*[@id='AgentConfigId_chosen']/div/div/input"
        DllSerName = "Autotest00"
        DllSerXpath = ".//*[@id='DllProfileId_chosen']/div/div/input"
        
        AgBElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(AgBXpath))
        AgSerElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(AgSerXpath))
        DllSeElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(DllSerXpath))
        
        AgBElement.send_keys(AgBName)
        clik(".//*[@id='AgentConfigId_chosen']/a/span")
        AgSerElement.send_keys(AgSername)
        AgSerElement.send_keys(Keys.RETURN)
        clik(".//*[@id='DllProfileId_chosen']")
        DllSeElement.send_keys(DllSerName)
        DllSeElement.send_keys(Keys.RETURN)
        clik("html/body/div[2]/form/div/div[6]/div/input")
        print("Creating agent build in processing")
        
    def tearDown(self):
        time.sleep(10)
        self.driver.close()
if __name__ == "__main__":
    unittest.main()