# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from random import randint
from collections import deque
from colorama import init, Fore, Back, Style
from helpers.system_func import *
from helpers.logging_function import *
from settings import *
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

__version__ = "$Revision: 5.2 $"


class tests_all(test_executor):
    ########################################################################################################################
    ############################################################## _For old test_ ##########################################
    def uploading_many_files(self, flag, count):
        if flag == 0:  # files for 248 server
            time.sleep(3)
            count = test_executor.upload(self, "181", count)
            time.sleep(3)
            count = test_executor.upload(self, "11", count)
            time.sleep(3)
            count = test_executor.upload(self, "8", count)
            time.sleep(3)
            count = test_executor.upload(self, "7", count)
            time.sleep(3)
            count = test_executor.upload(self, "6", count)
            time.sleep(3)
            count = test_executor.upload(self, "5", count)
            time.sleep(3)
            count = test_executor.upload(self, "4", count)
            time.sleep(3)
        else:  # files for 240 server
            time.sleep(3)
            count = test_executor.upload(self, "33", count)
            time.sleep(3)
            count = test_executor.upload(self, "17", count)
            time.sleep(3)
            count = test_executor.upload(self, "16", count)
            time.sleep(3)
            count = test_executor.upload(self, "15", count)
            time.sleep(3)
            count = test_executor.upload(self, "14", count)
            time.sleep(3)
            count = test_executor.upload(self, "13", count)
            time.sleep(3)
            count = test_executor.upload(self, "12", count)
            time.sleep(3)
        return count

    ##############################################################################################################################################
    ##############################################################################################################################################

    def go_to_string(self, count, filename, file_str="Resurs.py"):
        if not os.path.isfile(file_str):
            return 0
        else:
            f = open(file_str)
            for line in f.readlines():
                command = line.split("!")
                count, answer = test_executor.executor_command(self, command[1], count, filename)
        if answer.encode('utf-8') in command[2].encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def cd_test(self, filename, suffix=" ", result="Success", count=0):
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "cd " + suffix, count, filename)
        ##print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
            else:
                count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def pwd_test(self, filename, suffix=" ", result="Success", count=0):
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "pwd " + suffix, count, filename)
        ##print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def ls_test(self, filename, suffix=" ", search="", result="Success", count=0):
        ##print("Search option : ", "# - "+str(count)+" - "+str(suffix)+" - "+str(search))
        count = test_executor.searchidcom(self, count)
        flag = "1"
        count, ansver = test_executor.executor_command(self, "ls " + suffix, count, filename)
        ##print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
            else:
                count = logining.success_log(self, count, filename)
            output = test_executor.getOutput(self, count)
            if search != "":
                file = open("string_forls.txt", "w+")
                file.write(output)
                file.close
                with open("string_forls.txt", "r") as file:
                    for line in file:
                        if search in line:
                            ##print("Successful search : ", search)
                            my_file = open(filename, "a")
                            my_file.write("_____Conformity test is Success. Command number:")
                            my_file.write(str(count))
                            my_file.write("\n")
                            # print(str(count)+"~~~~~~~~"+str(line))
                            return count, line
                            flag = 0
                            break
                if flag == "1":
                    ##print("Not found - '"+search+"' in line - '"+line+"'")
                    ##print("Successful search : ", search)
                    my_file = open(filename, "a")
                    my_file.write("_____Conformity test is Error. Command number:")
                    my_file.write(str(count))
                    my_file.write("\n")
                    return count, flag
            else:
                return count
        else:
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
                return count, flag
            else:
                count = logining.error_log(self, count, filename)
                return count

    def dl_test(self, filename, suffix=" ", result="Success", count=0):
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "dl " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def agentinfo_test(self, filename, target="", prefix="OS Name", suffix="", result="Success",
                       count=0):  # 47 string information about agent
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "agentinfo " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
            else:
                count = logining.success_log(self, count, filename)
        else:
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
            else:
                count = logining.error_log(self, count, filename)
            return count
        time.sleep(3)
        # print("Search string - ", str(target))
        if target == "":
            return count
        else:
            if ansver.encode('utf-8') == result.encode('utf-8'):
                output = test_executor.getOutput(self, count)
                file = open("string_foragent.txt", "w+")
                file.write(output)
                file.close
                with open("string_foragent.txt", "r") as file:
                    for line in file:
                        if prefix in line:
                            if target in line:
                                # print("Successful search : ", target)
                                my_file = open(filename, "a")
                                my_file.write(str(target))
                                my_file.write("_____Conformity test is Success. Command number:")
                                my_file.write(str(count))
                                my_file.write("\n")
                                my_file.close()
                                flag = "0"
                                return count, flag, line
                            else:
                                # print("Not found - '"+target+"' in line - '"+line+"'")
                                # print("Unsuccessful search : ", target)
                                my_file = open(filename, "a")
                                my_file.write("_____Conformity test is Error. Command number:")
                                my_file.write(str(count))
                                my_file.write("\n")
                                my_file.close()
                                flag = "1"
                                return count, flag, line

    def sysinfo_test(self, filename, target="", prefix="Host Name", suffix="", result="Success",
                     count=0):  # 39 string information about pc target
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "sysinfo " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
            else:
                count = logining.success_log(self, count, filename)
        else:
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
            else:
                count = logining.error_log(self, count, filename)
            return count
        if target == "":
            return count
        else:
            if ansver.encode('utf-8') == result.encode('utf-8'):
                output = test_executor.getOutput(self, count)
                file = open("string_forsys.txt", "w+")
                file.write(output)
                file.close
                with open("string_forsys.txt", "r") as file:
                    for line in file:
                        if prefix in line:
                            if target in line:
                                # print("Successful search : ", target)
                                my_file = open(filename, "a")
                                my_file.write("_____Conformity test is Success. Command number:")
                                my_file.write(str(count))
                                my_file.write("\n")
                                my_file.close()
                                return count
                            else:
                                # print("Not found - '"+target+"' in line - '"+line+"'")
                                # print("Unsuccessful search: ", target)
                                my_file = open(filename, "a")
                                my_file.write("_____Conformity test is Error. Command number:")
                                my_file.write(str(count))
                                my_file.write("\n")
                                my_file.close()
                                return count

    def env_test(self, filename, suffix="", result="Success", count=0):  # create or show environment variables
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "env " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
        else:
            count = logining.error_log(self, count, filename)
            return count
        check = 0
        if "=" in suffix:
            if ansver.encode('utf-8') == result.encode('utf-8'):
                suffix = suffix.replace("=", " ", 1)
                output = test_executor.getOutput(self, count)
                if output == suffix:
                    # print("Success: ", suffix)
                    my_file = open(filename, "a")
                    my_file.write("_____Conformity test is Success. Command number:")
                    my_file.write(str(count))
                    my_file.write("\n")
                    return count
                else:
                    # print("Not found - '"+suffix+"' in line - '"+output+"'")
                    # print("Unsuccess: ", suffix)
                    my_file = open(filename, "a")
                    my_file.write("_____Conformity test is Error. Command number:")
                    my_file.write(str(count))
                    my_file.write("\n")
                    return count
        else:
            if suffix != "" and ansver.encode('utf-8') == result.encode('utf-8'):
                output1 = test_executor.getOutput(self, count)
                count, ansver = test_executor.executor_command(self, "env ", count, filename)
                output2 = test_executor.getOutput(self, count)
                file = open("string_forenv.txt", "w+")
                file.write(output2)
                file.close
                with open("string_forenv.txt", "r") as file:
                    for line in file:
                        if suffix in line:
                            # print(str(line))
                            if output1 in line:
                                # print("Success: ", output1)
                                my_file = open(filename, "a")
                                my_file.write("_____Conformity test is Success. Command number:")
                                my_file.write(str(count))
                                my_file.write("\n")
                                my_file.close()
                                check = check + 1
                            else:
                                # print("Not found - '"+output1+"' in line - '"+line+"'")
                                my_file = open(filename, "a")
                                my_file.write("_____Conformity test is Error. Command number:")
                                my_file.write(str(count))
                                my_file.write("\n")
                                my_file.close()
                                return count
                            if check == 2:
                                # print(Back.RED + "Critical error - '"+output1+"' in output more than once!", Style.RESET_ALL, end="\r")
                                my_file = open(filename, "a")
                                my_file.write("_____Conformity test is Error. Command number:")
                                my_file.write(str(count))
                                my_file.write("\n")
                                my_file.close()
                                return count
            else:
                return count

    def datetime_test(self, filename, suffix="", result="Success", count=0):
        count = test_executor.searchidcom(self, count)
        check1 = 0
        check2 = 0
        count, ansver = test_executor.executor_command(self, "date " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            check1 = 1
        count, ansver = test_executor.executor_command(self, "time " + suffix, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            check2 = 1
        if check1 == 1 and check2 == 1:
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def tasklist_test(self, filename, suffix="", search="", result="Success", count=0):
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "ps " + suffix, count, filename)
        resault = ""
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
            else:
                count = logining.success_log(self, count, filename)
            if search != "":
                output = test_executor.getOutput(self, count)
                file = open("string_fortask.txt", "w+")
                file.write(output)
                file.close
                resault1 = "0"
                if search != "":
                    with open("string_fortask.txt", "r") as file:
                        for line in file:
                            if search in line:
                                resault1 = line
                                return count, resault1
                    if resault1 == "0":
                        return count, resault1
            return count
        else:
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
            else:
                count = logining.error_log(self, count, filename)
            return count

    def listpipes_test(self, filename, suffix="", search="", result="Success", count=0):
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "listpipes " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        # print("Search optinon : ","# - ", count, " - ", search)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if search != "":
                if settings.result_flag == 1:
                    count = logining.warning_log(self, count, filename)
                else:
                    count = logining.success_log(self, count, filename)
            else:
                if settings.result_flag == 1:
                    count = logining.warning_log(self, count, filename)
                else:
                    count = logining.success_log(self, count, filename)
                return count, search
        else:
            if settings.result_flag == 1:
                count = logining.warning_log(self, count, filename)
            else:
                count = logining.error_log(self, count, filename)
            search = ""
            return count, search
        output = test_executor.getOutput(self, count)
        file = open("string_forlist.txt", "w+")
        file.write(output)
        file.close
        succsessresault = "0"
        if search != "":
            with open("string_forlist.txt", "r") as file:
                for line in file:
                    if search in line:
                        # print("Success pipes '"+str(search)+"' is opened. Command number -"+str(count))
                        my_file = open(filename, "a")
                        my_file.write("_____Conformity test is Success. Command number:")
                        my_file.write(str(count))
                        my_file.write("\n")
                        return count, line
            if succsessresault == "0":
                # print("Not found - '"+search+"' in line - '"+line+"'")
                # print("Error: ", count)
                my_file = open(filename, "a")
                my_file.write("_____Conformity test is Error. Command number:")
                my_file.write(str(count))
                my_file.write("\n")
                return count, succsessresault

    def listld_test(self, filename, suffix="", search="", type="", adress="", count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "listld " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        search = search + adress + type
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if suffix == "-a" or suffix == "":
                if search == "":
                    if settings.result_flag == 1:
                        count = logining.warning_log(self, count, filename)
                    else:
                        count = logining.success_log(self, count, filename)
                    return count
            else:
                if settings.result_flag == 1:
                    count = logining.warning_log(self, count, filename)
                else:
                    count = logining.error_log(self, count, filename)
                return count
        output = test_executor.getOutput(self, count)
        file = open("string_forld.txt", "w+")
        file.write(output)
        file.close
        succsessresault = 0
        if search != "" and type == "":
            if suffix == "-a" or suffix == "":
                with open("string_forld.txt", "r") as file:
                    for line in file:
                        if search in line:
                            # print("Success library '"+search+"' is searched. Command number -"+count)
                            my_file = open(filename, "a")
                            my_file.write("_____Conformity test is Success. Command number:")
                            my_file.write(str(count))
                            my_file.write("\n")
                            succsessresault = 1
                if succsessresault == 0:
                    # print("Not found - '"+search+"' in line - '"+output+"'")
                    # print("Error: ", count)
                    my_file = open(filename, "a")
                    my_file.write("_____Conformity test is Error. Command number:")
                    my_file.write(str(count))
                    my_file.write("\n")
        else:
            if suffix == "-a" or suffix == "":
                with open("string_forld.txt", "r") as file:
                    for line in file:
                        if search in line:
                            if type in line:
                                # print("Success dll '"+str(search)+"' is opened. Command number -"+str(count))
                                my_file = open(filename, "a")
                                my_file.write("_____Conformity test is Success. Command number:")
                                my_file.write(str(count))
                                my_file.write("\n")
                                succsessresault = 1
                if succsessresault == 0:
                    # print("Not found - '"+search+"' in line - '"+output+"'")
                    # print("Error: ", count)
                    my_file = open(filename, "a")
                    my_file.write("_____Conformity test is Error. Command number:")
                    my_file.write(str(count))
                    my_file.write("\n")

    def listexp_test(self, filename, suffix="", search="", count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "listexp " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        succsessresault = 0
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if suffix != "":
                count = logining.success_log(self, count, filename)
                output = test_executor.getOutput(self, count)
                file = open("string_forexp.txt", "w+")
                file.write(output)
                file.close
                if search != "":
                    with open("string_forexp.txt", "r") as file:
                        for line in file:
                            if search in line:
                                # print("Success search function '"+search+"' is found in line '"+line+"'. Command number - "+str(count))
                                my_file = open(filename, "a")
                                my_file.write("_____Conformity test is Success. Command number:")
                                my_file.write(str(count))
                                my_file.write("\n")
                                succsessresault = 1
                    if succsessresault == 0:
                        # print("Is Not found - '"+search+"' in line - '"+output+"'")
                        # print("Error: ", count)
                        my_file = open(filename, "a")
                        my_file.write("_____Conformity test is Error. Command number:")
                        my_file.write(str(count))
                        my_file.write("\n")
                        return count
                    return count
            else:
                count = logining.error_log(self, count, filename)
                return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def md5_test(self, filename, suffix="", search="", namefile="", result="Success", count=0):
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "md5 " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        succsessresault = 0
        if search == "" and namefile != "":
            search = hashlib.md5(open(namefile, "rb")).hexdigest()
            # print(search)
        else:
            # print("Case don't has control value.")
            if ansver.encode('utf-8') == result.encode('utf-8'):
                count = logining.success_log(self, count, filename)
                return count
            else:
                count = logining.error_log(self, count, filename)
                return count

        if ansver.encode('utf-8') == result.encode('utf-8'):
            if suffix != "":
                count = logining.success_log(self, count, filename)
                output = test_executor.getOutput(self, count)
                # print(str(search)+"_____"+str(output))
                if search != "":
                    if search == output:
                        # print("Success string '"+search+"'. Command number -"+str(count))
                        my_file = open(filename, "a")
                        my_file.write("_____Conformity test is Success. Command number:")
                        my_file.write(str(count))
                        my_file.write("\n")
                        succsessresault = 1
                        return count
                    if succsessresault == 0:
                        # print("Not found - '"+search+"' in line - '"+output+"'")
                        # print("Error: ", count)
                        my_file = open(filename, "a")
                        my_file.write("_____Conformity test is Error. Command number:")
                        my_file.write(str(count))
                        my_file.write("\n")
                        return count
            else:
                count = logining.error_log(self, count, filename)
                return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def mkdir_test(self, filename, suffix="", prefix="", result="Success", count=0):
        settings.result_flag = 1
        count = test_executor.searchidcom(self, count)
        if prefix == "" or prefix == " ":
            count, ansver = test_executor.executor_command(self, "mkdir " + suffix, count, filename)
            # print("Obtained result : ", ansver, ". Expected result : ", result)
            search = suffix
        else:
            count, ansver = test_executor.executor_command(self, "mkdir '" + prefix + "\\" + suffix + "'", count, filename)
            # print("Obtained result : ", ansver, ". Expected result : ", result)
            search = prefix + "\\" + suffix
            # print("Search option : ","# - ", count, " - "+str(search))
        if ansver.encode('utf-8') == result.encode('utf-8') and result.encode('utf-8') == "Success".encode('utf-8'):
            if suffix != "":
                count = logining.success_log(self, count, filename)
                output = test_executor.getOutput(self, count)
                if ":" in prefix:
                    count = test_executor.searchidcom(self, count)
                    count, result1 = testsall.ls_test(self, filename, suffix=prefix, search=suffix, count=count)
                    if suffix in result1:
                        # print("Successful search : ", result1)
                        my_file = open(filename, "a")
                        my_file.write("_____Conformity test is Success. Command number:")
                        my_file.write(str(count))
                        my_file.write("\n")
                    settings.result_flag = 0
                    return count
                if "\\" in search:
                    count = test_executor.searchidcom(self, count)
                    count = testsall.cd_test(self, filename)
                    output = test_executor.getOutput(self, count)
                    resault = output + "\\" + prefix
                    count, result1 = testsall.ls_test(self, filename, suffix=resault, search=suffix, count=count)
                    if suffix in result1:
                        # print("Successful search : ", result1)
                        my_file = open(filename, "a")
                        my_file.write("_____Conformity test is Success. Command number:")
                        my_file.write(str(count))
                        my_file.write("\n")
                    settings.result_flag = 0
                    return count
                else:
                    count = test_executor.searchidcom(self, count)
                    # print(count, "----", suffix)
                    count, resault = testsall.ls_test(self, filename, suffix="", search=suffix, count=count)
                    # print(count, "----", resault)
                    if resault == 1 or resault == "1":
                        count = logining.error_log(self, count, filename)
                        settings.result_flag = 0
                        return count
                    else:
                        if suffix in resault:
                            # print("Successful search : ", resault)
                            my_file = open(filename, "a")
                            my_file.write("_____Conformity test is Success. Command number:")
                            my_file.write(str(count))
                            my_file.write("\n")
                            settings.result_flag = 0
                            return count
            else:
                count = logining.error_log(self, count, filename)
                settings.result_flag = 0
                return count
        else:
            if result.encode('utf-8') == "Error".encode('utf-8'):
                count = logining.success_log(self, count, filename)
                settings.result_flag = 0
                return count
            else:
                count = logining.error_log(self, count, filename)
                settings.result_flag = 0
                return count

    def rm_test(self, filename, suffix="", prefix="", count=0):
        result = "Success"
        settings.result_flag = 1
        flag = 1
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "rm " + prefix + suffix, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if prefix == "":
                count, resault = testsall.ls_test(self, filename, suffix=" ", search=suffix, count=count)
                if resault == 1:
                    count = logining.success_log(self, count, filename)
                    settings.result_flag = 0
                    return count
            else:
                if ":" in prefix:
                    count, resault = testsall.ls_test(self, filename, prefix, suffix, count=count)
                    if resault == 1:
                        count = logining.success_log(self, count, filename)
                        settings.result_flag = 0
                        return count
                else:
                    testsall.cd_test(self, filename, " ")
                    output = test_executor.getOutput(self, count)
                    way = str(output) + str(prefix)
                    count, resault = testsall.ls_test(self, filename, way, suffix, count=count)
                    if resault == 1:
                        count = logining.success_log(self, count, filename)
                        settings.result_flag = 0
                        return count
            if flag != 1:
                count = logining.error_log(self, count, filename)
                settings.result_flag = 0
                return count
        else:
            count = logining.error_log(self, count, filename)
            settings.result_flag = 0
            return count

    def rmdir_test(self, filename, suffix="", prefix="", specific="", count=0):
        result = "Success"
        flag = 1
        settings.result_flag = 1
        count = test_executor.searchidcom(self, count)
        if specific == "-rf":
            count, ansver = test_executor.executor_command(self, "rmdir " + specific + " " + prefix + suffix, count, filename)
        else:
            count, ansver = test_executor.executor_command(self, "rmdir " + prefix + suffix, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if prefix == "":
                count, resault = testsall.ls_test(self, filename, suffix=" ", search=suffix, count=count)
                if resault == 1:
                    count = logining.success_log(self, count, filename)
                    settings.result_flag = 0
                    return count
                else:
                    count = logining.error_log(self, count, filename)
                    settings.result_flag = 0
                    return count
            else:
                if ":" in prefix:
                    count, resault = self.ls_test(filename, suffix=" ", search=suffix, count=count)
                    if resault == 1:
                        count = logining.success_log(self, count, filename)
                        settings.result_flag = 0
                        return count
                else:
                    count = testsall.cd_test(self, filename, " ", count=count)
                    output = test_executor.getOutput(self, count)
                    way = str(output) + str(prefix)
                    count, resault = testsall.ls_test(self, filename, suffix=way, search=suffix, count=count)
                    if resault == 1:
                        count = logining.success_log(self, count, filename)
                        settings.result_flag = 0
                        return count
            if flag == 1:
                count = logining.error_log(self, count, filename)
                settings.result_flag = 0
                return count
        else:
            count = logining.error_log(self, count, filename)
            settings.result_flag = 0
            return count

    def taskkill_test(self, filename, suffix="", prefix="-im", count=0):
        result = "Success"
        settings.result_flag = 1
        check = 0
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "taskkill " + prefix + " " + suffix, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if suffix != "":
                if prefix == "-pid":
                    inf = "Process with id: " + suffix + " successfully terminated"
                    output = test_executor.getOutput(self, count)
                    if inf == output:
                        count, resault1 = testsall.tasklist_test(self, filename, search=suffix, count=count)
                        if resault1 == "0":
                            count = logining.success_log(self, count, filename)
                            check = 1
                    else:
                        if inf in output:
                            count, resault1 = testsall.tasklist_test(self, filename, search=suffix, count=count)
                            if resault1 == "0":
                                count = logining.success_log(self, count, filename)
                                check = 1
                if prefix == "-im":
                    inf = "Process with image name: " + suffix + " successfully terminated"
                    output = test_executor.getOutput(self, count)
                    if inf == output:
                        count, resault1 = testsall.tasklist_test(self, filename, search=suffix, count=count)
                        if resault1 == "0":
                            count = logining.success_log(self, count, filename)
                            check = 1
                    else:
                        if inf in output:
                            count, resault1 = testsall.tasklist_test(self, filename, search=suffix, count=count)
                            if resault1 == "0":
                                count = logining.success_log(self, count, filename)
                                check = 1
                if prefix == "-all -img":
                    inf = "All process with image name: " + suffix + " successfully terminated"
                    output = test_executor.getOutput(self, count)
                    if inf == output:
                        count, resault1 = testsall.tasklist_test(self, filename, search=suffix, count=count)
                        if resault1 == "0":
                            count = logining.success_log(self, count, filename)
                            check = 1
                    else:
                        if inf in output:
                            count, resault1 = testsall.tasklist_test(self, filename, search=suffix, count=count)
                            if resault1 == "0":
                                count = logining.success_log(self, count, filename)
                                check = 1
                if check == 0:
                    count = logining.error_log(self, count, filename)
                    settings.result_flag = 0
                    return count
            else:
                count = logining.error_log(self, count, filename)
                settings.result_flag = 0
                return count
        else:
            count = logining.error_log(self, count, filename)
            settings.result_flag = 0
            return count

    def listen_test(self, filename, suffix="", count=0):
        result = "Success"
        settings.result_flag = 1
        resault1 = ""
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "listen " + suffix, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if suffix != "":
                count, resault1 = self.listpipes_test(filename, search=suffix, count=count)
                if suffix in resault1:
                    count = logining.success_log(self, count, filename)
                    settings.result_flag = 0
                    return count
                else:
                    count = logining.error_log(self, count, filename)
                    settings.result_flag = 0
                    return count
            else:
                count = logining.error_log(self, count, filename)
                settings.result_flag = 0
                return count
        else:
            count = logining.error_log(self, count, filename)
            settings.result_flag = 0
            return count

    def unlisten_test(self, filename, suffix="", result="Success", count=0):
        settings.result_flag = 1
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "unlisten " + suffix, count, filename)
        # print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if suffix != "":
                count, resault1 = self.listpipes_test(filename, search=suffix, count=count)
                if resault1 == "0":
                    count = logining.success_log(self, count, filename)
                    settings.result_flag = 0
                    return count
                else:
                    count = logining.error_log(self, count, filename)
                    settings.result_flag = 0
                    return count
            else:
                count = logining.error_log(self, count, filename)
                settings.result_flag = 0
                return count
        else:
            count = logining.error_log(self, count, filename)
            settings.result_flag = 0
            return count

    def useragent_test(self, filename, suffix="",
                       old="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0", result="Success",
                       count=0):
        count = test_executor.searchidcom(self, count)
        settings.result_flag = 1

        if suffix == "-r":
            count, ansver = test_executor.executor_command(self, "useragent " + suffix, count, filename)
        else:
            count, ansver = test_executor.executor_command(self, "useragent '" + suffix + "'", count, filename)
            # print("Obtained result : ", ansver, ". Expected result : ", result)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if suffix != "-r":
                count, flag, resault1 = self.agentinfo_test(filename, target=suffix, prefix="User agent", count=count)
                if flag == "0":
                    logining.success_log(self, (count - 1), filename)
                    settings.result_flag = 0
                    return count
                else:
                    logining.error_log(self, (count - 1), filename)
                    settings.result_flag = 0
                    return count
            else:
                count, flag, resault1 = testsall.agentinfo_test(self, filename, target=old, prefix="User agent",
                                                                count=count)
                if flag == "0":
                    logining.success_log(self, (count - 1), filename)
                    settings.result_flag = 0
                    return count
                else:
                    logining.error_log(self, (count - 1), filename)
                    settings.result_flag = 0
                    return count
        else:
            count = logining.error_log(self, count, filename)
            settings.result_flag = 0
            return count

    def rndrw_test(self, filename, suffix="", prefix="", long="", count=0):
        result = "Success"
        settings.result_flag = 1
        count = test_executor.searchidcom(self, count)
        flag = 1
        if long == "":
            count, ansver = test_executor.executor_command(self, "rndrw " + prefix + suffix, count, filename)
            if ansver.encode('utf-8') == result.encode('utf-8'):
                if prefix == "":
                    count, resault = testsall.ls_test(self, filename, " ", suffix, count=count)
                    if resault == 1:
                        count = logining.success_log(self, count, filename)
                        flag = 0
                        settings.result_flag = 0
                        return count
                else:
                    if ":" in prefix:
                        count, resault = testsall.ls_test(self, filename, prefix, suffix, count=count)
                        if resault == 1:
                            count = logining.success_log(self, count, filename)
                            flag = 0
                            settings.result_flag = 0
                            return count
                    else:
                        testsall.cd_test(self, filename, " ")
                        output = test_executor.getOutput(self, count)
                        way = str(output) + str(prefix)
                        count, resault = testsall.ls_test(self, filename, way, suffix, count=count)
                        if resault == 1:
                            count = logining.success_log(self, count, filename)
                            flag = 0
                            settings.result_flag = 0
                            return count
                if flag == 1:
                    count = logining.error_log(self, count, filename)
                    settings.result_flag = 0
                    return count
            else:
                count = logining.error_log(self, count, filename)
                settings.result_flag = 0
                return count
        else:
            count, ansver = test_executor.executor_command(self, "rndrw " + " " + long + " " + prefix + suffix, count, filename)
            if ansver.encode('utf-8') == result.encode('utf-8'):
                if prefix == "":
                    count, resault = testsall.ls_test(self, filename, suffix=" ", search=suffix, count=count)
                    if suffix in resault:
                        count = logining.success_log(self, count, filename)
                        flag = 0
                        settings.result_flag = 0
                        return count
                else:
                    if ":" in prefix:
                        count, resault = testsall.ls_test(self, filename, suffix=prefix, search=suffix, count=count)
                        if suffix in resault:
                            count = logining.success_log(self, count, filename)
                            flag = 0
                            settings.result_flag = 0
                            return count
                    else:
                        count = testsall.cd_test(self, filename, suffix=" ", result="Success", count=count)
                        output = test_executor.getOutput(self, count)
                        way = str(output) + '\\' + str(prefix)
                        count, resault = testsall.ls_test(self, filename, suffix=way, search=suffix, count=count)
                        if suffix in resault:
                            count = logining.success_log(self, count, filename)
                            flag = 0
                            settings.result_flag = 0
                            return count
                if flag == 1:
                    count = logining.error_log(self, count, filename)
                    settings.result_flag = 0
                    return count

    def mv_test(self, filename, target="", suffix="", prefix="", oldname="", count=0):
        result = "Success"
        settings.result_flag = 1
        count = test_executor.searchidcom(self, count)
        flag = 1
        if oldname == "":
            oldname = target
        count, ansver = test_executor.executor_command(self, "move " + prefix + oldname + " " + suffix + target, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if target != "" and oldname != "" and suffix != "":
                if ":" in suffix:
                    count, resault = testsall.ls_test(self, filename, suffix, target, count=count)
                    if target in resault:
                        count = logining.success_log(self, count, filename)
                        settings.result_flag = 0
                        return count
                else:
                    count = testsall.cd_test(self, filename, suffix=" ", result="Success", count=count)
                    output = test_executor.getOutput(self, count)
                    way = str(output) + "\\" + str(suffix)
                    count, resault = testsall.ls_test(self, filename, way, target, count=count)
                    if resault == 1:
                        count = logining.error_log(self, count, filename)
                        settings.result_flag = 0
                        return count
                    if target in resault:
                        count = logining.success_log(self, count, filename)
                        settings.result_flag = 0
                        return count
        else:
            count = logining.error_log(self, count, filename)
            settings.result_flag = 0
            return count

    def cp_test(self, filename, target="", suffix="", prefix="", oldname="", count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        settings.result_flag = 1
        if oldname == "":
            oldname = target
        count, ansver = test_executor.executor_command(self, "copy " + prefix + oldname + " " + suffix + target, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            if target != "" and oldname != "" and suffix != "":
                if ":" in suffix:
                    count = test_executor.searchidcom(self, count)
                    count, resault = testsall.ls_test(self, filename, suffix, target, result="Success", count=count)
                    if target in resault:
                        count = logining.success_log(self, count, filename)
                        settings.result_flag = 0
                        return count
                else:
                    count = test_executor.searchidcom(self, count)
                    count = testsall.cd_test(self, filename, suffix=" ", result="Success", count=count)
                    output = test_executor.getOutput(self, count)
                    way = str(output) + "\\" + str(suffix)
                    count = test_executor.searchidcom(self, count)
                    count, resault = testsall.ls_test(self, filename, way, target, count=count)
                    if resault == 1:
                        count = logining.error_log(self, count, filename)
                        settings.result_flag = 0
                        return count
                    if target in resault:
                        count = logining.success_log(self, count, filename)
                        settings.result_flag = 0
                        return count
        else:
            count = logining.error_log(self, count, filename)
            settings.result_flag = 0
            return count

    def lddll_modul(self, filename, target="", com="lddll", suffix="", prefix="", number="", result="Success", count=0):
        check = 1
        count = test_executor.searchidcom(self, count)
        if com == "lddll" or com == "lddlln":
            count, ansver = test_executor.executor_command(self, com + " " + prefix + target + " " + suffix, count, filename)
            check = 0
            if ansver.encode('utf-8') == result.encode('utf-8'):
                if target != "":
                    output = test_executor.getOutput(self, count)
                    count = logining.success_log(self, count, filename)
                    return count
                else:
                    count = logining.error_log(self, count, filename)
                    return count
            else:
                count = logining.error_log(self, count, filename)
                return count
        if com == "lddll2":
            count, resault = test_executor.upload(self, number, count, flag=1)
            check = 0
            if resault.encode('utf-8') == result.encode('utf-8'):
                if target != "":
                    output = test_executor.getOutput(self, count)
                    count = logining.success_log(self, count, filename)
                    return count
                else:
                    count = logining.error_log(self, count, filename)
                    return count
            else:
                count = logining.error_log(self, count, filename)
                return count
        if com == "lddllr":
            count, resault = test_executor.upload(self, number, count, flag=2)
            if resault.encode('utf-8') == result.encode('utf-8'):
                if target != "":
                    output = test_executor.getOutput(self, count)
                    count = logining.success_log(self, count, filename)
                    return count
                else:
                    count = logining.error_log(self, count, filename)
                    return count
            else:
                count = logining.error_log(self, count, filename)
                return count
        if check == 1:
            count = logining.error_log(self, count, filename)
            return count

    def fetch_test(self, filename, targetfile="", suffix="", search="", count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        if suffix == "":
            count = logining.error_log(self, count, filename)
            return count
        else:
            if search == "":
                if targetfile == "":
                    count, ansver = test_executor.executor_command(self, "fetch " + suffix, count, filename)
                    if ansver.encode('utf-8') == result.encode('utf-8'):
                        count = logining.success_log(self, count, filename)
                        return count
                    else:
                        count, ansver = test_executor.executor_command(self, "fetch " + suffix, count, filename)
                        search = hashlib(bytes(target, "utf-8")).hexdigest()
                        InTime = WebDriverWait(driver, 10).until(
                            lambda driver: driver.find_element_by_xpath(".//*[@id='logoutForm']/ul/li[2]")).text
                        Date = InTime.split(" ")
                        if ansver.encode('utf-8') == result.encode('utf-8'):
                            if suffix == "":
                                controllsumm = WebDriverWait(driver, 10).until(
                                    lambda driver: driver.find_element_by_xpath(
                                        ".//*[@id='DataTables_Table_0']/tbody/tr[1]/td[8]")).text
                                controlldate = WebDriverWait(driver, 10).until(
                                    lambda driver: driver.find_element_by_xpath(
                                        ".//*[@id='DataTables_Table_0']/tbody/tr[1]/td[6]")).text
                                if search == controllsumm:
                                    if Date in controlldate:
                                        count = logining.success_log(self, count, filename)
                                        return count
                                    else:
                                        count = logining.error_log(self, count, filename)
                                        return count
                                else:
                                    count = logining.error_log(self, count, filename)
                                    return count
                            else:
                                count = logining.error_log(self, count, filename)
                                return count
                        else:
                            count = logining.error_log(self, count, filename)
                            return count
            else:
                count, ansver = test_executor.executor_command(self, "fetch " + suffix, count, filename)
                if ansver.encode('utf-8') == result.encode('utf-8'):
                    pass
                    if search in output:
                        count = logining.success_log(self, count, filename)
                        return count
                    else:
                        count = logining.error_log(self, count, filename)
                        return count

    def debuglog_test(self, filename, suffix="", count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "debuglog" + suffix, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def cat_test(self, filename, suffix="", count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "cat " + suffix, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def exec_test(self, filename, suffix="", result="Success", count=0):
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "exec " + suffix, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def fork_test(self, filename, count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "fork", count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def turnoff_test(self, filename, count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "turnoff", count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def turnwipe_test(self, filename, count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "turnwipe", count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    def rndinterval_test(self, filename, suffix="on", count=0):
        result = "Success"
        count = test_executor.searchidcom(self, count)
        count, ansver = test_executor.executor_command(self, "rndinterval" + suffix, count, filename)
        if ansver.encode('utf-8') == result.encode('utf-8'):
            count = logining.success_log(self, count, filename)
            return count
        else:
            count = logining.error_log(self, count, filename)
            return count

    ###############################################################################################################################################
    ###############################################################################################################################################
    def test_for_debugging(self):  # debug
        test_executor.connect(self, "https://10.100.10.240/Account/Login")
        driver = self.driver
        self.driver.get("https://10.100.10.240/UpdateFile/Upload")
        time.sleep(5)
        number = logining.ini_File(self)
        my_file = open("C:\logs\Log" + str(number) + "_" + str(time.strftime("%Y_%m_%d_%H", time.localtime())) + ".txt",
                       "a+")
        name = my_file.name
        my_file.close()
        go = 0
        a = ["", "", ""]

    ###############################################
    # print(settings.test_string)
    # uploadstring = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='fileupload']"))
    # uploadstring.send_keys("E:\\builds\\Hektor 18.03.05.128.T.exe")
    ###############################################
    ###############################################

    def test_4(self):
        date, num_rec = test_executor.json_parse()
        settings.howmany_test = num_rec
        test_executor.connect(self, settings.work_login, settings.work_name, settings.work_pass)
        driver = self.driver
        self.driver.get(settings.work_address)
        time.sleep(5)
        number = logining.ini_File(self)
        my_file = open(
            "src\logs\Log" + str(number) + "_" + str(time.strftime("%Y_%m_%d_%H", time.localtime())) + ".txt", "a+")
        name = my_file.name
        my_file.close()

        go = 0
        a = ["", "", ""]
        #########################################
        print("OK")
        print("Test START!")
        my_file = open(settings.file_str, 'r')
        for i in range(num_rec):
            if str(date[0]["case_" + str(i)][0]["command"]) == 'cd':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    # print(str(date[0]["case_"+str(i)][0]["command"])+"//"+str(date[0]["case_"+str(i)][0]["parameters"]))
                    go = self.cd_test(name, result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    # print(str(date[0]["case_"+str(i)][0]["command"])+"//"+str(date[0]["case_"+str(i)][0]["parameters"]))
                    go = self.cd_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                      result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'ls':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.ls_test(name, result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.ls_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                      result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'pwd':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.pwd_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.pwd_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'debuglog':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.debuglog_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.debuglog_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'dl':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.dl_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.dl_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'env':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.env_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.env_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'datetime' or str(
                    date[0]["case_" + str(i)][0]["command"]) == 'date' or str(
                    date[0]["case_" + str(i)][0]["command"]) == 'time':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.datetime_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.datetime_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'rndinterval':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.rndinterval_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.rndinterval_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'turnoff':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.turnoff_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.turnoff_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'turnwipe':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.turnwipe_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.turnwipe_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'fork':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.fork_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.fork_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'cat':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.cat_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.cat_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'exec' or str(
                    date[0]["case_" + str(i)][0]["command"]) == 'start':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.exec_test(name, result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.exec_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                        result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'listen':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.listen_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.listen_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'unlisten':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.unlisten_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.unlisten_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'listld':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.listld_test(name, count=go)
                if 'type' in str(date[0]["case_" + str(i)]) and str(date[0]["case_" + str(i)][0]["type"]) != "":
                    go = self.listld_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                          search=str(date[0]["case_" + str(i)][0]["search"]),
                                          adress=str(date[0]["case_" + str(i)][0]["adress"]),
                                          type=str(date[0]["case_" + str(i)][0]["type"]), count=go)
                else:
                    if 'adress' in str(date[0]["case_" + str(i)]) and str(date[0]["case_" + str(i)][0]["adress"]) != "":
                        go = self.listld_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                              search=str(date[0]["case_" + str(i)][0]["search"]),
                                              adress=str(date[0]["case_" + str(i)][0]["adress"]), count=go)
                    else:
                        if 'search' in str(date[0]["case_" + str(i)]) and str(
                                date[0]["case_" + str(i)][0]["search"]) != "":
                            go = self.listld_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                                  search=str(date[0]["case_" + str(i)][0]["search"]), count=go)
                        else:
                            if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                                go = self.listld_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                                      count=go)
                            else:
                                print("Case number:" + str(
                                    i) + " doesn't have 'adress','search','type','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'listexp':
                if 'search' in str(date[0]["case_" + str(i)]) and str(date[0]["case_" + str(i)][0]["search"]) != "":
                    go = self.listexp_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                           search=str(date[0]["case_" + str(i)][0]["search"]), count=go)
                else:
                    if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                        go = self.listexp_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
                    else:
                        print("Case number:" + str(
                            i) + " doesn't have 'search','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'mkdir':
                if 'way' in str(date[0]["case_" + str(i)]) and str(date[0]["case_" + str(i)][0]["way"]) != "":
                    go = self.mkdir_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                         prefix=str(date[0]["case_" + str(i)][0]["way"]),
                                         result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
                else:
                    if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                        go = self.mkdir_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                             result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
                    else:
                        print("Case number:" + str(
                            i) + " doesn't have 'way','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'rm':
                if 'way' in str(date[0]["case_" + str(i)]) and str(date[0]["case_" + str(i)][0]["way"]) != "":
                    go = self.rm_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                      prefix=str(date[0]["case_" + str(i)][0]["way"]), count=go)
                else:
                    if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                        go = self.rm_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'taskkill':
                if 'specifier' in str(date[0]["case_" + str(i)]) and str(
                        date[0]["case_" + str(i)][0]["specifier"]) != "":
                    go = self.taskkill_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                            prefix=str(date[0]["case_" + str(i)][0]["specifier"]), count=go)
                else:
                    if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                        go = self.taskkill_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
                    else:
                        print("Case number:" + str(
                            i) + " doesn't have 'specifier','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'fetch' or str(
                    date[0]["case_" + str(i)][0]["command"]) == 'download':
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.fetch_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'cp' or str(
                    date[0]["case_" + str(i)][0]["command"]) == 'copy':
                if str(date[0]["case_" + str(i)][0]["old_file"]) != "" and str(
                        date[0]["case_" + str(i)][0]["new_file"]) != "" and str(
                        date[0]["case_" + str(i)][0]["way_in"]) != "" and str(
                        date[0]["case_" + str(i)][0]["way_out"]) != "":
                    go = self.cp_test(name, oldname=str(date[0]["case_" + str(i)][0]["old_file"]),
                                      suffix=str(date[0]["case_" + str(i)][0]["way_in"]),
                                      prefix=str(date[0]["case_" + str(i)][0]["way_out"]),
                                      target=str(date[0]["case_" + str(i)][0]["new_file"]), count=go)
                else:
                    if str(date[0]["case_" + str(i)][0]["old_file"]) != "" and str(
                            date[0]["case_" + str(i)][0]["way_in"]) != "" and str(
                            date[0]["case_" + str(i)][0]["way_out"]) != "":
                        go = self.cp_test(name, oldname=str(date[0]["case_" + str(i)][0]["old_file"]),
                                          suffix=str(date[0]["case_" + str(i)][0]["way_in"]),
                                          prefix=str(date[0]["case_" + str(i)][0]["way_out"]), count=go)
                    else:
                        if str(date[0]["case_" + str(i)][0]["old_file"]) != "" and str(
                                date[0]["case_" + str(i)][0]["way_in"]) != "":
                            go = self.cp_test(name, oldname=str(date[0]["case_" + str(i)][0]["old_file"]),
                                              suffix=str(date[0]["case_" + str(i)][0]["way_in"]), count=go)
                        else:
                            print("Case number:" + str(
                                i) + " doesn't have 'old_file','new_file','way_in','way_out','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'mv' or str(
                    date[0]["case_" + str(i)][0]["command"]) == 'move':
                if str(date[0]["case_" + str(i)][0]["old_file"]) != "" and str(
                        date[0]["case_" + str(i)][0]["new_file"]) != "" and str(
                        date[0]["case_" + str(i)][0]["way_in"]) != "" and str(
                        date[0]["case_" + str(i)][0]["way_out"]) != "":
                    go = self.mv_test(name, oldname=str(date[0]["case_" + str(i)][0]["old_file"]),
                                      suffix=str(date[0]["case_" + str(i)][0]["way_in"]),
                                      prefix=str(date[0]["case_" + str(i)][0]["way_out"]),
                                      target=str(date[0]["case_" + str(i)][0]["new_file"]), count=go)
                else:
                    if str(date[0]["case_" + str(i)][0]["old_file"]) != "" and str(
                            date[0]["case_" + str(i)][0]["way_in"]) != "" and str(
                            date[0]["case_" + str(i)][0]["way_out"]) != "":
                        go = self.mv_test(name, oldname=str(date[0]["case_" + str(i)][0]["old_file"]),
                                          suffix=str(date[0]["case_" + str(i)][0]["way_in"]),
                                          prefix=str(date[0]["case_" + str(i)][0]["way_out"]), count=go)
                    else:
                        if str(date[0]["case_" + str(i)][0]["old_file"]) != "" and str(
                                date[0]["case_" + str(i)][0]["way_in"]) != "":
                            go = self.mv_test(name, oldname=str(date[0]["case_" + str(i)][0]["old_file"]),
                                              suffix=str(date[0]["case_" + str(i)][0]["way_in"]), count=go)
                        else:
                            print("Case number:" + str(
                                i) + " doesn't have 'old_file','new_file','way_in','way_out','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'rndrw':
                if 'size' in str(date[0]["case_" + str(i)]) and str(date[0]["case_" + str(i)][0]["size"]) != "":
                    go = self.rndrw_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                         prefix=str(date[0]["case_" + str(i)][0]["way"]),
                                         long=str(date[0]["case_" + str(i)][0]["size"]), count=go)
                else:
                    if 'way' in str(date[0]["case_" + str(i)]) and str(date[0]["case_" + str(i)][0]["way"]) != "":
                        go = self.rndrw_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                             prefix=str(date[0]["case_" + str(i)][0]["way"]) != "", count=go)
                    else:
                        if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                            go = self.rndrw_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
                        else:
                            print("Case number:" + str(
                                i) + " doesn't have 'way','size','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'useragent':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.useragent_test(name, count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.useragent_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            if str(date[0]["case_" + str(i)][0]["command"]) == 'rmdir':
                if 'specific' in str(date[0]["case_" + str(i)]) and str(
                        date[0]["case_" + str(i)][0]["specific"]) == "" and str(
                        date[0]["case_" + str(i)][0]["way"]) != "" and str(
                        date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.rmdir_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                         prefix=str(date[0]["case_" + str(i)][0]["way"]), count=go)
                else:
                    if 'specific' in str(date[0]["case_" + str(i)]) and str(
                            date[0]["case_" + str(i)][0]["specific"]) == "" and str(
                            date[0]["case_" + str(i)][0]["parameters"]) != "":
                        go = self.rmdir_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
                if 'specific' in str(date[0]["case_" + str(i)]) and str(
                        date[0]["case_" + str(i)][0]["specific"]) != "" and str(
                        date[0]["case_" + str(i)][0]["way"]) != "" and str(
                        date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.rmdir_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                         specific=str(date[0]["case_" + str(i)][0]["specific"]),
                                         prefix=str(date[0]["case_" + str(i)][0]["way"]), count=go)
                else:
                    if 'specific' in str(date[0]["case_" + str(i)]) and str(
                            date[0]["case_" + str(i)][0]["specific"]) != "" and str(
                            date[0]["case_" + str(i)][0]["parameters"]) != "":
                        go = self.rmdir_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                             specific=str(date[0]["case_" + str(i)][0]["specific"]), count=go)
                    else:
                        print("Case number:" + str(
                            i) + " doesn't have 'specific','way','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'md5':
                if 'namefile' in str(date[0]["case_" + str(i)]) and str(date[0]["case_" + str(i)][0]["namefile"]) != "":
                    go = self.md5_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                       search=str(date[0]["case_" + str(i)][0]["search"]),
                                       namefile=str(date[0]["case_" + str(i)][0]["namefile"]),
                                       result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
                else:
                    if 'search' in str(date[0]["case_" + str(i)]) and str(date[0]["case_" + str(i)][0]["search"]) != "":
                        go = self.md5_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                           search=str(date[0]["case_" + str(i)][0]["search"]),
                                           result=str(date[0]["case_" + str(i)][0]["result"]), count=go)
                    else:
                        if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                            go = self.md5_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
                        else:
                            print("Case number:" + str(
                                i) + " doesn't have 'namefile','search','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'sysinfo':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.sysinfo_test(name, count=go)
                else:
                    if 'input' in str(date[0]["case_" + str(i)]) and 'value' in str(date[0]["case_" + str(i)]) and str(
                            date[0]["case_" + str(i)][0]["input"]) != "" and str(
                            date[0]["case_" + str(i)][0]["value"]) != "":
                        go = self.sysinfo_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                               target=str(date[0]["case_" + str(i)][0]["value"]),
                                               prefix=str(date[0]["case_" + str(i)][0]["input"]), count=go)
                    else:
                        if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                            go = self.sysinfo_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                                   count=go)
                        else:
                            print("Case number:" + str(
                                i) + " doesn't have 'input','value','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'agentinfo':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.agentinfo_test(name, count=go)
                else:
                    if 'value' in str(date[0]["case_" + str(i)]) and 'input' in str(date[0]["case_" + str(i)]) and str(
                            date[0]["case_" + str(i)][0]["input"]) != "" and str(
                            date[0]["case_" + str(i)][0]["value"]) != "":
                        go = self.agentinfo_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                                 target=str(date[0]["case_" + str(i)][0]["value"]),
                                                 prefix=str(date[0]["case_" + str(i)][0]["input"]), count=go)
                    else:
                        if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                            go = self.agentinfo_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                                     count=go)
                        else:
                            print("Case number:" + str(
                                i) + " doesn't have 'value','input','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'tasklist':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.tasklist_test(name, count=go)
                if 'search' in str(date[0]["case_" + str(i)]) and str(
                        date[0]["case_" + str(i)][0]["parameters"]) != "" and str(
                        date[0]["case_" + str(i)][0]["search"]) == "":
                    go = self.tasklist_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
                if 'search' in str(date[0]["case_" + str(i)]) and str(
                        date[0]["case_" + str(i)][0]["search"]) != "" and str(
                        date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.tasklist_test(name, suffix=str(date[0]["case_" + str(i)][0]["parameters"]),
                                            search=str(date[0]["case_" + str(i)][0]["search"]), count=go)
                else:
                    print("Case number:" + str(
                        i) + " doesn't have 'search','parameters' fields, add them to case according to the instruction")
            if str(date[0]["case_" + str(i)][0]["command"]) == 'lddll' or str(
                    date[0]["case_" + str(i)][0]["command"]) == 'lddlln':
                if str(date[0]["case_" + str(i)][0]["parameters"]) == "":
                    go = self.lddll_modul(name, com=str(date[0]["case_" + str(i)][0]["command"]), count=go)
                if str(date[0]["case_" + str(i)][0]["parameters"]) != "":
                    go = self.lddll_modul(name, com=str(date[0]["case_" + str(i)][0]["command"]),
                                          target=str(date[0]["case_" + str(i)][0]["parameters"]), count=go)
            settings.howcomplete_test = i
        if settings.close_browser == True:
            driver.close()
