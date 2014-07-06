import urllib2



#Is given the URL and retrieves the HTML from that page
def getHTML(url):
	source = urllib2.urlopen(str(url))
	s = source.readlines()
	source.close()

	return s
