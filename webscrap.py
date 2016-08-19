from bs4 import BeautifulSoup
import requests
import datetime
from dateutil.relativedelta import relativedelta

url_template = "http://www.daemonology.net/hn-daily/{0}.html"
month = datetime.date(2010, 7, 1)
current_month = datetime.date.today()
titles = []


while month < current_month:
	print "Scraping month ", month.strftime("%Y-%m"), " ... ", len(titles), 	" articles found so far"
	url = url_template.format(month.strftime("%Y-%m"))
	html = requests.get(url).text
	soup = BeautifulSoup(html, "html5lib")
	uls = soup('ul')
	for ul in uls:
		titles += [span.a.text for span in ul.find_all('span', 'storylink')]

	month += relativedelta(months=1)


