from bs4 import BeautifulSoup
import urllib2
import urllib
from urllib import FancyURLopener

# use this image scraper from the location that 
#you want to save scraped images to

class MyOpener(FancyURLopener, object):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


def make_soup(url):
	try:
		myopener = MyOpener()
		html = myopener.retrieve(url, 'useragent.html')
	except  e:
		print e
		return
	print(html)
	return BeautifulSoup(html, "html5lib")

def get_images(url):
	soup = make_soup(url)

	#this makes a list of bs4 element tags
	images = [img for img in soup.findAll('img')]
	print (str(len(images)) + "images found.")
	print 'Downloading images to current working directory.'
	#compile our unicode list of image links
	image_links = [each.get('src') for each in images]
	for each in image_links:
		filename=each.split('/')[-1]
		print(filename)
        print(each)#urllib.urlretrieve(each, filename)
	return image_links

#a standard call looks like this
#get_images('http://www.wookmark.com')
