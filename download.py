import requests 
import zipfile 
import io
import os 
import csv

try:
	with open('result.csv', 'r') as f:
		lastDone = int(','.join(reversed(list(csv.reader(f))[-1])).split(",")[0])
except:
	lastDone = 0

for code in range(lastDone,99999):
	r = requests.get("http://dl.stickershop.line.naver.jp/products/0/0/1/"+ str(code) +"/iphone/stickers@2x.zip")
	
	with open("result.csv","a") as f:
		f.write(str(r.status_code) + "," + str(code) + "\n")
	print(str(r.status_code) + "," + str(code))
	if (r.status_code!=404):
		z = zipfile.ZipFile(io.BytesIO(r.content))
		z.extractall("./"+str(code)+"/")
		for i in os.listdir("./"+str(code)+"/"):
			if "_key" in i:
				os.remove("./"+str(code)+"/"+i)
