# -*- coding: utf-8 -*- 

import sys
import os
import urllib.request
import re
import time
'''
	网络爬虫
	爬取小车图片
'''

def downloadjpg(url,save_path):
	req2 = urllib.request.Request(url) #爬虫第一层网址
	html2 = urllib.request.urlopen(req2,timeout=20).read()
	html2 = html2.decode('utf-8')
	

	reg10 = r'\|.+img src="http://img.chinacar.com.cn/spic/[\w]+\.jpg'
	imgre10 = re.compile(reg10)
	imglist10 = re.findall(imgre10,html2)
	
	if(len(imglist10)==0):
		return False
	
	for img in imglist10:
	# re1 = r'\w.+\)'
		re1 = r'\w.+\)'
		imgre1 = re.compile(re1)
		name = re.findall(imgre1,img)
		# print(name)
		re2 = r'http.+\.jpg'
		imgre2 = re.compile(re2)
		urltemp = re.findall(imgre2,img)


		# print(type(urltemp))
		print(urltemp[0])
		save_dir1 = os.path.join(save_path,name[0]+'.jpg')
		urllib.request.urlretrieve(urltemp[0],save_dir1)
	return True

def dataExtractOnline(url,save_path):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} #发送一个head，反网址禁止爬虫
	opener=urllib.request.build_opener()
	opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) 				Chrome/36.0.1941.0 Safari/537.36')]
	urllib.request.install_opener(opener)

	req = urllib.request.Request(url) #爬虫第一层网址
	html = urllib.request.urlopen(req,timeout=20).read()
	html=html.decode('utf-8')
	#查找所有品牌
	# reg = r'<div class="tb-pinpai">[\s\S]*?<div class="case_left">'
	reg = r'<div class="tb-pinpai">[\s\S]*?</ul>'
	reobj = re.compile(reg)
	brandlist = re.findall(reobj,html)
	
	info_brand_url = {}

	for brandseg in brandlist:

		
		reg = r'<div class="tb-pinpai">.+</a></div>'
		regobj = re.compile(reg)
		brand = re.findall(regobj,brandseg)
		brand = brand[0]
		
		reg = r'title.+target'
		regobj = re.compile(reg)
		brand = re.findall(regobj,brand)
		brand = brand[0]
		
		reg = r'"'
		brand = re.split(reg,brand)
		brand = brand[1]
		brand += '牌'
		# print("***************************************",brand)

		# 查找所有型号
		reg = r'<li><a href="/jiaoche/serie_.+</a></li> '
		imgre = re.compile(reg)
		imglist = re.findall(imgre,brandseg)
		# print(imglist)
		
		info_model_url = []
		
		for sp in imglist:
		# print("sp:",sp)
		
			imgsplit = sp.split('</a></li>')
			# print("imgsplit:",imgsplit)
			
			for sp2 in imgsplit:
				if(sp2 == " "):
					continue
				
				info = []
				#extract url
				reg = r'"/.+html"'
				reobj = re.compile(reg)
				url_model = re.findall(reobj,sp2)
				url_model = url_model[0]
				# print(url_model)
				reg = r'/.+html'
				reobj = re.compile(reg)
				url_model = re.findall(reobj,url_model)
				url_model = url_model[0]
				url_model = url_root + url_model
				
				#extract title
				reg = r'title=.+"'
				reobj = re.compile(reg)
				title = re.findall(reobj,sp2)
				title = title[0]
				
				reg = r'"'
				title = re.split(reg,title)
				title = title[1]
				
				info.append(title)
				info.append(url_model)
				
				info_model_url.append(info)
				# print(url_model)
		info_brand_url[brand] = info_model_url
	
	return info_brand_url
	
			


if __name__=='__main__':
	
	save_path = ".\picture"
	
	url_root = "http://www.chinacar.com.cn"
	
	url = "http://www.chinacar.com.cn/jiaoche/all_zwpp.html"

	try:
		info_brand_url = dataExtractOnline(url,save_path)
		# print(info_brand_url)
		count = 0
		for brand in info_brand_url:
			count+=1
			value = info_brand_url[brand]
			print(value,str(count))
	except Exception as e:
		print(e)
	  
	print('爬虫结束！')
  
 


 
 
 
 


