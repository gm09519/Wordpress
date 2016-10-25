import sys
import csv
import re
import time
import urllib3
from urllib3 import PoolManager, Retry, Timeout
try:
	file = open('domains.txt','r')
	out=open("new_data.csv","w")
	output=csv.writer(out)
	domains=file.readlines()
	http = urllib3.PoolManager(retries=1,timeout=3.0)
	for odomain in domains:
		tmp=odomain.strip()
		domain=tmp.lower()
		print(domain)
		try:
			page = http.request('GET',domain)
			try:
				data = page.data.decode("utf-8")
			except:
				data = page.data.decode("ISO-8859-1")
			print(type(data))
			set=[];
			set.append(domain)
			if (data.find("wordpress")):
				set.append("TRUE")
				v = re.search('<meta name="generator" content="(.+?)" />',data)
				if v:
					set.append(v.group(1))
			elif (data.find("wp-content")):
				set.append("TRUE")
				v = re.search('<meta name="generator" content="(.+?)" />',data)
				if v:
					set.append(v.group(1))
			else:
				set.append("False")
			output.writerow(set)
			print ("1")
		except:
			print("not connected")
		#for row in service
	out.close()
	file.close()
except Exception as e:
	print ('Error: %s' % e)
	out.close()
	file.close()
	sys.exit(1)
