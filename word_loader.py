import urllib2

def get_buzzwords():
	response = urllib2.urlopen("http://www.buzzwordipsum.com/buzzwords?type=words&paragraphs=1")
	return response.readlines()[0]