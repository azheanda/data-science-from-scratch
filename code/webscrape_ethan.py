from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.daemonology.net/hn-daily/2016-08.html").text
soup = BeautifulSoup(html, "html5lib")
uls = soup('ul')

titles = []

for ul in uls:
	spans = ul.find_all('span', 'storylink')
	titles += [span.a.text for span in spans]

for title in titles:
	print title

