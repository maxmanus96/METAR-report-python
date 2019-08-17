from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#chrome

#browser = webdriver.Chrome()
#webdriver.Chrome().get('http://www.metarreader.com/)
#browser.implicitly_wait(10)

airport=['EPWA','EPKK']
city=airport[0]
url='https://www.aviationweather.gov/metar/data?ids='+city+'&format=raw&date=0&hours=0'
#city = input('City Name :')

url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['base']

#login = browser.find_element_by_id('username_input')
#button=browser.find_element_by_class_name('submit')
#login.send_keys('blablabla')


login = browser.find_element_by_id('metar')
city=str(input("Enter the name of the city you want the METAR for :"))
login.send_keys(city)
button = browser.find_element_by_id('getmetar')
button.click()
metar = browser.find_element_by_id('convert')
print(metar)
#driver.get("https://www.wearher-forecast.com/locations/"+city+"/forecasts/latest")

#print(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
