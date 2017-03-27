# -*- coding: utf-8 -*-

from linkGrabber import Links
import re
import numpy as np
import os

class Grabber:

	@classmethod
	def generate_links(self, src, base_url, regex):
		regex = regex
		master_links = []
		link_list = []
		if os.path.isfile('links/'+src+'.txt'):
			srcdum = open('links/'+src+'.txt', 'r')
			rdum = srcdum.readlines()
			if not rdum:
				master_links.append(base_url)
				print master_links
			else:
				for x in rdum:
					master_links.append(x)
		else:
			master_links.append(base_url)
			print master_links

		for master_link in master_links:
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

		des = open('links/updated_'+src+'.txt','w')
		for href in link_list:
			des.write(href+'\n')

		if os.path.isfile('links/'+src+'.txt'):
			os.remove('links/'+src+'.txt')
		os.rename('links/updated_'+src+'.txt', 'links/'+src+'.txt')


