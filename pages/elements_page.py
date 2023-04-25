import random

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
	WebTablePageLocators, ViyarBazarLocators, ModalBazarLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):

	locators = TextBoxPageLocators()

	def fill_all_fields(self):
		person_info = next(generated_person())
		full_name = person_info.full_name
		email = person_info.email
		current_address = person_info.current_address
		permanent_address = person_info.permanent_address
		self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
		self.element_is_visible(self.locators.EMAIL).send_keys(email)
		self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
		self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
		self.element_is_clickable(self.locators.SUBMIT).click()
		return full_name, email,current_address,permanent_address

	def check_filled_form(self):

		full_name = self.element_is_presents(self.locators.CREATED_FULL_NAME).text.split(":")[1]
		email = self.element_is_presents(self.locators.CREATED_EMAIL).text.split(":")[1]
		current_address = self.element_is_presents(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
		permanent_address = self.element_is_presents(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
		return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

	locators = CheckBoxPageLocators()

	def open_full_list(self):
		self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

	def click_random_checkbox(self):
		item_list = self.element_are_visible(self.locators.ITEM_LIST)
		count = 21
		while count != 0:
			item = item_list[random.randint(1, 15)]
			if count > 0:
				self.go_to_element(item)
				item.click()
				count -= 1
			else:
				break

	def get_checked_checkboxes(self):
		checked_list = self.element_are_presents(self.locators.CHECKED_ITEMS)
		data = []
		for box in checked_list:
			title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
			data.append(title_item.text)
		return str(data).replace(" ", "").replace("doc", "").replace(".", "").lower()



	def get_output_result(self):
		result_list = self.element_are_presents(self.locators.OUTPUT_RESULT)
		data = []
		for item in result_list:
			data.append(item.text)
		return str(data).lower().replace(" ", "")


class RadioButtonPage(BasePage):

	locators = RadioButtonPageLocators()

	def click_on_the_radio_button(self, choice):
		choices = {'yes': self.locators.SYES_RADIOBUTTON,
				   'impressive': self.locators.SIMPRESSIVE_RADIOBUTTON,
				   'no': self.locators.SNO_RADIOBUTTON}

		self.element_is_visible(choices[choice]).click()

	def get_output_result(self):
		return self.element_is_presents(self.locators.SOUTPUT_RESULT).text



class WebTablePage(BasePage):

	locators = WebTablePageLocators()

	def add_new_person(self):
		count = 1
		while count != 0:
			person_info = next(generated_person())
			firstname = person_info.first_name
			lastname = person_info.last_name
			email = person_info.email
			age = person_info.age
			salary = person_info.salary
			department = person_info.department
			self.element_is_visible(self.locators.ADD_BUTTON).click()
			self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
			self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
			self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
			self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
			self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
			self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
			self.element_is_visible(self.locators.SUBMIT).click()
			count -= 1
			return [firstname,lastname,str(age),email,str(salary),department]


	def check_new_added_person(self):
		people_list = self.element_are_presents(self.locators.FULL_PEOPLE_LIST)
		data = []
		for item in people_list:
			data.append(item.text.splitlines())
		return data

	#	def search_some_person(self, key_word):
	#		self.element_is_visible(self.locators.s)


class ViyarBazarPage(BasePage):





	locators = ViyarBazarLocators()
	locator = ModalBazarLocators()


	def register_on_bazar_viyar(self):
		password = self.password
		person_info = next(generated_person())
		second_name = person_info.second_name
		first_name = person_info.first_name
		email = person_info.email
		middle_name = person_info.middle_name
		number = person_info.number
		self.element_is_visible(self.locators.BUTTON_YVITI).click()
		self.element_is_visible(self.locators.BUTTON_REGISTER).click()
		self.element_is_visible(self.locators.SECOND_NAME).send_keys(second_name)
		self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
		self.element_is_visible(self.locators.EMAIL).send_keys(email)
		self.element_is_visible(self.locators.MIDDLE_NAME).send_keys(middle_name)
		self.element_is_visible(self.locators.NUMBER).send_keys(number)
		self.element_is_visible(self.locators.PASSWORD).send_keys(password)
		self.element_is_visible(self.locators.CLONE_PASSWORD).send_keys(password)
		#self.element_is_visible(self.locators.VIRDEL).click()
		self.element_is_visible(self.locators.VIRDEL_ZAMOVNIK).click()
		#self.element_is_visible(self.locators.VIRDEL_ZAMOVNIK).send_keys(Keys.ESCAPE)
		self.element_is_visible(self.locators.CHECK_BOX).click()
		self.element_is_visible(self.locators.SUBMIT_REGISTER).click()
		self.data = email
		print(email)
		return second_name,first_name,email,middle_name,number

	def after_register_viyar(self):

		all_oblasti = self.element_are_presents(self.locator.ALL_OBLAST)
		print(all_oblasti.text)


	def viyti_s_akka(self):
		self.element_is_visible(self.locator.CLOSE_MODAL).click()
		self.element_is_visible(self.locator.TRI_TOCHKI).click()
		self.element_is_visible(self.locator.VIHOD_CHEREZ_TRI).click()

	def avtorizacion(self):
		email = self.email
		password = "alona007"
		self.element_is_visible(self.locators.BUTTON_YVITI).click()
		self.element_is_visible(self.locator.INPUT_EMAIL).send_keys(email)                #self.data
		self.element_is_visible(self.locator.INPUT_PASSWORD).send_keys(password)
		self.element_is_visible(self.locator.YVITI_KEKLOK).click()









