##Demo Program Scraping URL's from web pages-- Professor Reed -- Wed. Jan. 29th, 2014
##Modified (12/10/2013) for Python 3.3
##Modified (12/11/2013) for OETC Web page url extraction
##
####requires special install of requests
##==>see: http://docs.python-requests.org/en/latest/user/install/#install for complete details

##Demo03A -- OETC 2014 -- WEB Page Scraping demo 01
##NOW: setup for Python 3.3 (as of Dec. 10th, 2013)
##
##NOTE: run testURLscraper()
##
from bs4 import BeautifulSoup
import requests

def get_my_urls(url): 
    r  = requests.get("http://" +url) 
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))

def testURLscraper():
## uncomment next statement for live input test    
##    url = raw_input("Enter a website to extract the URL's from: ")
    print('OETC 2014 Highlights Web Page:')
    url = 'oetc.ohio.gov/2014ProgramHighlights.aspx'
    get_my_urls(url)
    print('### end of scrapes from OETC 2014 Highlights Web Page ###')
    print('____________________________________________')
    print('OETC 2014 Keynote Speakers Web Page:')
    url = 'oetc.ohio.gov/2014ProgramHighlights/2014KeynoteSpeakers.aspx'
    get_my_urls(url)
    print('### end of scrapes from OETC 2014 Keynote Speakers Web Page ###')
    print('____________________________________________')
    print('____________________________________________')

    print
    print('end of report')
    
    
    


