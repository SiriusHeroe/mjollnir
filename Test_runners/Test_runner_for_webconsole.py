# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from random import randint
from collections import deque
from colorama import init, Fore, Back, Style
from threading import Thread
import settings
from helpers.system_func import *
from test_func import *
from helpers.logging_function import *
import importlib
import unittest
import time
import datetime
import sys
import queue
import threading
import os
import hashlib
init()



def trigger():
    suite = unittest.TestSuite()
    l = 0
    if settings.key == "all":
        for l in range(len(settings.test_suite)):
            retry = test_executor.restruktor()
            if retry == 0:
                suite.addTest(testsall("test_for_debugging"))
            return suite
    sys.exit()

def booster():
    suite = unittest.TestSuite()
    l = 0
    print("ok5")
    for l in range(len(settings.test_suite)):
        retry = test_executor.restructor()
        if retry == 0:
            #thread1 = Thread(target=testindid.jaba)
            thread2 = Thread(target=suite.addTest(tests_all("test_4")))
            thread2.start()
            #thread1.start()
            thread2.join()
            #thread1.join()
        return suite



if __name__ == '__main__':
    if settings.hand_test == True:
        try:
            p = logining.ini_Filedebug()
            my_file = open("_init_.txt", "a")
            p = p+1
            my_file.write(str(p))
            my_file.write(str(time.strftime("_%Y_%m_%d_%H_%M_%S", time.localtime())))
            my_file.write("\n")
            my_file.close()
            print("try1")
        except:
            print("Error in process create fail 'init'")
            sys.exit(-1)
        else:
            print("try2")
            try:
                if settings.restart_toggle == True:
                    print("ok1")
                    while settings.howcomplete_test+1 != settings.howmany_test:
                        settings.howcomplete_test = 0
                        runner = unittest.TextTestRunner()
                        l = 0
                        for l in range(len(settings.test_suite)):
                            if settings.test_suite[l]["enable_flag"] == True:
                                runner.run(booster())
                    print("ok2")

                else:
                    print("ok3")
                    runner = unittest.TextTestRunner()
                    print("ok4")
                    l = 0
                    for l in range(len(settings.test_suite)):
                        if settings.test_suite[l]["enable_flag"] == True:
                            runner.run(booster())
                    print("error1")
            except Exception:
                #sys.stderr.write(Back.RED +"Test finished with fatal error! Please restart test.")
                print(Back.RED +"Test finished with fatal error! Please restart test.")
                sys.exit(-1)
            else:
                print(settings.howcomplete_test+1, settings.howmany_test)
                if settings.howcomplete_test+1 == settings.howmany_test:
                    print(Back.GREEN + "Test finished Successed! Good luck!")
                else:
                    print(Back.RED +"Test finished with fatal error! Please restart test.")
                    sys.exit(-1)
            #input("Press enter")"""
    else:
        try:
            p = ini_Filedebug()
            my_file = open("_init_.txt", "a")
            p = p+1
            my_file.write(str(p))
            my_file.write(str(time.strftime("_%Y_%m_%d_%H_%M_%S", time.localtime())))
            my_file.write("\n")
            my_file.close()
        except:
            print("Error in process create fail 'init'")
            sys.exit(-1)
        else:
            runner = unittest.TextTestRunner()
            for flag_id in settings.flags:
                if flag_id == 1:
                    runner.run(trigger())
            #input("Press enter")
    sys.exit()