from bs4 import BeautifulSoup
import requests
import datetime
from dateutil.relativedelta import relativedelta
import pymongo

client = pymongo.MongoClient()
db = client.hackernews_database
titlesByDate = db.titlesByDate

url_template = "http://www.daemonology.net/hn-daily/{0}.html"
curr_date = datetime.date(2010, 7, 11)
today = datetime.date.today()
num_of_titles = 0;


while curr_date < today:
	curr_date_format = curr_date.strftime("%Y-%m-%d")
	print "Scraping date ", curr_date_format, " ... ", num_of_titles, 	" articles found so far"
	url = url_template.format(curr_date_format)
	html = requests.get(url).text
	soup = BeautifulSoup(html, "html5lib")
	ul = soup.ul
	record = { 'date': curr_date_format,
			   'titles': [span.a.text for span in ul.find_all('span', 'storylink')]
			  }
	num_of_titles += len(record['titles'])
	titlesByDate.insert_one(record)
	curr_date += relativedelta(days=1)


def dumpDataToDisk():
	with open('titles.txt', 'w') as f:
		for record in titlesByDate.find():
			for title in record['titles']:
				f.write(title.encode('utf-8') + "\n")
