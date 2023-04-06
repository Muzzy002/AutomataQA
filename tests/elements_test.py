import time

from pages.elements_page import TextBoxPage

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




