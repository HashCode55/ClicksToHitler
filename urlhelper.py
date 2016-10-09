"""
Module for fetching and cleaning the URL's
"""
import bs4
from urllib import request
import re 

def fetch(url, regex_patt):
	"""
	Extracts the links from the given url
	"""
	text = request.urlopen(url)
	bs_text = bs4.BeautifulSoup(text, 'lxml')
	url_list = []
	for link in bs_text.find_all('a'):
		url_list.append(str(link.get('href')))
	#get the cleaned list	
	url_list = clean(url_list, regex_patt)
	url_list = list(map((lambda x : 'https://en.wikipedia.org' + x), url_list))
	return set(url_list)

def clean(urls, patt):
	"""
	Used to clean the list of urls 
	"""
	cleaned_list = []
	for url in urls:
		if patt.match(url) and 'disambiguation' not in url:
			if '#' in url:
				url = url[:url.index('#')]
			cleaned_list.append(url)
	return cleaned_list
