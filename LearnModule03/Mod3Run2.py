## Professor Reed demos astronomy data scraped from worldclock page!
##import urllib2 #For Python 2.7
##IMPORTANT -- Setup for Python 3.3!!!
##
##NOTE: run testSunrises()
##
## Suggested Classroom Project:
## Run Sunrise Scraper
## copy data to notepad
## copy notepad data to Excel or other Spreadsheet
## align fix columns
## create mini-report on the next seven days of sunrises in your area
##
## Challenge: write data out as csv file type and directly import into Excel!
####
##
import urllib.request

#   #from BeautifulSoup import BeautifulSoup #obsoleted
# or if you're using BeautifulSoup4:
from bs4 import BeautifulSoup

##url = BeautifulSoup(urllib2.urlopen('http://www.timeanddate.com/worldclock/astronomy.html?n=78').read())
url = BeautifulSoup(urllib.request.urlopen('http://www.timeanddate.com/worldclock/astronomy.html?n=77').read())
def get_and_print_sunrise_times(url):
    print('Date and Time of Sunrise')
    for row in url('table', {'class': 'spad'})[0].tbody('tr'):
        tds = row('td')
        print (tds[0].string, tds[1].string)
        # will print date and sunrise

##Test Driver function follows:
def testSunrises():
    get_and_print_sunrise_times(url)
    
