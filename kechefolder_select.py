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

if __name__=='__main__':
	
	ModelPath = "./pic_group"
	ImagePath = "./第一组"
	
	modellist = os.listdir(ModelPath)
	#subdir
	subdir = os.listdir(ImagePath)
	
	namelist = []
	for dir in subdir:
		
		reg = r'客车.+'
		reobj = re.compile(reg)
		str = re.findall(reobj,dir)
		if(len(str)>0):
			str = str[0].split('_')[1]
			for n in [str]:
				namelist.append(n)
	namelist = set(namelist)
	
	for name in namelist:
		isexist = False
		for model in modellist:
			if(model==name or model==name+'牌'):
				isexist = True
				break
		if(not isexist):
			name += '牌'
			save_dir = os.path.join(ModelPath,name)
			os.mkdir(save_dir)
			print(save_dir)
		
