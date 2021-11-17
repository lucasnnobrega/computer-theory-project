import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
#options.add_argument("--disable-gpu")
options.add_argument("--window-size=800,600")
options.add_argument("--disable-dev-shm-usage")
#options.set_headless()

driver = webdriver.Chrome('./chromedriver', options=options)  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()