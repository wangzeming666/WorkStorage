# newspam.py
from uiautomator import Device
import time
import os
import requests
import re
import random
import time
import sys
from pymongo import MongoClient
from uiautomator import JsonRPCError
from createName import *
import subprocess


deviceID = '0c9625a80c592409'
d = Device(deviceID)
conn = MongoClient('mongodb://192.168.1.66:27017/')
db = conn.proemail
proton = db.newaccount

try:
    os.popen('adb -s {} shell am start -n biz.bokhorst.xprivacy/biz.bokhorst.xprivacy.ActivityMain'.format(deviceID))
    time.sleep(1)
    status, string = subprocess.getstatusoutput("adb -s {} uninstall ch.protonmail.android".format(deviceID))
    time.sleep(2)
    status, string = subprocess.getstatusoutput("adb -s {} install /home/administator/protonmail.apk".format(deviceID))
    time.sleep(8)
    os.popen('adb -s {} shell settings put global airplane_mode_on 1'.format(deviceID))
    time.sleep(1)
    os.popen('adb -s {} shell am broadcast -a android.intent.action.AIRPLANE_MODE'.format(deviceID))
    time.sleep(10)
    os.popen('adb -s {} shell settings put global airplane_mode_on 0'.format(deviceID))
    time.sleep(1)
    os.popen('adb -s {} shell am broadcast -a android.intent.action.AIRPLANE_MODE'.format(deviceID))
    time.sleep(5)
    # d(description='More options').click()
    os.system('adb -s {} shell am start -n ch.protonmail.android/ch.protonmail.android.activities.SplashActivity'.format(deviceID))
    time.sleep(6)
    print(1)
    d(text="Create Account").click()
    time.sleep(10)
    d(resourceId="ch.protonmail.android:id/expand_free").click()
    time.sleep(2)
    d(text="Select").click()
    time.sleep(1)
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    emailpart = ''
    print(2)
    for i in range(8):
        emailpart += random.choice(words)
    for i in range(random.randint(1,5)):
        emailpart += str(random.randint(0, 10))
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password = ''
    words += numbers
    for i in range(12):
        password += random.choice(words)
    emailaccount = emailpart+"@protonmail.com"
    d.click(100,800)
    os.popen('adb -s {} shell input text "{}"'.format(deviceID, emailpart))
    time.sleep(2)
    d.press.back()
    # time.sleep(5)
    # d.press.back()
    time.sleep(random.randint(10, 15))
    d(resourceId="ch.protonmail.android:id/sign_up").click()
    time.sleep(1)
    #d(text="Password").click()
    d(resourceId="ch.protonmail.android:id/password").set_text(password)     
    d(resourceId="ch.protonmail.android:id/confirm_password").set_text(password)
    time.sleep(1)
    d.press.back()
    time.sleep(random.randint(10, 15))
    d(resourceId="ch.protonmail.android:id/generate_keypair").click()
    time.sleep(1)
    d(resourceId="ch.protonmail.android:id/cont").click()
    time.sleep(5)
    d(resourceId="ch.protonmail.android:id/phone_verification").click()
    time.sleep(2)
    d.click(555, 787)
    time.sleep(2)
    for i in range(4):
        num = random.random() * 100
        d.swipe(400+num, 1500-num, 600+num, 400-num)
    time.sleep(1)
    d(text="China").click()
    request_token = requests.get('http://api.ema666.com/Api/userLogin?uName=wangzeming666&pWord=123456789&Developer=Cnp%2bioCFjIENLUVatRXU6g%3d%3d',timeout=60)
    token = re.match(r'([\w\W]+?)&', request_token.text).group(1)
    print(token)
    number = requests.get('http://api.ema666.com/Api/userGetPhone?ItemId=49740&token={}&PhoneType=0'.format(token),timeout=60)
    phonenum = re.match(r'([\d]+);', number.text).group(1)
    print(phonenum)
    d(resourceId="ch.protonmail.android:id/phone_number").set_text(phonenum)
    time.sleep(1)
    d.press.back()
    time.sleep(random.randint(10, 15))
    d(text="Send Verification Code").click()
    try:
        code = ''
        time.sleep(5)
        codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=49740&phone={}'.format(token,phonenum), timeout=60).text
        print(codestr)
        code = re.search(r'([\d]{6}|[\d]{5}|[\d]{4})', codestr).group(1)
    except AttributeError:
        count_time = time.time()
        while (time.time() - count_time) < 120:
            time.sleep(10)
            try:
                if (time.time() - count_time) > 60:
                    d(text='Resend').click()
                codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=49740&phone={}'.format(token,phonenum), timeout=60).text
                print(codestr)
                if codestr == 'False:Session 过期':
                    raise RequestException
                elif codestr == 'False:此号码已经被释放':
                    raise RequestException
                code = re.search(r'([\d]{7}|[\d]{6}|[\d]{5}|[\d]{4})', codestr).group(1)
                break
            except AttributeError:
                continue
    if code == '':
        print('验证码平台出错')
        add_into_blackList = requests.get('http://api.ema666.com/Api/userAddBlack?token={}&phoneList=itemId-58216,{};'.format(token,phonenum))
        print(add_into_blackList.text)
        add_into_blackList = requests.get('http://api.ema666.com/Api/userAddBlack?token={}&phoneList=58216-{};'.format(token,phonenum))
        print(add_into_blackList.text)
        raise Exception('unrecive phone code.')
    d(resourceId="ch.protonmail.android:id/verification_code").set_text(code)
    time.sleep(1)
    d.press.back()
    time.sleep(1)
    d(text="Continue").click()
    time.sleep(20)
    if d(text="Display Name").exists:
        d(text="Display Name").click()
    else:
        time.sleep(10)
        if d(text="Display Name").exists:
            d(text="Display Name").click()
        else:
            time.sleep(5)
            d(text="Display Name").click()
    proton.insert({"userName":emailaccount, "passwords":password, "used":0})
    time.sleep(random.random()*1000)
    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)

except (JsonRPCError,Exception,BaseException, requests.exceptions.RequestException, IndexError) as e:
    print(e)
    # with open('error_log', 'r') as f:
    #     old = f.read()

    # with open('error_log', 'w') as f:
    #     f.write(old)
    #     f.write(str(e)+'\n')
 
    time.sleep(300)
    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)


