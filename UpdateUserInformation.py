from uiautomator import JsonRPCError
import aircv as ac
import os
import random
import re
import sys
import time


class UnKnowError(Exception):
	pass


class typer():
	'''
	填写facebook个人详细信息功能。
	需要传入两个参数， 第一个是设备uiautomator的Device实例对象， 第二个是设备的IP。
	基本上函数的作用都能在函数名上看出来。
	'''
	def __init__(self, Device, deviceIP):
		# 几百种大学专业名json文件路径
		self.ConcentrationRoad = './Concentration.json'
		# 公司图片路径
		self.addWorkSrcRoad = './addWork/Position/'
		self.srcAddCollege = './homePage/addCollege.png'
		# srcAdd开头的除了下面这个都是第一个选择界面的五个填写部分的图片路径，如添加大学，公司。下面这个是大学的专业填写框用来识别的demo。
		self.srcAddConcetration = './addCollege/AddConcetration.png'
		self.srcAddCurrentCity = './homePage/addCurrentCity.png'
		self.srcAddHighSchool = './homePage/addHighSchool.png'
		self.srcAddHomeTown = './homePage/addHomeTown.png'
		self.srcAddRelationship = './homePage/addRelationship.png'
		self.srcAddWork = './addWork/addWork.png'
		# 这个图片没用到，但还是放在这里备用了。
		self.srcCannotFindASecureConnection = 'CannotFindASecureConnection.png '
		# 图片的变量名基本都和要填写或点击的框里文字相同，不多解释了。
		self.srcCityTown = './addWork/CityTown.png'
		self.srcDay = './addHighSchool/Day.png'
		self.srcDescription = './addWork/Description.png'
		self.srcEditCollegeUI = './addCollege/EditCollege.png'
		self.srcEditHighSchoolUI = './addHighSchool/EditHighSchool.png'
		self.srcEditRelationship = './addRelationship/EditRelationship.png'
		self.srcEditWorkUI = './addWork/EditWork.png'
		self.srcEnterYourCollege = './addCollege/EnterYourCollege.png'
		self.srcEnterYourCurrentCity = './addCurrentCity/EnterYourCurrentCity.png'
		self.srcEnterYourHighSchool = './addHighSchool/EnterYourHighSchool.png'
		self.srcEnterYourHomeTown = './addCurrentCity/EnterYourHomeTown.png'
		self.srcFirstInSelectUI = 'FirsInAllSelectionUI.png'
		self.srcFrom = './addWork/From.png'
		self.srcHongKong = './addWork/HongKong.png'
		self.srcItsNotAPhysicalPlace = './add/addWork/ItsNotAPhysicalPlace.png'
		self.srcMonth = './addHighSchool/Month.png'
		self.srcPosition = './addWork/Posiotion.png'
		self.srcSave = './homePage/Save.png'
		self.srcWhatIsYourRelationshipStatus = './addRelationship/WhatIsYoutRelationshipStatus.png'
		self.srcWhereDidYouWork = './addWork/whereDidYouWork.png'
		self.srcYear = './addHighSchool/Year.png'
		self.srcGraduate = './homePage/Graduate.png'
		self.srcEditCurrentCityUI = './addCurrentCity/srcEditCurrentCity.png'
		self.swipeTimes += 1
		self.swipeTimes = 0
		self.CoporationList[
		{'name': 'ChinaResources', 'position': 'Sales'}
		{'name': 'ChinaResourcesVanguard', 'position': 'Sales'},
		{'name': 'GreatFoodHall', 'position': 'CustomerServiceAssistant'}, 
		{'name': 'JUSCO', 'position': 'AdviserSales'},
		{'name': 'LaneCrawford', 'position': 'LaneCrawford'}, 
		{'name': 'SeibuDepartmentStores', 'position': 'BeautyConsultant'}, 
		{'name': 'SincereDepartmentStores', 'position': 'Stoker'}, 
		{'name': 'SogoHongKong', 'position': 'Sales'},
		{'name': 'Wellcome', , 'position': 'ShopAssistant'},
		{'name': 'WingOn', , 'position': 'SalesAssociate'},
		{'name': '裕華國貨', 'position': 'Sales'},
		{'name': 'ParknShop', 'position': 'CustomerServiceAssistant'},
		]
		self.HighSchoolList[
		{'name': 'CityUniversityOfHongKong'},
		{'name': 'TheChineseUniversityOfHongKong'},
		{'name': 'TheEducationUniversityOfHongKong'},
		{'name': 'TheHongKongPolytechnicUniversity'},
		{'name': 'TheHongKongUniversityOfScienceAndTechnology'},
		{'name': 'TheUniversityOfHongKong'},
		{'name': 'UniversityOfSunderlandInHongKong'},
		{'name': 'HongKongBaptisUniversity'},
		]
		self.CollegeList[
		{'name': 'Harrow International School'},
		{'name': 'Hong Kong Academy'},
		{'name': 'HongKong Japanese School'},
		{'name': 'Islamic Kasim Tuet Memorial College'},
		{'name': 'Kellett School'},
		{'name': 'MaryKnoll Convent'},
		{'name': 'Munsang College'},
		{'name': 'Scared Heart Canossian College'},
		{'name': 'South Island School'},
		{'name': 'Yew Chung Community College'},
		{'name': 'Ying Wa College'},
		{'name': 'Chinese International School'},
		{'name': 'Delia Memorial School'},
		{'name': 'ESF Discovery College'},
		{'name': 'German Swiss International School'},
		]
		self.workDate = {
			'Day': random.choice([str(i) for i in range(1,31)]),
			'Month': random.choice([
				'January', 'February', 'March', 'April', 
				]),
			'Year':2018, 
			}


	def addCollege(self):
		try:
			x, y = self.findEditBlock(self.srcAddCollege)
			self.checkCurrentFullOfUI(self.srcEditCollegeUI)
			x, y = self.findElement(self.srcEnterYourCollege)
			self.raiseIfError(x, y)
			data = random.choice(self.CollegeList)
			self.clickAndInput(x, y, data['name'])
			time.sleep(5)
			x, y = self.findElement('./addCollege/'+data['name']+'/'+data['name']+'png')
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
			self.selectDate(True)
			x, y = self.findElement(self.Graduate)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
			x, y = self.findElement(self.AddConcetration)
			self.raiseIfError()
			with open(self.ConcentrationRoad, 'r') as f:
				string = f.read()
			concentrationDict = json.loads(string)
			concentration = random.choice(concentrationDict[Concentration])
			self.d.swipe(250, 800, 250, 200)
			time.sleep(3)
			self.clickAndInput(x, y, concentration)
			x, y = self.findElement(self.srcSave)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
		except UnKnowError:
			self.RestartAppAndWalkInEditUI()
			self.addCollege()
			return
		

	def addCurrentCity(self):
		try:
			x, y = self.findEditBlock(self.srcAddCurrentCity)
			self.checkCurrentFullOfUI(self.srcEditCurrentCityUI)
			x, y = self.findElement(self.srcEnterYourCurrentCity)
			self.raiseIfError(x, y)
			self.clickAndInput(x, y, 'HongKong')
			time.sleep(5)
			x, y = self.findElement(srcHongKong)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
			x, y = self.findElement(self.srcAddHomeTown)
			self.raiseIfError()
			self.clickAndInput(x, y, 'HongKong')
			x, y = self.findElement(self.srcHongKong)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
			x, y = self.findElement(self.srcSave)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
		except UnKnowError:
			self.RestartAppAndWalkInEditUI()
			self.addCurrentCity()
			return


	def addHighSchool(self):
		try:
			x, y = self.findEditBlock(self.srcAddHighSchool)
			self.checkCurrentFullOfUI(self.srcEditHighSchoolUI)
			x, y = self.findElement(self.srcEnterYourHighSchool)
			self.raiseIfError(x, y)
			data = random.choice(self.HighSchoolList)
			self.clickAndInput(x, y, data['name'])
			time.sleep(5)
			x, y = self.findElement('./addHighSchool/'+data['name']+'/'+data['name']+'png')
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
			self.selectDate(True)
			x, y = self.findElement(self.Graduate)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
			x, y = self.findElement(self.srcSave)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
		except UnKnowError:
			self.RestartAppAndWalkInEditUI()
			self.HighSchool()
			return


	def addRelationship(self, data):
		try:
			x, y = self.findEditBlock(self.srcAddRelationship)
			self.checkCurrentFullOfUI(self.srcEditRelationship)
			x, y = self.findElement(self.srcWhatIsYourRelationshipStatus)
			self.raiseIfError(x, y)
			self.d.click(x, y)
			time.sleep(3)
			if not self.d(index='6').exists:
				raies UnKnowError()
			self.d(text='Single').click()
			time.sleep(3)
			x, y = self.findElement(self.srcSave)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
		except UnKnowError:
			self.RestartAppAndWalkInEditUI()
			self.srcAddRelationship()
			return


	def addWork(self):
		try:
			x, y = self.findEditBlock(self.srcAddWork)
			self.checkCurrentFullOfUI(self.srcEditWorkUI)
			x, y = self.findElement(self.srcWhereDidYouWork)
			self.raiseIfError(x, y)
			data = random.choice(self.CoporationList)
			self.clickAndInput(x, y, data['name'])
			time.sleep(5)
			x, y = self.findElement('./addWork/Position/'+data['name']+'/'+data['name']+'png')
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
			x, y = self.findElement(self.srcPosition)
			self.clickAndInput(x, y, data['position'])
			time.sleep(5)
			if data['name'] == 'ChinaResourcesVanguard':
				self.d.swipe(250, 600, 250, 200)
				time.sleep(3)
			x, y = self.findElement('./addWork/Position/'+data['name']+'/'+data['positiublime 怎么输入中文on']+'png')
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
			if data['name'] == '裕華國貨':
				self.d.click(250, 800)
				time.sleep(3)
			x, y = self.findElement(self.CityTown)
			self.raiseIfError()
			self.clickAndInput(x, y, 'HongKong')
			time.sleep(5)
			x, y = self.findElement(self.srcHongKong)
			self.raiseIfError()
			self.selectDate()
			x, y = self.findElement(self.srcSave)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
		except UnKnowError:
			self.RestartAppAndWalkInEditUI()
			self.addWork()
			return


	def calculateDateAtSchool(self, level):
		DATA = {}
		date = {}
		date['Month'] = 'September'
		if level == 'College':
			date['Year'] = self.Birthday['Year'] + 18
		else:
			date['Year'] = self.Birthday['Year'] + 15		
		DATA['Start'] = date
		if level == 'College':
			date['Year'] = date['year'] + 4
		else:
			date['Year'] = date['year'] + 3
		date['Month'] = 'July'		
		day['Day'] = 1
		DATA['End'] = date	
		return DATA


	def calculateDatePosition(x, y):
		current = self.Myscreenshot()
		x, y = self.match_result(current, self.From)
		self.raiseIfError()
		day = (x + 203, y)
		month = (x + 138, y)
		year = (x + 64, y)
		return (year, month, day)


	def checkCurrentFullOfUI(imgobj):
		current = self.d.screenshot('{}.png'.format(self.deviceIp))
		time.sleep(1)
		x, y = self.matchImg(current, imgobj, 0.8)
		self.raiseIfError()


	def clickAndInput(x, y, data):
		if x == y == 0:
			pass
		else:
			self.d.click(x, y)
			time.sleep(3)
		dataList = data.splite(' ')
		length = len(dataList)
		if length > 1:
			times = 0
			for i in dataList:
				times += 1
				os.popen("adb -s {} shell am broadcast -a ADB_INPUT_TEXT --es msg '{}'".format(self.deviceIP, i))
				time.sleep(2)
				if times < length:
					os.popen('adb -s {} shell input keyevent 62')
					time.sleep(2)
		else:
			os.popen("adb -s {} shell am broadcast -a ADB_INPUT_TEXT --es msg '{}'".format(self.deviceIP, data))
			time.sleep(2)


	def clickWait(self):
		if self.d(text='wait').exists():	
		self.d(text='wait').click()
		time.sleep(10)


	def findEditBlock(imgsrc):
		'''用来在第一个选择界面寻找编辑如工作、大学的入口，没找到的时候会向下滑动，超时会抛出异常，由上级承接。
		'''
		current = self.Myscreenshot()
		time.sleep(1)
		match_result = matchImg(current, imgsrc)
		t = time.time()
		while match_result == None or match_result['confidence'] < 0.8:
			ttt = time.time() - t
			self.d.swipe(250, 600, 250, 400)
			time.sleep(3)
			current = self.Myscreenshot()
			time.sleep(1)
			match_result = matchImg(current, imgsrc)
			if ttt > 100:
				raise UnKnowError()
			self.clickWait()
		x, y = match_result['result']
		self.d.click(x, y)
		time.sleep(5)


	def findElement(imgsrc):
		'''在当前界面内寻找指定的图片位置，如果没找到，返回(0,0)。
		'''
		current = self.d.screenshot()
		result = self.matchImg(current, imgsrc)
		if result == None:
			return (0, 0)
		else:
			return  result['result']


	def getBirthday(self):
		'''从Facebook个人中心获取到用户的生日信息。
			这里我想过不在RestartApp函数里面调用，但是不好处理，建议以类实例调用，并保存起来，避免反复获取。
			上述建议只需将RestartApp函数中的调用此函数部分删去，在进行其他任务前以类实例调用一次即可。
			需注意facebook界面须在个人中心处，并额外处理app停止运行的情况。
		'''
		t = time.time()
		while not self.d(textContains='Born on').exists:
			ttt = time.time() - t
			self.d.swipe(250, 800, 250, 300)
			time.sleep(4)
			if ttt > 100:
				raise UnKnowError()
		self.d.dump('{}.text'.format(self.deviceIP))
		time.sleep(1)
		with open('{}.text'.format(self.deviceIP)) as f:
			string = f.read()
		month, day, year = re.search('text="Born on[\s]+([\w]+?)[\s]+([\d]+?),[\s]+([\d]+)', string).groups()
		self.Birthday = {'Year': int(year), 'Month': month, 'Day': int(day)}


	def matchImg(imgsrc,imgobj,confidence=0.5):
		'''此函数用来识别一张图片在另一张图片中的位置，返回一个字典.
		使用方法稍作尝试便知，使用的算法我也有，不依赖于aircv模块。
		'''
	    imsrc = ac.imread(imgsrc)
	    imobj = ac.imread(imgobj)
	    match_result = ac.find_template(imsrc,imobj,confidence)
	    if match_result is not None:
	        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])
	    return match_result


	def Myscreenshot(self):
		current = self.d.screenshot('{}.png'.format(self.deviceIP))
		return current
	

	def partOfChooseDate(self, src, data):
		'''供selectDate函数调用'''
		x, y = self.findElement(src)
			self.raiseIfError()
			self.d.click(x, y)
			time.sleep(3)
			self.swipeAndClick(x, y, data)


	def raiseIfError(self, x, y):
		'''重复调用'''
		if x = y == 0:
			raise UnKnowError()


	def RestartAppAndWalkInEditUI(self):
		os.popen('adb -s {} shell am start -n com.facebook.katana/.LoginActivity'.format(self.deviceIP))
		time.sleep(5)
		os.popen('adb -s {} shell am force-stop com.facebook.katana'.format(self.deviceIP))
		time.sleep(30)
		if self.d(description='More').exists:
			self.d(description='More').click()
			time.sleep(3)
		else:
			self.RestartAppAndWalkInEditUI()
			return
		if self.d(descriptionContains='View your profile').exists:
			self.d(descriptionContains='View your profile').click()
			time.sleep(5)
		else:
			self.RestartAppAndWalkInEditUI()
			return
		try:
			self.getBirthday()
		except UnKnowError:
			self.RestartAppAndWalkInEditUI()
			return
		t = time.time()
		while not self.d(text='ADD DETAILS ABOUT YOU').exists and not self.d(text='EDIT DETAILS').exists and ttt < 100:
			ttt = time.time() - t
			self.d.swpie(250, 200, 250, 600)
			time.sleep(3)
			self.clickWait()
			if ttt > 100:
				self.RestartAppAndWalkInEditUI()
				return
		if self.d(text='ADD DETAILS ABOUT YOU').exists:
			self.d(text='ADD DETAILS ABOUT YOU').click()
			time.sleep(3)
		elif self.d(text='EDIT DETAILS').exists:
			self.d(text='EDIT DETAILS').click()
			time.sleep(3)
		else:
			self.RestartAppAndWalkInEditUI()
			return


	def selectDate(self, signal=False):
		year_x, year_y, month_x, month_y, day_x, day_y = self.calculateDatePosition()
		if signal:
			self.swipeAndClick(year_x, year_y, self.atSchoolDate['Start']['Year'])
		if signal:
			Data = self.atSchoolDate['Start']
		else:
			Date = self.workDate
		self.swipeAndClick(month_x, month_y, Data['Month'])
		self.swipeAndClick(day_x, day_y, Data['Day'])
		if signal:
			self.partOfChooseDate(self.srcYear, self.atSchoolDate['End']['Year'])
			self.partOfChooseDate(self.srcMonth, self.atSchoolDate['End']['Month'])
			self.partOfChooseDate(self.srcDay, self.atSchoolDate['End']['Day'])


	def swipeAndClick(self, x, y, data):
		self.d.click(x, y)
		time.sleep(3)
		if not d(index='6').exists:
			raise UnKnowError()
		t = time.time()
		while not self.d(text='{}'.format(data)).exists:
			ttt = time.time() - t
			self.d.swipe(250, 800, 250, 200)
			time.sleep(3)
			self.clickWait()
			if ttt > 60:
				raise UnKnowError()
		self.d(text='{}'.format(data)).click()
		time.sleep(3)


