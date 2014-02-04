##Demo Program Scraping URL's from web pages-- Professor Reed -- Monday Dec. 9th, 2013
##Python 3.3
from bs4 import BeautifulSoup
import requests


def get_my_urls(url): 
    r  = requests.get("http://" +url) 
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))

def testURLscraping():
## uncomment next statement for live input test    
##    url = raw_input("Enter a website to extract the URL's from: ")
    print('OETC 2014 Home Site:')
    url = 'oetc.ohio.gov'
    get_my_urls(url)
    print("______________end of my first url set________")
    print('Yahoo S&P:')
    url = 'finance.yahoo.com/q?s=^gspc'
    get_my_urls(url)
    print("______________end of my second url set________")
    


