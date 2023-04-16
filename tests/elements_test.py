import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
	class TestTextBox:

		def test_text_box(self, driver):
			test_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
			test_box_page.open()
			full_name, email, current_address, permanent_address = test_box_page.fill_all_fields()
			output_full_name, output_email, output_current_address, output_permanent_address = test_box_page.check_filled_form()


			for i in full_name, email, current_address, permanent_address:
				print('\n' + i)


			assert full_name == output_full_name, "NAME FAILED"
			assert email == output_email, "EMAIL FAILED"
			assert current_address == output_current_address, "CUR ADR FAILED"
			assert permanent_address == output_permanent_address, "PER ADR FAILED"

	class TestCheckBox:
		def test_check_box(self,driver):
			check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
			check_box_page.open()
			check_box_page.open_full_list()
			check_box_page.click_random_checkbox()
			input_checkbox = check_box_page.get_checked_checkboxes()
			output_result = check_box_page.get_output_result()
			assert input_checkbox == output_result, "Тест по чек боксам не прошел"

	class TestRadioButton:
		def test_radio_button(self, driver):
			radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
			radio_button_page.open()
			radio_button_page.click_on_check()
			time.sleep(5)





