import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re

current_url = "https://www.bigc.co.th"

options = Options()
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=r'C:/chromedriver/chromedriver.exe')
driver.get(current_url)
time.sleep(30) # Wait for render elements
search_box = driver.find_element_by_id("search-id")
search_box.send_keys("แสนดีข้าวกล้องหอม 5กก.")
search_box.send_keys(Keys.RETURN);

time.sleep(30) # Wait for render elements
print("Checking product price....")
product_p = driver.find_element_by_xpath("//div[@class='product-data']/p[@class='product-name' and normalize-space(text())='แสนดี ข้าวกล้องหอมมะลิ 5 กก.']/following-sibling::div/p[@class='promotion']")
price = product_p.get_attribute('textContent')

price = re.sub(r'ถุง','',re.sub(r'([\s|฿|\/])', '', price))
print(price)

driver.quit()