import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

current_url = "https://www.tops.co.th/th"

options = Options()
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=r'C:/chromedriver/chromedriver.exe')
driver.get(current_url)
search_box = driver.find_element_by_id("search-input")
search_box.send_keys("แสนดีข้าวกล้องหอม 5กก.")
search_box.send_keys(Keys.RETURN);

time.sleep(30) # Wait for render elements
print("Checking product price....")
product_div = driver.find_element_by_xpath("//div[@data-productid = '8851042400059']")
print(product_div.get_attribute("data-productprice"))

driver.quit()