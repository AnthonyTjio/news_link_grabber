# -*- coding: utf-8 -*-

from linkGrabber import Links
import re
import numpy as np
import json
from grabber import Grabber

with open("conf.json") as conf:
	sites = json.load(conf)
	for site in sites:
		Grabber.generate_links(site["src"], site["base_url"], site["regex"])


