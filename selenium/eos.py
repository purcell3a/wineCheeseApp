from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

DRIVER_PATH = '/Users/mouse/src/chromedriver' #local machine unzipped chrome driver path
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://google.com')

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://eosfitness.com/location/los-angeles-downtown-la-cesar-chavez/")
print ("###########################  Begin Scraping ########################### ")
main = driver.find_elements_by_class_name('site-header__main')
print ("###########################  Page URL ########################### ")
# print(driver.current_url) #to get the current url (can be useful when there are redirections on the website and that you need the final URL)
print ("###########################  Page Title ########################### ")
# print(driver.title) #to get the page's title
print ("###########################  Page Source ########################### ")
# print(driver.page_source)   #will return and print the full page HTML code in terminal
print ("###########################  END Scraping ########################### ")
# driver.quit()

