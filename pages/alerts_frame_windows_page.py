from locators.alerts_frame_windwos_locators import BrowserWindowsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
	locators = BrowserWindowsLocators()

	def check_opened_new_tab(self, page):
		if page.upper() == "TAB":
			self.element_is_visible(self.locators.BUTTON_NEW_TAB).click()
			self.switch_tab(1)
			text_title = self.element_is_presents(self.locators.CHECKED_NEW_TAB).text
			self.switch_tab(0)
			return text_title
		elif page.upper() == "WINDOW":
			self.element_is_visible(self.locators.BUTTON_NEW_WINDOW).click()
			self.switch_tab(1)  #self.driver.switch_to.window(self.driver.window_handles[1])
			text_title = self.element_is_presents(self.locators.CHECKED_NEW_TAB).text
			self.switch_tab(0)
			return text_title



