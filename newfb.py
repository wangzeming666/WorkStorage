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
deviceID = '0c9625a80c592409'
d = Device(deviceID)

try:
	# get facked name. 
	text = requests.get('https://www.fakenamegenerator.com/gen-male-us-us.php', timeout=30, headers={"User-Agent":"User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}).text
	name = re.search('''<div class="address">[\w\W]+?<h3>([\w\W]+?)</h3>''', text).groups()[0]
	FullName = re.match('([\w]+) ([\w\W]+)', name).group()
	# lastname = re.sub('([\w]+)\. ([\w]+)', r'\2', nameGroup[1])
	password = ''
	words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	for i in range(12):
		password += random.choice(words)
	# get phone number.  
	request_token = requests.get('http://api.ema666.com/Api/userLogin?uName=wangzeming666&pWord=123456789&Developer=Cnp%2bioCFjIENLUVatRXU6g%3d%3d', timeout=10)
	token = re.match(r'([\w\W]+?)&', request_token.text).group(1)
	print(token)
	number = requests.get('http://api.ema666.com/Api/userGetPhone?ItemId=165&token={}&PhoneType=0'.format(token), timeout=10)
	phonenum = re.match(r'([\d]+);', number.text).group(1)
	print(phonenum)
	phonenum86 = '+86'+phonenum
	os.system('adb -s {} shell am start -n biz.bokhorst.xprivacy/biz.bokhorst.xprivacy.ActivityMain'.format(deviceID))
	time.sleep(3)
	d.dump('aaa')
	d(description='More options').click()
	time.sleep(1)
	d(text="Settings").click()
	time.sleep(1)
	d.swipe(500, 1700, 500, -500)
	d(text="Randomize now").click()
	time.sleep(1)
	d.dump('aaa')
	d.swipe(500, 1700, 500, 300)
	d.dump('bbb')
	d.swipe(500, 1700, 500, 700)
	d.dump('ccc')
	d(description="OK").click()
	list = [21, 24, 27, 30, 35, 40, 43, 46, 49, 52, 59, 70, 73]
	with open('aaa', 'r') as f:
		string = f.read()
	with open('bbb', 'r') as f:
		string = string + f.read()
	with open('ccc', 'r') as f:
		string = string + f.read()
	argudict = {}
	for i in list:
		text = re.search('index="{}"[\w\W]+?text="([\w\W]+?)"'.format(i+1), string).groups()[0]
		value = re.search('index="{}"[\w\W]+?text="([\w\W]+?)"'.format(i+2), string).groups()[0]
		argudict[text] = value
	print(argudict)
	# 卸载fb
	subprocess.getstatusoutput('adb -s {} uninstall com.facebook.katana'.format(deviceID))
	time.sleep(1)
	# 安装fb
	subprocess.getstatusoutput('adb -s {} install /home/administator/facebook-163-0-0-43-91.apk'.format(deviceID))
	os.system('adb -s {} shell am start -n com.github.shadowsocks/.MainActivity'.format(deviceID))
	time.sleep(2)
	d(resourceId='com.github.shadowsocks:id/fab').click()
	time.sleep(2)
	d(resourceId="com.github.shadowsocks:id/edit").click()
	time.sleep(1)
	if d(text="Server").exists:
		d(text="Server").click()
	else:
		d(resourceId='com.github.shadowsocks:id/fab').click()
		time.sleep(2)
		d(resourceId="com.github.shadowsocks:id/edit").click()
		time.sleep(1)
		d(text="Server").click()
	time.sleep(2)
	for i in range(20):
		os.system('adb -s {} shell input keyevent 67'.format(deviceID))
		time.sleep(0.2)
	# 切换ip代理
	db = conn.ssArgu
	ss = [i for i in db.ts.find().sort('times', 1)][0]
	# 设置信号量
	ss['times'] = ss['times'] + 1
	ip = ss['ip']
	db.ts.update({'ip':ss['ip']}, ss)
	print(ip)
	ip = 'jp.b.cloudss.win'
	d(resourceId="android:id/edit").set_text(ip)
	d(text="OK").click()
	time.sleep(1)
	d(resourceId="com.github.shadowsocks:id/action_apply").click()
	time.sleep(1)
	d(resourceId="com.github.shadowsocks:id/fab").click()
	time.sleep(5)

except (requests.exceptions.RequestException, JsonRPCError, AttributeError, NameError, Exception) as e:
	print(e)
	print(1)	
	python3 = sys.executable
	os.execl(python3, python3, * sys.argv)


try:
	os.system('adb -s {} shell am start -n com.facebook.katana/.LoginActivity'.format(deviceID))
	time.sleep(10)
	d(text="Create New Facebook Account").click()
	time.sleep(1)
	d(text="Next").click()
	time.sleep(1)
	if d(textContains="Deny").exists:
		d(textContains="Deny").click()
	time.sleep(1)
	if d(textContains="Deny").exists:
		d(textContains="Deny").click()
	time.sleep(1)
	if d(text="Full Name").exists:
		d(text="Full Name").click()
		time.sleep(1)
		nameSplit = FullName.split(' ')
		length = len(nameSplit)
		if length > 1:
			times = 0
			for i in nameSplit:
				times += 1
				print('starting input...')
				os.system('adb -s {} shell input text "{}"'.format(deviceID, i))
				time.sleep(1)
				if times < length:
					os.system('adb -s {} shell input keyevent 62'.format(deviceID))
					time.sleep(1)
	elif d(text='Last Name').exists:
		d(text='Last Name').click()
		nameSplit = FullName.split(' ')
		length = len(nameSplit[1:])
		os.system('adb -s {} shell input text "{}"'.format(deviceID, nameSplit[0]))
		d(text='First Name').click()
		if length > 1:
			times = 0
			for i in nameSplit[1:]:
				times += 1
				print('starting input...')
				os.system('adb -s {} shell input text "{}"'.format(deviceID, i))
				time.sleep(1)
				if times < length:
					os.system('adb -s {} shell input keyevent 62'.format(deviceID))
		elif length == 1:
			os.system('adb -s {} shell input text "{}"'.format(deviceID, nameSplit[1]))
	time.sleep(8)
	d(text='Next').click()
	time.sleep(1)
	num = [str(i) for i in range(10)]
	year = '19' + random.choice(['8', '9']) + random.choice(num)
	month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
	day = str(random.randint(1,31))
	if int(day) < 10:
		day = '0'+day
	month = random.choice(month)
	day = random.choice(day)
	time.sleep(1)
	d.dump('aaa')
	time.sleep(3)
	with open('aaa', 'r') as f:
		string = f.read()
	MON, DAY, YEA = re.findall(r'<node index="1" text="([\w]+)" resource-id="android:id/numberpicker_input"', string)
	
	time.sleep(1)
	d(text="{}".format(DAY)).set_text(random.choice(day))
	time.sleep(3)
	d(text="{}".format(YEA)).set_text(random.choice(year))
	time.sleep(10)
	d(text="Next").click()
	time.sleep(1)
	d(text="Female").click()
	time.sleep(1)
	d(text="Next").click()
	time.sleep(1)
	d(text="Mobile Number")[1].click()
	time.sleep(1)
	os.system('adb -s {} shell input text "{}"'.format(deviceID, phonenum86))
	time.sleep(10)
	d(text="Next").click()
	time.sleep(1)
	d(text="Password")[1].click()
	time.sleep(1)
	os.system('adb -s {} shell input text "{}"'.format(deviceID, password))
	time.sleep(10)
	d(text="Next").click()
	time.sleep(1)
	d(text="Sign up without uploading my contacts").click()
	time.sleep(2)
	d(text="Deny").click()
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
		time.sleep(1)
	if d(text="Skip").exists:
		d(text="Skip").click()
		time.sleep(1)
	if d(text="Skip").exists:
		d(text="Skip").click()
		time.sleep(1)
	print("SIGNAL:", signal)
	if d(text="Try Again").exists:
		raise MyError("Something went wrong, may be cannot sent data to Facebook.")
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
	argudict["name"] = FullName
	argudict['device_argu'] = 'True'
	# print(argudict)

	# insert to database.  
	db = conn.fbaccount
	db.newPhoneAccount.insert(argudict)
	print('Finished')
	# This line of code cannot be annotation.  
	time.sleep(1)
	
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
