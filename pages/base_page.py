from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

	def __init__(self, driver, url):
		self.email = "brookskeith@example.com"
		self.password = "alona007"
		self.driver = driver
		self.url = url
		self.random_email = None

	def open(self):
		self.driver.get(self.url)

	def element_is_visible(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

	def element_are_visible(self, locator, timeout=5):
		self.go_to_element(self.element_is_presents(locator))
		return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

	def element_is_presents(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

	def element_are_presents(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

	def element_is_not_visible(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

	def element_is_clickable(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

	def go_to_element(self, element):
		self.driver.execute_script("arguments[0].scrollIntoView;", element)

	def scroll_page(self, pixels):
		self.driver.execute_script(f"window.scrollBy(0, {pixels});")

	def action_double_click(self, element):
		action = ActionChains(self.driver)
		action.double_click(element)
		action.perform()

	def action_right_click(self, element):
		action = ActionChains(self.driver)
		action.context_click(element)
		action.perform()

	def element_to_remove(self, element):
		self.driver.execute_script("arguments[0].remove();", element)

	def window_zoom(self):
		window = self.driver.execute_script("return window")
		window.document.body.style.zoom = "75%"

	def move_to_element(self, element):
		action = ActionChains(self.driver)
		action.move_to_element(element)
		action.perform()

	def remove_footer(self):
		self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
		self.driver.execute_script("document.getElementsById('close-fixedban').remove();")

	def switch_tab(self,number):
		self.driver.switch_to.window(self.driver.window_handles[number])


# def switch_to_tab(self):
