import bs4
import requests
import warnings
import csv
import datetime
import sys
import pandas as pd
from fileinput import FileInput
from itertools import tee
warnings.filterwarnings('ignore')

def DBAscraper():
	print("\n       ============================ \n       |        DBA Scraper       |\n       |   by David Shmilowitz    |\n       |   &    Joseph Awwal      |    \n       ============================ \n")	
	for i in range(1,100):
		url = "http://www.dba.dk/boliger/ejerbolig/side-{}/".format(i)
		r = requests.get(url)
		r.raise_for_status()
		soup = bs4.BeautifulSoup(r.text)
		date,price,link,desc = [],[],[],[]
		encoding = 'Cp1252'
		listings = soup.findAll('tr', 'dbaListing')
		for listing in listings:
			#URL
			link.append(listing.find('a', 'listingLink')['href'])
			#Description 
			d = listing.find('div', 'expandable-box expandable-box-collapsed')
			#Removing the last 50 characters (Annoncen præsenteres i samarbejde med Boligsiden)
			desc.append(d.find('a', 'listingLink').text.strip()[:-50])
			#Date
			date.append(listing.find('td', {'title': 'Dato'}).text.strip())
			#Check for "I dag"/"I går" and change to current date
			for index,item in enumerate(date):
				if item == 'I dag':
					date[index] = ("%s/%s" % (datetime.datetime.now().day, datetime.datetime.now().month))
				elif item == 'I går':
					date[index] = ("%s/%s" % (datetime.datetime.now().day-1, datetime.datetime.now().month))
			#Price
			price.append(listing.find('td', {'title': 'Pris'}).text.strip())
			
		results =  list(zip(date,price,link,desc))

		with open('DBA.csv', 'a', encoding='Cp1252', newline='') as f:
			writer = csv.writer(f,delimiter=",")
			if i == 1:
				writer.writerow(["Date", "Price DKK","URL","Description"])
			for item in results:
				writer.writerow(item)
		print(url + " Page {} Done".format(i))
		
def deleteDuplicate():
	# seen = set()
	# dupeCount = 0
	# for line in fileinput.FileInput('DBA.csv', inplace=1):
		# linesplit = line.split (",")[2]
		# if linesplit in seen:
			# dupeCount+=1
			# continue # skip duplicated line
		# seen.add(linesplit)
		# print(line, end='')
	# print(seen)
	# print("Removed {} Duplicates".format(dupeCount))
	
	seen = set()
	dupeCount = 0
	counter = 0
	with FileInput('DBA.csv', inplace=1) as f:
		f, f_orig = tee(f)
		for row, line in zip(csv.reader(f), f_orig):
			if row[2] in seen:
				dupeCount+=1
				continue
			seen.add(row[2])
			counter+=1
			print(line, end='')
		print(counter)
		print("Removed {} Duplicates".format(dupeCount))

DBAscraper()
deleteDuplicate()

