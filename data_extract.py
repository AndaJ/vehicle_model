# -*- coding: utf-8 -*- 

import sys
import os
import urllib.request
import re
import time

def dataExtractOnline(url,save_path):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} #发送一个head，反网址禁止爬虫
	opener=urllib.request.build_opener()
	opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
	urllib.request.install_opener(opener)

	req = urllib.request.Request(url) #爬虫第一层网址
	html = urllib.request.urlopen(req,timeout=20).read()
	html=html.decode('utf-8')

	imgname = []

	
	reg = r'\|.+img src="http://img.chinacar.com.cn/spic/[\w]+\.jpg'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)

	for img in imglist:
	# re1 = r'\w.+\)'
		re1 = r'\w.+\)'
		imgre1 = re.compile(re1)
		name = re.findall(imgre1,img)
		imgname.append(name)
		# print(name)
		re2 = r'http.+\.jpg'
		imgre2 = re.compile(re2)
		urltemp = re.findall(imgre2,img)

		print(urltemp)
		# print(type(urltemp))
		
		save_dir = os.path.join(save_path,name[0]+'.jpg')
		urllib.request.urlretrieve(urltemp[0],save_dir)
		# print(url)
	# print(imgname)

  # imglist=list(set(imglist))
  # for i in range(0,len(imglist)):
    # imgurl=imglist[i]
    # filepath_nomer="http://platesmania.com/cn/nomer"+imgurl[15:len(imgurl)-1]
    # filepath_foto="http://platesmania.com/cn/foto"+imgurl[15:len(imgurl)-1]
  
    # #print(filepath_nomer) #爬虫第二层网址
    # req1 = urllib.request.Request(filepath_nomer)
    # html1 = urllib.request.urlopen(req1,timeout=20).read()
    # html1=html1.decode('utf-8')
    # #print(type(html1))
  
    # reg1 = r'<title>.+?</title>' #车牌字段信息提取的正则表达式
    # imgre1 = re.compile(reg1)
    # imglist1 = re.findall(imgre1,html1)
   
    # reg2 = r'src="(http.+?\.png)"' #车牌下载地址的正则表达式
    # imgre2 = re.compile(reg2)
    # imglist2 = re.findall(imgre2,html1)
  
  
    # #print(imglist1[0],imglist2[0])
  
    # req2 = urllib.request.Request(filepath_foto) #爬虫第三层网址
    # html2 = urllib.request.urlopen(req2,timeout=20).read()
    # html2=html2.decode('utf-8')
  
    # reg3 = r'src="(http.+?\.jpg)"' #车图片下载正则表达式，且获取下载地址
    # imgre3 = re.compile(reg3)
    # imglist3 = re.findall(imgre3,html2)
  
    # ATimage_name=imglist1[0][7:15]
    # ATfile_name=imglist1[0][7]
    # results_path="D:/mywork/urldata"
  
  
    # print(ATimage_name)
  
    # if ATfile_name in os.listdir(results_path): #保存
      # results_file=results_path+'/'+ATfile_name  
    # else:  
      # os.makedirs(os.path.join(results_path,ATfile_name))
      # results_file=results_path+'/'+ATfile_name
  
    # urllib.request.urlretrieve(imglist2[0],results_file+'/'+ATimage_name+'_license.jpg') #车牌的图片
    # urllib.request.urlretrieve(imglist3[0],results_file+'/'+ATimage_name+'_car.jpg') #车的图片
  

if __name__=='__main__':
	
	save_path = ".\picture\奥迪"
	
	url_pre = "http://www.chinacar.com.cn/keche/aodi_3329/"
	for k in range(1,2):
		if(k == 1):
			url_last = ''
		else:
			url_last = 'index_'+str(k)+'.html'
    # url="http://platesmania.com/cn/gallery-"+str(k)
		url = url_pre + url_last
		print(url)

		# try:
		dataExtractOnline(url,save_path)
		# except Exception as e:
			# print(e)
	  
	print('爬虫结束！')
  
 


 
 
 
 
'''

#reg2 = r'href="/cn/foto.+?"'
#imgre2 = re.compile(reg2)
#imglist2 = re.findall(imgre2,html)

#print(imglist,imglist1)

#req1 = urllib.request.Request("http://platesmania.com/cn/nomer11616358")
#html1 = urllib.request.urlopen(req1).read()

#print(html1)

#x = 0
#for imgurl in imglist:
#  print(imgurl)
#  file_name=os.path.split(imgurl)
#  file_name_Before=os.path.splitext(file_name[1])

 


# opener=urllib.request.build_opener()
#  opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
#  urllib.request.install_opener(opener)
  
  #req2 = urllib.request.Request(url=imgurl, headers=headers)
  
#  urllib.request.urlretrieve(imgurl,'D:/mywork/urldata/'+str(x)+'.png')
# x = x+1

 
#print(getimg(html))

'''

