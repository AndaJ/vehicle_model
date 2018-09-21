# -*- coding: utf-8 -*- 

import sys
import os
import urllib.request
import re
import shutil

if __name__=='__main__':
	
	ImagePath = "./pic"
	Save_Path = "./pic_group"
	#subdir
	subdir = os.listdir(ImagePath)
	
	for dir in subdir:
		print(dir)
		
		pic_dir = os.path.join(ImagePath,dir)
		
		save_brand = os.path.join(Save_Path,dir)
		if(not os.path.exists(save_brand)):
			os.mkdir(save_brand)
				
		piclist = os.listdir(pic_dir)

		for imgname in piclist:
			img_dir = os.path.join(pic_dir,imgname)

			reg = r'\d.+\('
			imgre = re.compile(reg)
			str1 = re.findall(imgre,imgname)
			if(len(str1)==0):
				continue
			str1 = str1[0]
			
			str_sp = str1.split('(')
			if(len(str_sp)>0):
				str1 = str_sp[0]
			
			reg1 = r'\d.+\d|\d+'
			imgre1 = re.compile(reg1)
			str2 = re.findall(imgre1,str1)
			
			save_zuo = os.path.join(save_brand,str2[0])
			if(not os.path.exists(save_zuo)):
				os.mkdir(save_zuo)
			
			save_dir = os.path.join(save_zuo,imgname)
			shutil.copyfile(img_dir,save_dir)
			# print(save_dir)
			
		
  
 


 
 
 
 


