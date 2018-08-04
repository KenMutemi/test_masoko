from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/opt/chromedriver')
driver.get("https://www.masoko.com/customer/account/create/")
elem_firstname = driver.find_element_by_name("firstname")
elem_lastname = driver.find_element_by_name("lastname")
elem_mobile = driver.find_element_by_name("mobile")
elem_email = driver.find_element_by_name("email")
elem_password = driver.find_element_by_name("password")
elem_password_confirmation = driver.find_element_by_name("password_confirmation"
                                                         )
elem_firstname = driver.find_element_by_name("firstname")
elem_firstname.send_keys("Kennedy")
elem_lastname.send_keys("Mutemi")
elem_mobile.send_keys("727011159")
elem_email.send_keys("mutemikennedy@gmail.com")
elem_password.send_keys("Frost10012#")
elem_password_confirmation.send_keys("Frost10012#")
elem_email.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close
