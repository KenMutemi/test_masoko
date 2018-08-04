import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = webdriver.Chrome(executable_path='/opt/chromedriver')
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get("https://www.masoko.com/")
        inst.driver.title

    def test_search(self):
        # get the search field
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("huawei")
        self.search_field.send_keys(Keys.RETURN)

        # get list of returned data (elements)

        returned_data = self.driver.find_element_by_class_name("product-item")
        self.assertGreater(0, len(returned_data))

    @classmethod
    def tearDownClass(inst):
        # close browser instance
        inst.driver.quit()
if __name__ == '__main__':
    unittest.main()
