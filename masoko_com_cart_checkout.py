import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/opt/chromedriver')
driver.get("https://www.masoko.com/all-categories/")
driver.find_element_by_css_selector("#product-addtocart-button").click()
driver.get("https://www.masoko.com/checkout/")
driver.close
