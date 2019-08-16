from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from random import randint
from collections import deque
from colorama import init, Fore, Back, Style
from threading import Thread
from helpers.logging_function import *
import settings
import importlib
import unittest
import time
import datetime
import sys
import queue
import threading
import os
import hashlib
import json
import random
import sys
init()


class test_executor(logining):

    def SetUp(self, url):  # star brows
        # self.driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        print(settings.test_string)
        self.driver = webdriver.Firefox()
        self.driver.get(url)

    def connect(self, url, Username, Password):  # login in server
        print("Get to agent server:"+str(url))
        test_executor.SetUp(self, url)
        driver = self.driver
######## Log in
        UserXpath = ".//*[@id='UserName']"
        passXpath = ".//*[@id='Password']"
        registrXpath = "//*[@id='loginForm']/form/div[4]/div/input"
        check1Xpath = ".//*[@id='logoutForm']/ul/li[1]/a"
########
        UserSignUpElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(UserXpath))
        passSignUpElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passXpath))
        registrElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(registrXpath))
########
        UserSignUpElement.send_keys(Username)
        passSignUpElement.send_keys(Password)
        registrElement.click()
        time.sleep(1)
        try:
            check_flag = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(check1Xpath)).text
        except:
            print("Logon isn't possible authorization error!!")
        else:
            print("Entering in system is correct!")

    def executor_command(self, com, count, filename):
        driver = self.driver
        print(Back.YELLOW, end='\r')
        time.sleep(2)
        areaXpath = "//*[@id='message']"
        msg = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(areaXpath))
        time.sleep(3)
        msg.send_keys(com)
        time.sleep(3)
        msg.send_keys(Keys.RETURN)
        count = count + 1
        CommandResultXpath = "//*[@id='agent_command_" + str(count) + "']/td[5]"
        CommandOutputXpath = "//*[@id='agent_command_" + str(count) + "']/td[3]"
        CommandDatatimeXpath = ".//*[@id='agent_command_" + str(count) + "']/td[4]"
        while True:
            time.sleep(1)
            CommandResultElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandResultXpath))
            try:
                Result = CommandResultElement.text
            except StaleElementReferenceException:
                print("Exception")
                print("Explorer lost the reply box or the DOM tree has been updated!")
                time.sleep(1)
                CommandResultElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandResultXpath))
                try:
                    Result = CommandResultElement.text
                except StaleElementReferenceException:
                    time.sleep(1)
                    CommandResultElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandResultXpath))
                    Result = CommandResultElement.text
                    print("Exception")
                    print("Explorer lost the reply box or the DOM tree has been updated!")
            if Result == "Success":
                #print(Back.CYAN, end='\r')
                #print("\r" + str(count) + " - " + com + " - " + Result)
                break
            if Result == "AgentError":
                Result = "Error"
                print(Back.CYAN, end='\r')
                print(str(count) + " - " + com + " - " + Result)
                break
            if Result == "ServerError":
                Result = "Error"
                print(Back.CYAN, end='\r')
                print(str(count) + " - " + com + " - " + Result)
                break
        CommandOutputElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandOutputXpath))
        CommandDatatimeElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandDatatimeXpath))
        CommandResultElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandResultXpath))
        my_file = open(filename, "a")
        log_time = CommandDatatimeElement.text
        log_date = CommandOutputElement.text
        log_result = CommandResultElement.text
        my_file.write("Command number:"+str(count)+". ")
        my_file.write(str(log_time).split(" ")[1]+". ")
        my_file.write("Body command '"+str(com)+"'. ")
        my_file.write("Web console result: "+str(log_result)+" ")
        my_file.write("\n")
        my_file.close()
        print(Style.RESET_ALL, end='\r')
        return count, Result

    def clik(self, Xpath):  # castom click for bag situation
        driver = self.driver
        Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(Xpath))
        Element.click()
        return 0

    def getOutput(self, count):  # castom print output resault
        driver = self.driver

        time.sleep(1)
        CommandOutputXpath = "//*[@id='agent_command_" + str(count) + "']/td[3]/div"
        CommandOutputElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandOutputXpath))
        return CommandOutputElement.text

    def upload(self, com, filename, count, flag=0):  # custom upload files on web
        driver = self.driver

        massageXpath = "//*[@id='message']"
        MassegeElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(massageXpath))
        if flag == 0:
            MassegeElement.send_keys("put")
        if flag == 1:
            MassegeElement.send_keys("lddll2")
        if flag == 2:
            MassegeElement.send_keys("lddllr")
        time.sleep(15)
        driver = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='" + str(com) + "']"))
        driver.click()
        time.sleep(10)
        MassegeElement.send_keys(Keys.RETURN)  # принудительное выполнение
        time.sleep(3)
        count = count + 1
        print("Exception")
        if flag == 0:
            count = self.command_new("cd", count, filename)
            return count
        else:
            CommandResultXpath = "//*[@id='agent_command_" + str(count) + "']/td[5]"
            while True:
                time.sleep(1)
                CommandResultElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandResultXpath))
                try:
                    Result = CommandResultElement.text
                except StaleElementReferenceException:
                    print("Exception")
                    time.sleep(1)
                    CommandResultElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandResultXpath))
                    try:
                        Result = CommandResultElement.text
                    except StaleElementReferenceException:
                        time.sleep(1)
                        CommandResultElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(CommandResultXpath))
                        Result = CommandResultElement.text
                        print("Exception")
                if Result == "Success":
                    print("\r" + str(count) + " - " + com + " - " + Result)
                    return count, Result
                    break
                if Result == "AgentError":
                    print(str(count) + " - " + com + " - " + Result)
                    return count, Result
                    break
                if Result == "ServerError":
                    print(str(count) + " - " + com + " - " + Result)
                    return count, Result
                    break

    def searchidcom(self, count):  # search last command id
        driver = self.driver
        if count == 0:
#################################################
            areaXpath = "//*[@id='message']"
            msg = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(areaXpath))
            time.sleep(3)
            #msg.send_keys("cd")
            maxi = 1

            while count < maxi:
                point = random.randint(1, 3)
                if point == 1:
                    msg.send_keys("cd")
                    msg.send_keys(Keys.RETURN)
                if point == 2:
                    msg.send_keys("pwd")
                    msg.send_keys(Keys.RETURN)
                if point == 3:
                    msg.send_keys("ls")
                    msg.send_keys(Keys.RETURN)
                count = count + 1

                time.sleep(0.7)
            time.sleep(3)
            msg.send_keys(Keys.RETURN)
#################################################
            countXpath = "/html/body/div[2]/div[1]/div[4]//tr[position() = 1]/td[position() = 1]"
            time.sleep(1)
            countElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(countXpath))
            count_s = countElement.text
            print(str(count_s))
            time.sleep(5)
            l = []
            for t in count_s.split():
                try:
                    l.append(float(t))
                except ValueError:
                    pass
            print(l)
            return int(l[0])
        else:
            if type(count) != int:
                areaXpath = "//*[@id='message']"
                msg = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(areaXpath))
                time.sleep(3)
                msg.send_keys("cd")
                time.sleep(3)
                msg.send_keys(Keys.RETURN)
                #################################################
                countXpath = "/html/body/div[2]/div[1]/div[4]//tr[position() = 1]/td[position() = 1]"
                time.sleep(1)
                countElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(countXpath))
                count_s = countElement.text
                print(str(count_s))
                time.sleep(5)
                l = []
                for t in count_s.split():
                    try:
                        l.append(float(t))
                    except ValueError:
                        pass
                print("Id last executed command : ", l)
                return int(l[0])
            else:
                return count

    def json_parse():
        if not os.path.isfile(settings.file_str):
            pass
        else:
            os.remove(settings.file_str)
        with open(settings.hand_test_run, 'r') as fi:
            data = json.load(fi)
        num_rec = len(data[0])
        print("Counting the number of tests...")
        for i in range(num_rec):
             print(i)
             with open(settings.file_str,'a',encoding = 'utf-8') as fi:
                fi.write(str(data[0]["case_"+str(i)][0]["command"])+"//"+str(data[0]["case_"+str(i)][0]["parameters"]))
                fi.write("\n")
        if settings.debug_toggle == False:
            os.remove(settings.file_str)
        print("Found total "+str(num_rec)+" tests.")
        return data, num_rec

    def restructor():  # Function for parsing login date(pass, login, url)
        i = 0
        for l in range(len(settings.test_suite)):
            if settings.work_id == i:
                # print('work_id - ',settings.work_id)

                if settings.test_suite[l]["enable_flag"] == True:

                    settings.work_login = settings.test_suite[l]["host_login"] + '/Account/Login'
                    # print("Server address - ", settings.test_suite[l]["host_login"])

                    settings.work_address = settings.test_suite[l]["host_login"] + '/InstalledAgent/Console/' + str(
                        settings.test_suite[l]["host_agent_address"])
                    # print("Id testable console - ",settings.test_suite[l]["host_agent_address"])

                    settings.work_name = settings.test_suite[l]["login_name"]
                    # print("Name user - ", settings.test_suite[l]["login_name"])

                    settings.work_pass = settings.test_suite[l]["login_pass"]
                    # print("User's password - ", settings.test_suite[l]["login_pass"])

                    settings.work_id = i + 1
                    # print("Full address testable console - ", settings.work_address)
                    return 0
                else:
                    settings.work_id = i + 1
            i = i + 1

