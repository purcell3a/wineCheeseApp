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
driver.get("https://www.gourmetsleuth.com/features/wine-cheese-pairing-guide")
print ("###########################  Begin Scraping ########################### ")
print ("###########################  Page URL ########################### ")
# print(driver.current_url) #to get the current url (can be useful when there are redirections on the website and that you need the final URL)
print ("###########################  Page Title ########################### ")
# print(driver.title) #to get the page's title
print ("###########################  Page Source ########################### ")
# print(driver.page_source)   #will return and print the full page HTML code in terminal
print ("###########################  END Scraping ########################### ")
# driver.quit()

# scraping cheese names
cheese_el = driver.find_elements_by_class_name('item-1')
cheese_rows = []
for cheese in cheese_el:
    cheeset = cheese.text
    ncheese = cheeset.replace('\n', '')
    cheese_rows.append([ncheese])

# scraping wine names
wine_el = driver.find_elements_by_class_name('wines')
spans = []
spans_set = set()
for wine in wine_el:
    spans.append(wine.find_element_by_tag_name('span'))

for span in spans:
    spans_set.add(span.text)

print(spans_set)# writing wine to csv
with open('wine.csv', mode='w') as file:
    wine_writer = csv.writer(
        file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for wine in spans_set:
        wine_writer.writerow([wine])

# writing cheese to csv
with open('cheese.csv', mode='w') as file:
    cheese_writer = csv.writer(
        file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for cheese in cheese_rows:
        cheese_writer.writerow(cheese)

# writing wine to csv
with open('wine.csv', mode='w') as file:
    wine_writer = csv.writer(
        file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for wine in wine_rows:
        wine_writer.writerow([wine])