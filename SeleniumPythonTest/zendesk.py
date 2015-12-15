from selenium                                       import webdriver

from selenium.webdriver.support.ui                  import WebDriverWait

from selenium.webdriver.common.by                   import By

from selenium.webdriver.common.action_chains        import ActionChains

from selenium.webdriver.common.keys                 import Keys

import unittest

import time

class zendesk(unittest.TestCase):

	def setUp(self):
		global driver 
		driver = webdriver.Firefox()
		driver.get("https://www.zendesk.com")
		driver.maximize_window()

	def test_selectOption(self):
		#locators
		innovativeLocator = "a[contains(@href, '/product/innovative-customer-service/')]"
		innovativeElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_tag(innovativeLocator))

		actions = ActionChains(driver)
		action.send_keys_to_element(innovativeElement, Keys.ENTER)
		actions.send_keys(Keys.ARROW_DOWN)
		actions.send_keys(Keys.ARROW_DOWN)
		actions.perform()

		time.sleep(10)

	def tearDown(self):
		driver.quit()

if __name__ == "__main__":
	unittest.main()

