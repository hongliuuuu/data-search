
from mock import Mock

from google import google
from six.moves import urllib
from bs4 import BeautifulSoup

def dataset_verify(website):
    ''' To verify if this website contains the dataset we want'''
    page = urllib.request.urlopen(website).read()
    # firstly to see the frenquency of keywords
    data = page.lower().count("data")+page.lower().count("dataset")
    feature = page.lower().count("feature")+page.lower().count("variable")+page.lower().count("attribute")
    instance = page.lower().count("sample")+page.lower().count("instance")+page.lower().count("patient")
    return data&(feature|instance)



num_page = 1
search_results = google.search("dataset", num_page)


website = "http://stackoverflow.com/questions/27180789/python-search-for-words-before-and-after-a-pair-of-keywords"
if (dataset_verify(website)): print 'yes'
#for result in search_results:
 #   print result.link

