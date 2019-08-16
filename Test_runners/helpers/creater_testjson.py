import json
import random
import os

def choose_mode(lot=0):
    mode = input()
    if lot == 0:
        if mode == "auto" or mode == "hand":
            return 1, mode
        else:
            print("You have entered a non-existent value, please try again!")
            return 0, 0
    else:
        if is_digit(mode) == True:
            return 1,mode
        else:
            print("You have entered a non-existent value, please try again!")
            return 0, 0

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def auto_mode(maxi):
    str1 = {"command": "ls","parameters": "","result": "Success","case_id": 1}
    str2 = {"command": "pwd","parameters": "","case_id": 1}
    str3 = {"command": "cd","result":"Success","parameters": "","case_id": 1}
    date = [{"case_0":[]}]
    count = 0
    while count < maxi:
        point = random.randint(1,3)
        if point == 1:
            date[0]["case_"+str(count)] = []
            target = date[0]["case_"+str(count)]
            target.append(str1)
        if point ==2:
            date[0]["case_" + str(count)] = []
            target = date[0]["case_" + str(count)]
            target.append(str2)
        if point ==3:
            date[0]["case_" + str(count)] = []
            target = date[0]["case_" + str(count)]
            target.append(str3)
        count = count+1
    return count,date

def truncate_utf8_chars(filename, count, ignore_newlines=True):
    """
    Truncates last `count` characters of a text file encoded in UTF-8.
    :param filename: The path to the text file to read
    :param count: Number of UTF-8 characters to remove from the end of the file
    :param ignore_newlines: Set to true, if the newline character at the end of the file should be ignored
    """
    with open(filename, 'rb+') as f:
        last_char = None

        size = os.fstat(f.fileno()).st_size

        offset = 1
        chars = 0
        while offset <= size:
            f.seek(-offset, os.SEEK_END)
            b = ord(f.read(1))

            if ignore_newlines:
                if b == 0x0D or b == 0x0A:
                    offset += 1
                    continue

            if b & 0b10000000 == 0 or b & 0b11000000 == 0b11000000:
                # This is the first byte of a UTF8 character
                chars += 1
                if chars == count:
                    # When `count` number of characters have been found, move current position back
                    # with one byte (to include the byte just checked) and truncate the file
                    f.seek(-1, os.SEEK_CUR)
                    f.truncate()
                    return
            offset += 1


flag = 0
print('Hello, please choose the input mode "auto" or "hand".')

while flag != 1:
    flag, mode = choose_mode()
flag = 0

if mode == "auto":
    print("Please choose the input quantity command to generate")
    while flag != 1:
        flag, maxi = choose_mode(lot=1)
    count, data = auto_mode(float(maxi))
    print("Total",count)

print(data)
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, sort_keys=True, indent=4,
              ensure_ascii=False)

#truncate_utf8_chars('data.json', 1)



