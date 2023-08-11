import random
import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.slider_page_locators import SlidePageLocators, ProgressBarPageLocators
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
	TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, SelectMenuPageLocators
from pagesbazar.base_page import BasePage


class AccordianPage(BasePage):
	locators = AccordianPageLocators()

	def check_accordian(self, accordian_num):
		accordian = {'first':
						 {'title': self.locators.SECTION_FIRST,
						  'content': self.locators.SECTION_CONTENT_FIRST},
					 'second':
						 {'title': self.locators.SECTION_SECOND,
						  'content': self.locators.SECTION_CONTENT_SECOND},
					 'third':
						 {'title': self.locators.SECTION_THIRD,
						  'content': self.locators.SECTION_CONTENT_THIRD},
					 }

		section_title = self.element_is_visible(accordian[accordian_num]['title'])
		section_title.click()
		try:
			section_content = self.element_is_visible(accordian[accordian_num]['content']).text
		except TimeoutException:
			section_title.click()
			section_content = self.element_is_visible(accordian[accordian_num]['content']).text
		return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
	locators = AutoCompletePageLocators()

	def fill_input_multi(self):
		colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
		for color in colors:
			input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
			input_multi.send_keys(color)
			input_multi.send_keys(Keys.ENTER)
		return colors

	def remove_value_from_multi(self):
		count_value_before = len(self.element_are_presents(self.locators.MULTI_VALUE))
		remove_button_list = self.element_are_visible(self.locators.MULTI_VALUE_REMOVE)
		for value in remove_button_list:
			value.click()
			break
		count_value_after = len(self.element_are_presents(self.locators.MULTI_VALUE))
		return count_value_before, count_value_after

	def check_color_in_multi(self):
		color_list = self.element_are_presents(self.locators.MULTI_VALUE)
		colors = []
		for color in color_list:
			colors.append(color.text)
		return colors

	def fill_input_single(self):
		color = random.sample(next(generated_color()).color_name, k=1)
		input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
		input_single.send_keys(color)
		input_single.send_keys(Keys.ENTER)
		return color

	def check_color_in_single(self):
		color = self.element_is_visible(self.locators.SINGLE_VALUE)
		return [color.text]


class DatePickerPage(BasePage):
	locators = DatePickerPageLocators()

	def select_date(self):
		date = next(generated_date())
		input_date = self.element_is_visible(self.locators.DATE_INPUT)
		value_data_before = input_date.get_attribute('value')
		input_date.click()
		self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
		self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
		self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
		value_date_after = input_date.get_attribute('value')
		return value_data_before, value_date_after

	def select_date_and_time(self):
		date = next(generated_date())
		input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
		value_date_before = input_date.get_attribute('value')
		input_date.click()
		self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
		self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
		self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
		self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
		self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
		self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
		input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
		value_date_after = input_date_after.get_attribute('value')
		return value_date_before, value_date_after

	def set_date_by_text(self, element, value):
		select = Select(self.element_is_presents(element))
		select.select_by_visible_text(value)

	def set_date_item_from_list(self, elements, value):
		item_list = self.element_are_presents(elements)
		for item in item_list:
			if item.text == value:
				item.click()
				break


class SliderPage(BasePage):
	locators = SlidePageLocators()

	def change_slider_value(self):
		value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
		slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
		self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
		value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
		return value_before, value_after


class ProgressBarPage(BasePage):
	locators = ProgressBarPageLocators()

	def change_progress_bar_value(self):
		progress_bar = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
		progress_bar.click()
		value_before = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
		time.sleep(random.randint(1, 8))
		progress_bar.click()
		value_after = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
		return value_before, value_after

	def change_progress_bar_value_100(self):
		progress_bar = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
		progress_bar.click()
		value_before = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
		self.check_progress_bar()
		value_after = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
		return value_before, value_after

	def check_progress_bar(self):

		try:
			value_succsess = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE_SUCCSESS).text
			if value_succsess == "100%":
				progress_bar_reset = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON_RESET)
				progress_bar_reset.click()
			else:
				time.sleep(1)  # Задержка выполнения на 1 секунду
				self.check_progress_bar()  # Рекурсивный вызов функции

		except TimeoutException:
			self.check_progress_bar()


class TabsPage(BasePage):
	locators = TabsPageLocators()

	def check_tabs(self):
		what_button = self.element_is_visible(self.locators.TABS_WHAT)
		origin_button = self.element_is_visible(self.locators.TABS_ORIGIN)
		use_button = self.element_is_visible(self.locators.TABS_USE)
		more_button = self.element_is_visible(self.locators.TABS_MORE)
		what_button.click()
		what_content = self.element_is_visible(self.locators.TABS_WHAT_CONTENT).text
		origin_button.click()
		origin_content = self.element_is_visible(self.locators.TABS_ORIGIN_CONTENT).text
		use_button.click()
		use_content = self.element_is_visible(self.locators.TABS_USE_CONTENT).text
		try:
			more_button.click()
			more_content = self.element_is_visible(self.locators.TABS_MORE_CONTENT).text
		except ElementClickInterceptedException:
			print('lol')
		return len(what_content), len(origin_content), len(use_content)

class ToolTipsPage(BasePage):
	locators = ToolTipsPageLocators()

	def tool_tips(self):
		elements_text = []
		self.element_is_visible(self.locators.BUTTON).click()
		hint_button = self.element_is_visible(self.locators.TOOL_TIP_BUTTON).text
		elements_text += [hint_button]
		self.element_is_visible(self.locators.FIELD).click()
		hint_field = self.element_is_visible(self.locators.TOOL_TIP_FIELD).text
		elements_text += [hint_field]
		self.element_is_visible(self.locators.CONTRTARY_LINK).click()
		hint_link = self.element_is_visible(self.locators.TOOL_TIP_CONTRARY).text
		elements_text += [hint_link]
		self.scroll_page("200")
		self.element_is_visible(self.locators.SECTION_LINK).click()
		hint_section = self.element_is_visible(self.locators.TOOL_TIP_SECTION).text
		elements_text += [hint_section]
		print(elements_text)

	def get_text_fro_tool_tips(self, hover_element, wait_elem):
		element = self.element_is_presents(hover_element)
		self.move_to_element(element)
		self.element_is_visible(wait_elem)
		tool_tip_text = self.element_is_visible(self.locators.ALL_TOOL_TIPS)
		text = tool_tip_text.text
		return text

	def check_tool_tips(self):
		self.scroll_page("200")
		tool_tip_text_button = self.get_text_fro_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
		time.sleep(2)
		tool_tip_text_field = self.get_text_fro_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
		time.sleep(2)
		tool_tip_text_contrary = self.get_text_fro_tool_tips(self.locators.CONTRTARY_LINK, self.locators.TOOL_TIP_CONTRARY)
		time.sleep(2)
		tool_tip_text_selection = self.get_text_fro_tool_tips(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
		time.sleep(2)
		return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_selection

class MenuPage(BasePage):
	locators = MenuPageLocators()


	def check_menu(self):
		menu_item_list = self.element_are_presents(self.locators.ALL_ITEMS)
		data = []
		for item in menu_item_list:
			self.move_to_element(item)
			data.append(item.text)
		return data

class SelectMenuPage(BasePage):
	locators = SelectMenuPageLocators()

	def first_input(self):
		data_for_first = f"Group {random.randint(1,2)}, option {random.randint(1,2)}"
		first_input = self.element_is_clickable(self.locators.SELECT_VALUE)
		first_input.click()
		select_input = self.element_is_visible(self.locators.INPUT_VALUE)
		select_input.send_keys(data_for_first)
		select_input.send_keys(Keys.ENTER)
		data = self.element_is_visible(self.locators.OUTPUT_VALUE).text
		return [data], [data_for_first]

	def second_input(self):
		data = ["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Other"]
		random_data = random.choice(data)
		second_input = self.element_is_clickable(self.locators.SELECT_ONE)
		second_input.click()
		select_input = self.element_is_visible(self.locators.SELECT_ONE_INPUT)
		select_input.send_keys(random_data)
		select_input.send_keys(Keys.ENTER)
		output_data = self.element_is_visible(self.locators.OUTPUT_ONE).text
		return output_data, random_data

	def third_input(self):
		randomp = random.randint(0, 10)
		multi_select = self.element_is_clickable(self.locators.OLD_STYLE_MENU)
		multi_select.click()
		all_multi_select = self.element_are_presents(self.locators.ALL_LIST)
		random_select = all_multi_select[randomp]
		random_select.click()
		return random_select.text

	def fourth_input(self):
		data = ["Black","Green","Blue","Red",]
		self.scroll_page(200)
		old_style_input = self.element_is_clickable(self.locators.MULTI_SELECT_DROP)
		old_style_input.click()
		for i in data:
			input = self.element_is_presents(self.locators.INPUT_MULTI)
			input.send_keys(i)
			input.send_keys(Keys.ENTER)
		delete_button = self.element_is_presents(self.locators.DELETE_MULTI_SELECT)
		delete_button.click()
		time.sleep(3)
		result = self.element_are_presents(self.locators.RESULT_MULTI)
		return result

	def five_multi_select(self):
		first_element = self.element_is_visible(self.locators.STANDART_MULTI_SELECT)
		self.action_drag_and_drop_by_offset(first_element, 0, 50)




















