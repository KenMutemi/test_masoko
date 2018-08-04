from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/opt/chromedriver')
driver.get("https://www.masoko.com/customer/account/login/")
elem_username = driver.find_element_by_name("login[username]")
elem_password = driver.find_element_by_name("login[password]")
elem_username.clear()
elem_password.clear()
elem_username.send_keys("mutemikennedy@gmail.com")
elem_password.send_keys("Frost10012#")
elem_password.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close
