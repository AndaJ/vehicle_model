# -*- coding: utf-8 -*- 

import sys
import os
import urllib.request
import re
import shutil

if __name__=='__main__':
	
	strs = "                  <li><a href=jiaocheserie_758.html target=_blank title=猎鹰>猎鹰</a></li><li><a href=jiaoche/serie_759.htmltarget=_blank title=永源A380>永源A380</a></li><li><a href=jiaoche/serie_760.html target=_blank title=永源五星>永源五星</a></li>"
	
	reg = r'^<li><a href='
	imgre = re.compile(reg)
	imglist = re.findall(imgre,strs)
	print(imglist)
