import requests
import base64
import json

url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=24.29e3920ead0e11bc62f95294f61e6021.2592000.1535622359.282335-11614886'
string = requests.get('https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=2VbPbE4VRhrFyml3yopZRSW6&client_secret=rUWX1y9Uv3kyDCG9bevk9aRMYem31BwE').text
dic = json.loads(string)
access_token = dic['access_token']
path = input('input your picture road: ')
with open(path, 'rb') as f:
	binary = f.read()
basecode = base64.b64encode(binary)
params = {'image': basecode}
result = requests.post(url, params).text
dic = json.loads(string)['words_result']
for i in dic:
	print(i['words'])
