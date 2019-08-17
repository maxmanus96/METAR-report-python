from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

#import urllib2
from bs4 import BeautifulSoup
from urllib.request import urlopen

airport=['EPWA','EPKK']
city=airport[0]
url='https://www.aviationweather.gov/metar/data?ids='+city+'&format=raw&date=0&hours=0'

page = urlopen(url)
soup = BeautifulSoup(page,'html.parser')
metar=soup.find(city)
print (metar)

#x = soup.body.find('div', attrs={'class' : 'container'}).text

