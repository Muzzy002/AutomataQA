import random
import time

from locators.alerts_frame_windwos_locators import BrowserWindowsLocators, AlertsPageLocators, FramesPageLocators, \
	NestedFramesPageLocators, ModalDialogPageLocators
from pagesbazar.base_page import BasePage


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
			self.switch_tab(1)  # self.driver.switch_to.window(self.driver.window_handles[1])
			text_title = self.element_is_presents(self.locators.CHECKED_NEW_TAB).text
			self.switch_tab(0)
			return text_title


class AlertsPage(BasePage):
	locators = AlertsPageLocators()

	def check_see_alert(self):
		self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
		alert_window = self.switch_to_alert()  # self.driver.switch_to.alert
		return alert_window.text

	def check_alert_appear_5_sec(self):
		self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
		time.sleep(5)
		alert_window = self.switch_to_alert()  # self.driver.switch_to.alert
		return alert_window.text

	def check_confirm_alert(self):
		self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
		alert_window = self.driver.switch_to.alert
		alert_window.accept()
		text_result = self.element_is_presents(self.locators.CONFIRM_RESULT).text
		return text_result

	def check_promt_alert(self):
		text = f"Autotest{random.randint(0, 999)}"
		self.element_is_visible(self.locators.PROMT_BOX_ALERT_BUTTON).click()
		alert_window = self.driver.switch_to.alert
		alert_window.send_keys(text)
		alert_window.accept()
		text_result = self.element_is_presents(self.locators.PROMT_RESULT).text
		return text, text_result


class FramesPage(BasePage):
	locators = FramesPageLocators()

	def check_frame(self, frame_num):
		if frame_num == 'frame1':
			frame = self.element_is_presents(self.locators.FIRST_FRAME)
			width = frame.get_attribute('width')
			height = frame.get_attribute('height')
			self.switch_to_frame(frame)
			text = self.element_is_presents(self.locators.TITLE_FRAME).text
			self.switch_to_default_content()
			return [text, width, height]
		if frame_num == 'frame2':
			frame = self.element_is_presents(self.locators.SECOND_FRAME)
			width = frame.get_attribute('width')
			height = frame.get_attribute('height')
			self.switch_to_frame(frame)
			text = self.element_is_presents(self.locators.TITLE_FRAME).text
			self.switch_to_default_content()
			return [text, width, height]


class NestedFramesPage(BasePage):
	locators = NestedFramesPageLocators()

	def check_nested_frame(self):
		parent_frame = self.element_is_presents(self.locators.PARENT_FRAME)
		self.switch_to_frame(parent_frame)
		parent_text = self.element_is_presents(self.locators.PARENT_TEXT).text
		child_frame = self.element_is_presents(self.locators.CHILD_FRAME)
		self.switch_to_frame(child_frame)
		child_text = self.element_is_presents(self.locators.CHILD_TEXT).text
		return parent_text, child_text


class ModalDialogPage(BasePage):

	locators = ModalDialogPageLocators()

	def check_modal_dialogs(self):
		self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
		title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
		body_small_text = self.element_is_visible(self.locators.BODY_SMALL).text
		self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
		self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
		title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
		body_large_text = self.element_is_visible(self.locators.BODY_LARGE).text
		return [title_small, len(body_small_text)], [title_large, len(body_large_text)]


