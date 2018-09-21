# -*- coding: utf-8 -*- 

import sys
import os
import urllib.request
import re
import shutil

if __name__=='__main__':
	
	ImagePath = "./pic_group"

	subdir = os.listdir(ImagePath)
	index = 1
	with open("./class_static.txt","w") as f:
		for cls in subdir:
			# print(cls)
			
			cls_dir = os.path.join(ImagePath,cls)
				
			zw_list = os.listdir(cls_dir)
			
			str1 = str(index)
			
			index += 1
			indexset = set(str(index))
			chcount = len(indexset)
			for i in range(chcount,15):
					str1 += " "
			# print(str1)
			for zw in zw_list:
				# print(cls,"...",zw)
				
				str2 = str1
				print(str2)
				
				zw_dir = os.path.join(cls_dir, zw)
				
				piclist = os.listdir(zw_dir)
				pic_count = len(piclist)
				strset = set(cls)
				chcount = len(strset)
				str2 += cls
				# print(str2)
				for i in range(chcount,25):
					str2+=" "
				str2 += zw
				zwset = set(zw)
				chcount = len(zwset)
				for i in range(chcount,15):
					str2+=" "
				str2 += str(pic_count)
				str2 += "\n"
				
				f.write(str2)
			
  
 


 
 
 
 


