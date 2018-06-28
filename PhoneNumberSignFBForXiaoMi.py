# facebook_sign_up_with_yandexMail.py
import os
import re
import sys
import json
import time
import random
import requests
import subprocess
from uiautomator import Device
from pymongo import MongoClient
from uiautomator import JsonRPCError

class MyError(Exception):
    pass

conn = MongoClient('mongodb://192.168.1.66:27017/')
d = Device('d78a2778')

try:
    # get facked name. 
    text = requests.get('https://www.fakenamegenerator.com/gen-male-us-us.php', timeout=30, headers={"User-Agent":"User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}).text
    name = re.search('''<div class="address">
                                        <h3>([\w\W]+?)</h3>''', text).groups()[0]
    nameGroup = re.match('([\w]+) ([\w\W]+)', name).groups()
    firstname = nameGroup[0]                                                                                                                      
    lastname = re.sub('([\w]+)\. ([\w]+)', r'\2', nameGroup[1])
    # make password. 
    password = ''
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(12):
        password += random.choice(words)
    # get phone number.  
    request_token = requests.get('http://api.ema666.com/Api/userLogin?uName=wangzeming666&pWord=123456789&Developer=Cnp%2bioCFjIENLUVatRXU6g%3d%3d',timeout=10)
    token = re.match(r'([\w\W]+?)&', request_token.text).group(1)
    print(token)
    number = requests.get('http://api.ema666.com/Api/userGetPhone?ItemId=165&token={}&PhoneType=0'.format(token),timeout=10)
    phonenum = re.match(r'([\d]+);', number.text).group(1)
    print(phonenum)
    phonenum86 = '+86'+phonenum
    # get device informations.  
    d.press('home')
    d(text="XPrivacy").click()
    time.sleep(3)
    d.click(650, 100)
    time.sleep(1)
    d.swipe(700, 1000, 700, 600)
    d(text="Settings").click()
    time.sleep(1)
    d(text="Randomize now").click()
    time.sleep(1)
    d.swipe(350, 1000, 350, 100)
    d.dump('aaa')
    d.swipe(350, 1000, 350, 100)
    d.dump('bbb')
    d(text="OK").click()
    list = [17, 20, 23, 26, 31, 36, 39, 42, 45, 48, 55, 66, 69]
    with open('aaa', 'r') as f:
        string = f.read()
    with open('bbb', 'r') as f:
        string = string + f.read()
    argudict = {}
    for i in list:
        text = re.search('index="{}"[\w\W]+?text="([\w\W]+?)"'.format(i+1), string).groups()[0]
        value = re.search('index="{}"[\w\W]+?text="([\w\W]+?)"'.format(i+2), string).groups()[0]
        argudict[text] = value
    # 卸载fb
    status, string = subprocess.getstatusoutput('adb -s d78a2778 uninstall com.facebook.katana')
    # 安装fb
    status, string = subprocess.getstatusoutput('adb -s d78a2778 install /home/administator/facebook-163-0-0-43-91.apk')
    # 切换ip代理
    d.press('home')
    db = conn.ssArgu
    ss = [i for i in db.ts.find().sort('times', 1)][0]
    # 设置信号量
    ss['times'] = ss['times'] + 1
    ip = ss['ip']
    db.ts.update({'ip':ss['ip']}, ss)
    print(ip)
    # change ip.  
    d(textContains='shadow').click()
    time.sleep(1)
    d(resourceId="com.github.shadowsocks:id/fab").click()
    time.sleep(2)
    d(resourceId="com.github.shadowsocks:id/edit").click()
    time.sleep(1)
    d(text="Server").click()
    time.sleep(3)
    # d.click(660, 1100)
    # time.sleep(2)
    # d(resourceId="android:id/edit").set_text(ip)
    os.popen('adb -s d78a2778 shell input text "{}"'.format(ip))
    time.sleep(1)
    d(text="OK").click()
    time.sleep(1)
    d(resourceId="com.github.shadowsocks:id/action_apply").click()
    d(resourceId="com.github.shadowsocks:id/fab").click()
    time.sleep(5)
    d.press('home')
    
except (requests.exceptions.RequestException, JsonRPCError, AttributeError, NameError, Exception) as e:
    print(e)
    print(1)
    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)
    

try:
    # 注册fb
    d(text="Facebook").click()
    time.sleep(15)
    if d(text="CONTINUE").exists:
        d(text="CONTINUE").click()
    d(text="Create New Facebook Account").click()
    if d(textContains="Deny").exists:
        d(textContains="Deny").click()
    time.sleep(1)
    d(text="Next").click()
    time.sleep(1)
    d(text="Last Name").set_text(lastname)
    time.sleep(1)
    d(text="First Name").set_text(firstname)
    time.sleep(1)
    d(text='Next').click()
    time.sleep(1)
    num = [str(i) for i in range(10)]
    year = '19' + random.choice(['8', '9']) + random.choice(num)
    month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    day = [str(i) for i in range(1, 31)]
    month = random.choice(month)
    day = random.choice(day)
    time.sleep(1)
    d(className="android.widget.EditText")[2].set_text(year)
    time.sleep(1)
    d(className="android.widget.EditText")[0].set_text(month)
    time.sleep(1)
    d(className="android.widget.EditText")[1].set_text(day)
    time.sleep(1)
    d(text="Next").click()
    time.sleep(1)
    d(text="Female").click()
    time.sleep(1)
    d(text="Next").click()
    time.sleep(1)
    # input the phone number.  
    d(text="Mobile Number")[1].set_text(phonenum86)
    time.sleep(1)
    d(text="Next").click()
    time.sleep(1)
    d(text="Password")[1].set_text(password)
    time.sleep(1)
    d(text="Next").click()
    time.sleep(1)
    d(text="Sign up without uploading my contacts").click()
    time.sleep(6)
    if d(textContains="Deny").exists:
        d(textContains="Deny").click()
    time.sleep(1)
    if d(textContains="Deny").exists:
        d(textContains="Deny").click()
    time.sleep(1)
    if d(textContains="Deny").exists:
        d(textContains="Deny").click()
        time.sleep(1)
    time.sleep(20)
    if d(text="Not Now").exists:
        d(text="Not Now").click()
    signal = ''
    if d(text="Skip").exists:
        signal = 1
        d(text="Skip").click()
        time.sleep(3)
    if d(text="Skip").exists:
        d(text="Skip").click()
        time.sleep(3)
    if d(text="Skip").exists:
        d(text="Skip").click()
        time.sleep(3)
    if d(text="Skip").exists:
        d(text="Skip").click()
        time.sleep(3)
    print("SIGNAL:", signal)
    if d(text="Try Again").exists:
    	raise MyError("Something went wrong, may be cannot sent data to Facebook.")
    # get the confirmation code.  
    try:
        code = ''
        time.sleep(5)
        codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=165&phone={}'.format(token,phonenum), timeout=10).text
        print(codestr)
        code = re.search(r'([\d]{6}|[\d]{5}|[\d]{4})', codestr).group(1)
    except AttributeError:
        count_time = time.time()
        while (time.time() - count_time) < 60:
            time.sleep(5)
            try:
                codestr = requests.get('http://api.ema666.com/Api/userSingleGetMessage?token={}&itemId=165&phone={}'.format(token,phonenum), timeout=10).text
                print(codestr)
                if codestr == 'False:Session 过期':
                    raise requests.exceptions.RequestException
                code = re.search(r'([\d]{6}|[\d]{5}|[\d]{4})', codestr).group(1)
                break
            except AttributeError:
                continue
    if code == '':
        print('未收到验证码')
        raise requests.exceptions.RequestException
      
    # input the confirmation code.
    d(text="Confirmation code").set_text(code)
    time.sleep(1)
    d(text="Confirm").click()
    time.sleep(8)

    # if error did not be fond, successful.
    if d(text="Not Now").exists:
        d(text="Not Now").click()
    if signal == 1:
        pass
    elif d(text="Skip").exists:
    	pass
    elif d(text="OK").exists:
    	pass
    elif d(text="Not Now").exists:
    	pass
    else:
        raise MyError("Something went wrong, this error has not been defined.")

    # put data in dict.  
    print(year,month,day)
    argudict["phonenum86"] = phonenum86
    argudict["passwd"] = password
    argudict["birthday"] = "{}".format(year+'-'+month+'-'+day)
    argudict["gender"] = "Female"
    argudict["page"] = "Null"
    argudict["first_name"] = firstname
    argudict["last_name"] = lastname
    argudict['device_argu'] = 'True'
    # print(argudict)

    # insert to database.  
    db = conn.fbaccount
    db.phoneAccount.insert(argudict)
    print('Finished')
    # This line of code cannot be annotation.  
    time.sleep(random.random()*1000)
    
except (requests.exceptions.RequestException, JsonRPCError, AttributeError, MyError, IndexError) as e:
    print(e)
    print(2)
    print('Add the phone-number into the black list.')
    add_into_blackList = requests.get('http://api.ema666.com/Api/userAddBlack?token={}&phoneList=itemId-165,{};'.format(token,phonenum))
    print(add_into_blackList.text)
    add_into_blackList = requests.get('http://api.ema666.com/Api/userAddBlack?token={}&phoneList=165-{};'.format(token,phonenum))
    print(add_into_blackList.text)
    python3 = sys.executable
    os.execl(python3, python3, * sys.argv)

# 重启程序
time.sleep(20)
python3 = sys.executable
os.execl(python3, python3, * sys.argv)
