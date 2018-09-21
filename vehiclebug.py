# -*- coding: utf-8 -*- 

import sys
import os
import urllib.request
import re
import time
'''
	网络爬虫
	爬取汽车图片
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

	# 查找所有品牌
	reg = r'<dd ><a href=(.*)</dd>'
	# reg = r'\|.+img src="http://img.chinacar.com.cn/spic/[\w]+\.jpg'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	
	
	icount = 0
	for sp in imglist:
		# print("sp:",sp)
		
		imgsplit = sp.split('<dd >')
		# print("imgsplit:",imgsplit)
		# os.system("pause")
		for sp2 in imgsplit:
			# if(icount<=52):
				# continue
			#品牌url
			reg2 = r'"/.+/"'
			imgre2 = re.compile(reg2)
			url2= re.findall(imgre2,sp2)[0]
			# print("url2:",url2)
			
			reg4 = r'/.+/'
			imgre4 = re.compile(reg4)
			url4= re.findall(imgre4,url2)[0]
			#品牌名
			reg3 = r'>.+/a'
			imgre3 = re.compile(reg3)
			brand_temp= re.findall(imgre3,sp2)[0]
			brand_1 = brand_temp.split('>')[1]
			brand = brand_1.split('<')[0]
			
			print(brand,"  ",str(icount))
			
			#保存文件夹
			save_dir = os.path.join(save_path,brand)
			if(not os.path.exists(save_dir)):
				os.mkdir(save_dir)
				
			icount+=1
			if(icount<=96):
				continue
			url_brand = 'http://www.chinacar.com.cn'+url4
			
			for k in range(1,300):
				if(k==1):
					url_last = ''
				else:
					url_last = 'index_'+str(k)+'.html'
				
				url_all = url_brand + url_last
				try:
					if(not downloadjpg(url_all,save_dir)):
						break
				except Exception as e:
					print(e)


if __name__=='__main__':
	
	save_path = ".\picture"
	
	url_pre = "http://www.chinacar.com.cn/keche/anchi_7/"

	try:
		dataExtractOnline(url,save_path)
	except Exception as e:
		print(e)
	  
	print('爬虫结束！')
  
 


 
 
 
 


