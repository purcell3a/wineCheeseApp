import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import csv

DRIVER_PATH = '/Users/mouse/src/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')

# Optional argument, if not specified will search path.
# instantiated object Options
# options = Options()ls
# options.headless = True
# options.add_argument('--window-size=1920,1200')
# driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)

# driver.get('https://www.gourmetsleuth.com/features/wine-cheese-pairing-guide')



