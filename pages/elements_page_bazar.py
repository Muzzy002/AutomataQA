import random
import time

import requests

from generator.generator import generated_person
from locators.elements_locators_bazara import ViyarBazarLocators, ModalBazarLocators, GalleryBazar, ButtonHelp
from pages.base_page import BasePage


class ViyarBazarPage(BasePage):
	viyarbazarlocators = ViyarBazarLocators()
	modalbazarlocators = ModalBazarLocators()
	gallerybazarlocators = GalleryBazar()
	buttonhelphref = ButtonHelp()

	def register_on_bazar_viyar(self):
		password = self.password
		person_info = next(generated_person())
		second_name = person_info.second_name
		first_name = person_info.first_name
		email = person_info.email
		middle_name = person_info.middle_name
		number = person_info.number
		self.element_is_visible(self.viyarbazarlocators.BUTTON_YVITI).click()
		self.element_is_visible(self.viyarbazarlocators.BUTTON_REGISTER).click()
		self.element_is_visible(self.viyarbazarlocators.SECOND_NAME).send_keys(second_name)
		self.element_is_visible(self.viyarbazarlocators.FIRST_NAME).send_keys(first_name)
		self.element_is_visible(self.viyarbazarlocators.EMAIL).send_keys(email)
		self.element_is_visible(self.viyarbazarlocators.MIDDLE_NAME).send_keys(middle_name)
		self.element_is_visible(self.viyarbazarlocators.NUMBER).send_keys(number)
		self.element_is_visible(self.viyarbazarlocators.PASSWORD).send_keys(password)
		self.element_is_visible(self.viyarbazarlocators.CLONE_PASSWORD).send_keys(password)
		self.element_is_visible(self.viyarbazarlocators.VIRDEL_ZAMOVNIK).click()
		self.element_is_visible(self.viyarbazarlocators.CHECK_BOX).click()
		self.element_is_visible(self.viyarbazarlocators.SUBMIT_REGISTER).click()
		self.random_email = email
		print(email)
		return second_name, first_name, email, middle_name, number

	def after_register_viyar(self):
		all_oblasti = self.element_are_visible(self.modalbazarlocators.ALL_OBLAST)
		count = 1
		while count != 0:
			item = all_oblasti[random.randint(1, 24)]
			if count > 0:
				self.go_to_element(item)
				item.click()
				count -= 1
			else:
				continue
		all_goroda = self.element_are_visible(self.modalbazarlocators.ALL_CITYES)
		count = 1
		while count != 0:
			item = all_goroda[random.randint(1, 7)]
			if count > 0:
				self.go_to_element(item)
				self.element_is_clickable(item).click()
				count -= 1
			else:
				continue

		button_accept = self.element_is_presents(self.modalbazarlocators.ACCEPT_MODAL)
		button_close = self.element_are_presents(self.modalbazarlocators.CLOSE_MODAL_SKAS)
		if button_accept.is_displayed():
			button_accept.click()
		else:
			button_close.click()

	def viyti_s_akka(self):
		self.element_is_visible(self.modalbazarlocators.CLOSE_MODAL).click()
		self.element_is_visible(self.modalbazarlocators.TRI_TOCHKI).click()
		self.element_is_visible(self.modalbazarlocators.VIHOD_CHEREZ_TRI).click()

	def avtorizacion(self):
		email_cons = self.email
		email = self.random_email
		password = self.password
		self.element_is_visible(self.viyarbazarlocators.BUTTON_YVITI).click()
		if email == None:
			self.element_is_visible(self.modalbazarlocators.INPUT_EMAIL).send_keys(email_cons)
			email = email_cons
		else:
			self.element_is_visible(self.modalbazarlocators.INPUT_EMAIL).send_keys(email)
		self.element_is_visible(self.modalbazarlocators.INPUT_PASSWORD).send_keys(password)
		self.element_is_visible(self.modalbazarlocators.YVITI_KEKLOK).click()
		return email

	def check_email_in(self):
		return self.element_is_presents(self.modalbazarlocators.CHECK_POSHTA).text

	def check_maker(self):
		data = []
		maker = self.element_is_visible(self.gallerybazarlocators.CHECK_MAKER).text
		data.append(maker)
		return data

	def click_on_gallery(self):
		self.element_is_visible(self.gallerybazarlocators.BUTTON_GALLERY_ON_HOME).click()

	def random_sort(self):
		all_sort = self.element_are_visible(self.gallerybazarlocators.ALL_SORT_GALLERY)
		count = 1
		while count != 0:
			item = all_sort[random.randint(1, 12)]
			if count > 0:
				self.go_to_element(item)
				item.click()
				count -= 1
			else:
				break

	def button_more(self):
		time.sleep(10)
		self.scroll_page(500)
		item = self.element_is_presents(self.gallerybazarlocators.DOWNLOAD_MORE)
		count = 1
		while count != 0:
			self.go_to_element(item)
			if count > 0:
				if item.is_displayed():
					item.click()
					count -= 1
				else:
					return item

	def random_portfolio(self):
		all_kartochki = self.element_are_visible(self.gallerybazarlocators.ALL_KARTOCHKI_PORTF)
		data = []
		count = 1
		while count != 0:
			item = all_kartochki[random.randint(0, len(all_kartochki) - 1)]
			for_data = item.text
			data.append(for_data.split('\n')[0])
			self.go_to_element(item)
			item.click()
			count -= 1
		return data

# def check_vnytri_portdolio(self):
