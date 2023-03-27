import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
	locators = TextBoxPageLocators()

	def fill_all_fields(self):
		self.element_are_visible(self.locators.FULL_NAME).send_keys("asdasd")
		self.element_are_visible(self.locators.EMAIL).send_keys("asdasd.com")
		self.element_are_visible(self.locators.CURRENT_ADDRESS).send_keys("da")
		self.element_are_visible(self.locators.PERMANENT_ADDRESS).send_keys("da")
		self.element_are_visible(self.locators.SUBMIT).click()


