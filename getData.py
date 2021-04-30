
# Selenium using Chrome WebDriver to get the HTML table of weather data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

url = "https://mars.nasa.gov/msl/weather/"
options = Options() #instantiating browser options
options.headless = True #browser does not open when run
browser = webdriver.Chrome(options = options, executable_path="chromedriver.exe")
browser.implicitly_wait(10) #wait for data to populate table on site
browser.get(url)
html = browser.page_source #grabs all HTML data from the page
browser.close()
try:
    with open('mars_weather.html', 'w') as f:
        f.write(html)
    print("file was written")
except:
    print("error writing to file")
