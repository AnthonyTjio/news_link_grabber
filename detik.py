# -*- coding: utf-8 -*-

from linkGrabber import Links
import re
import numpy as np
import os

link_list = []
des = open('links/updated_detik.txt','w')

if os.path.isfile("links/detik.txt"):
	src = open('links/detik.txt', 'r')
	master_links = []
	rdum = src.readlines()
	for x in rdum:
		master_links.append(x)

else:
	master_links = ["https://detik.com"]

# wildcard = '(/.*){1}/(\w)*/?$'
regex = '^(.*/read/.*|.*/d-[0-9]*/.*)$'

for index,master_link in enumerate(master_links):
	try:
		links = Links(master_link)
		temp_list = links.find(href=re.compile(regex), duplicate=False)
		for x in temp_list:
			href = x['href']
			link_list.append(href)
	except ValueError:
		print master_link+' fails!'
			

link_list = np.unique(link_list)
link_list = np.array([listx for listx in link_list if 'page' not in listx])

for href in link_list:
	des.write(href+'\n')

if os.path.isfile("links/detik.txt"):
	os.remove('links/detik.txt')
os.rename('links/updated_detik.txt', 'links/detik.txt')
# print(link_list)


