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
	pos = 0
	with open("./class_static.txt","w") as f:
		for cls in subdir:
			# print(cls)
			
			cls_dir = os.path.join(ImagePath,cls)
				
			zw_list = os.listdir(cls_dir)
			
			
			str1 = str(index)
			
			
			
			index += 1
			
			# print(str1)
			for zw in zw_list:
				
				
				f.write(str1)
				pos += 15
				f.seek(pos,0)
				
				str2 = str1
				
				zw_dir = os.path.join(cls_dir, zw)
				
				piclist = os.listdir(zw_dir)
				pic_count = len(piclist)
					
				f.write(cls)
				pos += 15
				f.seek(pos,0)
				
				f.write(zw)
				pos += 15
				f.seek(pos,0)
				
				f.write(str(pic_count))
				pos += 15
				f.seek(pos,0)
				
				f.write("\n")
			
  
 


 
 
 
 


