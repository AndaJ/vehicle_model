# -*- coding: utf-8 -*- 

import sys
import os
import urllib.request
import re
import time

def dataExtractOnline(url):
  #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} #发送一个head，反网址禁止爬虫
  opener=urllib.request.build_opener()
  opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
  urllib.request.install_opener(opener)

  req = urllib.request.Request(url) #爬虫第一层网址
  html = urllib.request.urlopen(req,timeout=20).read()
  html=html.decode('utf-8')

  #reg = r'src="(http.+?\.jpg)"' #表示在整个网页中过滤出所有图片的地址
  #imgre = re.compile(reg)
  #imglist = re.findall(imgre,html)  

  reg = r'href="/cn/nomer.+?"' #过滤出china车牌的图片地址
  imgre = re.compile(reg)
  imglist = re.findall(imgre,html)

  #reg2 = r'href="/cn/foto.+?"'
  #imgre2 = re.compile(reg2)
  #imglist2 = re.findall(imgre2,html)

  imglist=list(set(imglist))
  for i in range(0,len(imglist)):
    imgurl=imglist[i]
    filepath_nomer="http://platesmania.com/cn/nomer"+imgurl[15:len(imgurl)-1]
    filepath_foto="http://platesmania.com/cn/foto"+imgurl[15:len(imgurl)-1]
  
    #print(filepath_nomer) #爬虫第二层网址
    req1 = urllib.request.Request(filepath_nomer)
    html1 = urllib.request.urlopen(req1,timeout=20).read()
    html1=html1.decode('utf-8')
    #print(type(html1))
  
    reg1 = r'<title>.+?</title>' #车牌字段信息提取的正则表达式
    imgre1 = re.compile(reg1)
    imglist1 = re.findall(imgre1,html1)
   
    reg2 = r'src="(http.+?\.png)"' #车牌下载地址的正则表达式
    imgre2 = re.compile(reg2)
    imglist2 = re.findall(imgre2,html1)
  
  
    #print(imglist1[0],imglist2[0])
  
    req2 = urllib.request.Request(filepath_foto) #爬虫第三层网址
    html2 = urllib.request.urlopen(req2,timeout=20).read()
    html2=html2.decode('utf-8')
  
    reg3 = r'src="(http.+?\.jpg)"' #车图片下载正则表达式，且获取下载地址
    imgre3 = re.compile(reg3)
    imglist3 = re.findall(imgre3,html2)
  
    ATimage_name=imglist1[0][7:15]
    ATfile_name=imglist1[0][7]
    results_path="D:/mywork/urldata"
  
  
    print(ATimage_name)
  
    if ATfile_name in os.listdir(results_path): #保存
      results_file=results_path+'/'+ATfile_name  
    else:  
      os.makedirs(os.path.join(results_path,ATfile_name))
      results_file=results_path+'/'+ATfile_name
  
    urllib.request.urlretrieve(imglist2[0],results_file+'/'+ATimage_name+'_license.jpg') #车牌的图片
    urllib.request.urlretrieve(imglist3[0],results_file+'/'+ATimage_name+'_car.jpg') #车的图片
  

if __name__=='__main__':
  for k in range(0,750):
    url="http://platesmania.com/cn/gallery-"+str(k)
    print(url)
	
    try:
      dataExtractOnline(url)
    except Exception as e:
      print(e)
	  
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

