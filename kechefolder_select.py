# -*- coding: utf-8 -*- 

import sys
import os
import urllib.request
import re
import shutil
import numpy as np
# import pandas as pd

'''
	说明：合并车型目录
	将ImagePath的车型合并到ModelPath目录中
'''


'''
	function:find bran list from Image Path
	params:
		ImagePath:	Image path 
		reg:	split char
		index:	char segment index
'''
def find_brand_list(ImagePath, reg, index):
	
	
	subdir = os.listdir(ImagePath)
	
	namelist = []
	for dir in subdir:
		reobj = re.compile(reg)
		str = re.findall(reobj,dir)
		if(len(str)>0):
			str = str[0].split('_')[index]
			
			for n in [str]:
				namelist.append(n)
	namelist = set(namelist)
	return namelist
	
	
#craete new branch folder
def newfolder(namelist,ModelPath):
	modellist = os.listdir(ModelPath)
	for brand in namelist:
		isexist = False
		for model in modellist:
			if(model==brand or model==brand+'牌'):
				isexist = True
				break
		if(not isexist):
			brand += '牌'
			save_dir = os.path.join(ModelPath,brand)
			os.mkdir(save_dir)
			# print(save_dir)
			
def copyImage(ImagePath, ModelPath, reg):
	subdir = os.listdir(ImagePath)
	for dir in subdir:
	
		branddir = os.path.join(ImagePath,dir)
		
		reobj = re.compile(reg)
		str = re.findall(reobj,dir)
		if(len(str)>0):
			
			str = re.split(r'_+',str[0])
			brand = str[1]+'牌'
			if(len(str)>3):
				model = str[2]
			else:
				model = "未知"
			save_dir = os.path.join(ModelPath,brand,model)
			if(not os.path.exists(save_dir)):
				os.mkdir(save_dir)
				
			imglist = os.listdir(branddir)
			print(save_dir)
			for imgname in imglist:
				imgdir = os.path.join(branddir,imgname)
				shutil.copy(imgdir,save_dir)
def copy_car_image(ImagePath, ModelPath, reg):
	subdir = os.listdir(ImagePath)
	
	count = 0
	for dir in subdir:
	
		branddir = os.path.join(ImagePath,dir)
		print(dir)
		reobj = re.compile(reg)
		str = re.findall(reobj,dir)
		count += 1
		print(count)
		if(len(str)>0):
			
			str = re.split(r'_+',str[0])
			brand = str[0]+'牌'
			if(len(str)>=2):
				model = str[1]
			else:
				model = "未知"
			save_dir = os.path.join(ModelPath,brand,model)
			if(not os.path.exists(save_dir)):
				os.mkdir(save_dir)
				
			imglist = os.listdir(branddir)
			# print(save_dir)
			for imgname in imglist:
				imgdir = os.path.join(branddir,imgname)
				# shutil.copy(imgdir,save_dir)
				copyfile(imgdir,save_dir)

def copyfile(imgdir,save_dir):
	if(os.path.isfile(imgdir)):
		shutil.copy(imgdir,save_dir)
	else:
		folderlist = os.listdir(imgdir)
		for folder in folderlist:
			folderPath = os.path.join(imgdir,folder)
			copyfile(folderPath,save_dir)
				
def truck():
	ModelPath = "F:\\projects\\vehicle_model\\truck"
	ImagePath1 = "F:\\projects\\第一组"
	ImagePath2 = "F:\\projects\\第二组"
	reg = r'货车.+'
	
	for i in range(2):
		if(i==0):
			ImagePath = ImagePath1
		else:
			ImagePath = ImagePath2
		namelist = find_brand_list(ImagePath, reg, 1)
		# print(namelist)
		#new folder
		newfolder(namelist,ModelPath)
		copyImage(ImagePath, ModelPath, reg)
	
def coach():
	ModelPath = "F:\\projects\\vehicle_model\\coach"
	ImagePath1 = "F:\\projects\\第一组"
	ImagePath2 = "F:\\projects\\第二组"
	reg = r'客车.+'
	
	for i in range(2):
		if(i==0):
			ImagePath = ImagePath1
		else:
			ImagePath = ImagePath2
		namelist = find_brand_list(ImagePath, reg, 1)
		#new folder
		newfolder(namelist,ModelPath)
		copyImage(ImagePath, ModelPath, reg)
		
def car():
	ModelPath = "F:\\projects\\vehicle_model\\car"
	ImagePath1 = "F:\\projects\\第一组"
	ImagePath2 = "F:\\projects\\第二组"
	reg = r'[^客车].+'
	
	subdir = os.listdir(ImagePath1)
	
	for i in range(2):
		if(i==0):
			ImagePath = ImagePath1
		else:
			ImagePath = ImagePath2
		namelist = find_brand_list(ImagePath, reg, 0)
		newfolder(namelist,ModelPath)
		copy_car_image(ImagePath, ModelPath, reg)
	
def main():
	#货车
	truck()
	
	#客车
	coach()
	
	#小车
	# car()
	print("Done.")

if __name__=='__main__':
	main()
	
	
		
