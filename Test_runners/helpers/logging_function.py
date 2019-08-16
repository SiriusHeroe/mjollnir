from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from random import randint
from collections import deque
from colorama import init, Fore, Back, Style
from threading import Thread
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

class logining(unittest.TestCase):

    def ini_File(self):
        my_file = open("_init_.txt", "r")
        p = 0
        line = my_file.readline()
        while line:
            p = p+1
            line = my_file.readline()
        my_file.close()
        return p


    def ini_Filedebug():
        if not os.path.isfile("_init_.txt"):
            return 0
        my_file = open("_init_.txt", "r")
        p = 0
        line = my_file.readline()
        while line:
            p = p + 1
            # print(line)
            line = my_file.readline()
        # print(line)
        my_file.close()
        if not os.path.exists("c:\\logs"):
            os.makedirs("c:\\logs")
        return p
    def error_log(self, count, filename, massage=""):
        print("Test result ", Back.RED + "Error", Style.RESET_ALL, ". Command number:" + str(count))
        print(Style.RESET_ALL, end='\r')
        my_file = open(filename, "a")
        my_file.write("Result test is Error. Command number:")
        my_file.write(str(count))
        my_file.write(str(massage))
        my_file.write("\n")
        my_file.write("\n")
        my_file.close()
        return count

    def success_log(self, count, filename, massage=""):
        #print("Test result ", Back.GREEN + "Success",  Style.RESET_ALL, ". Command number:" + str(count))
        #print(Style.RESET_ALL, end='\r')
        #thread1 = Thread(target=testindid.jaba)
        #testindid.gipno_jaba()
        my_file = open(filename, "a")
        my_file.write("Result test is Success. Command number:")
        my_file.write(str(count))
        my_file.write(str(massage))
        my_file.write("\n")
        my_file.write("\n")
        my_file.close()
        #thread1.start()
        #thread1.join()
        return count

    def gipno_jaba():
        Nabor = " ", "░", "▒", "▓", "█", "▓", "▒", "░"
        x = 0
        while x < 9:
            time.sleep(0.08)
            # print('\r%s' % (Nabor[x]), str(time.strftime("%Y_%m_%d_%H.%S", time.localtime())), end = '\r')
            print('\r', str(time.strftime("%Y_%m_%d_%H", time.localtime())), '%s' % (Nabor[x]),
                  str(time.strftime("%S", time.localtime())), end='\r')
            x = x + 1
            if x == 8:
                pass
                #x = 0

    def warning_log(self, count, filename, massage=""):
        #print(Back.CYAN + "Test result use in other test. Command number:" + str(count))
        #print(Style.RESET_ALL, end='\r')
        my_file = open(filename, "a")
        my_file.write("Result test is Success. Command number:")
        my_file.write(str(count))
        my_file.write(str(massage))
        my_file.write("\n")
        my_file.write("\n")
        my_file.close()
        return count
