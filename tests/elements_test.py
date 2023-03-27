import time

from pages.elements_page import TextBoxPage

class TestElements:
	class TestTextBox:

		def test_text_box(self, driver):
			test_text_box = TextBoxPage(driver, "https://demoqa.com/text-box")
			test_text_box.open()
			test_text_box.fill_all_fields()
			time.sleep(5)
