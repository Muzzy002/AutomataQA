import random
import time
import allure
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
	UploadAndDownloadPage, DynamicPropertiesPage, FFormPage

@allure.suite("Elements")
class TestElements:
	@allure.feature("TextBox")
	class TestTextBox:

		@allure.title("Check TextBox")

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

	@allure.feature("TextBox1")
	class TestCheckBox:
		@allure.title("Check CheckBox2")
		def test_check_box(self, driver):
			check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
			check_box_page.open()
			check_box_page.open_full_list()
			check_box_page.click_random_checkbox()
			input_checkbox = check_box_page.get_checked_checkboxes()
			output_result = check_box_page.get_output_result()
			assert input_checkbox == output_result, "Тест по чек боксам не прошел"

	@allure.feature("TextBox3")
	class TestRadioButton:
		@allure.title("Check RadioButton4")

		def test_radio_button(self, driver):
			radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
			radio_button_page.open()
			radio_button_page.click_on_the_radio_button("yes")
			output_yes = radio_button_page.get_output_result()
			radio_button_page.click_on_the_radio_button("impressive")
			output_impressive = radio_button_page.get_output_result()
			radio_button_page.click_on_the_radio_button("no")
			output_no = radio_button_page.get_output_result()
			assert output_yes == "Yes", "'Yes' have no been selected"
			assert output_impressive == "Impressive", "'Impressive' have no been selected"
			assert output_no == "No", "'No' have no been selected"

	@allure.feature("TextBo12x")
	class TestWebTable:
		@allure.title("Check Web12Table")

		def test_web_table_add_person(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			new_person = web_table_page.add_new_person()
			table_result = web_table_page.check_new_added_person()
			assert new_person in table_result, "ABRAKADABRA"

		@allure.title("Che123ck FormPage")
		def test_web_table_search_person(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			key_word = web_table_page.add_new_person()[random.randint(0, 5)]
			web_table_page.search_some_person(key_word)
			table_result = web_table_page.check_search_person()
			print(key_word, table_result)
			assert key_word in table_result

		@allure.title("Che44ck FormPage")
		def test_web_table_person_info(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			lastname = web_table_page.add_new_person()[1]
			web_table_page.search_some_person(lastname)
			age = web_table_page.update_person_info()
			row = web_table_page.check_search_person()
			assert age in row, "person card has not been changed"

		@allure.title("Check Fo55rmPage")
		def test_web_table_dalete_person(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			email = web_table_page.add_new_person()[3]
			web_table_page.search_some_person(email)
			web_table_page.delete_person()
			text = web_table_page.check_deleted()
			assert text == "No rows found"

		@allure.title("Check For112mPage")
		def test_web_table_change_count_row(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			count = web_table_page.select_up_to_some_rows()
			assert count == [5, 10, 20, 25, 50, 100], "Все гуд только на сайте баг"

	@allure.feature("TextB33ox")
	class TestButtonPage:
		@allure.title("Chec232k ButtonPage")
		def test_different_click_on_the_buttons(self, driver):
			button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
			button_page.open()
			button_page.random_click_on_different_button()
			time.sleep(5)

	@allure.feature("Text234Box")
	class TestLinkPage:
		@allure.title("4Chec5k LinkPage")
		def test_check_link(self, driver):
			links_page = LinksPage(driver, 'https://demoqa.com/links')
			links_page.open()
			href_link, current_url = links_page.check_new_tab_simple_link()
			assert href_link == current_url, "the link is broken or url is incorrect"

		@allure.title("Ch34eck FormPage")
		def test_broken_link(self, driver):
			links_page = LinksPage(driver, "https://demoqa.com/links")
			links_page.open()
			response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
			assert response_code == 400, 'test_broken_link наебнулся'

	@allure.feature("T34extBox")
	class TestUploadANDDownload:
		@allure.title("Check UploadANDDownload")
		def test_upload_file(self, driver):
			upload_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
			upload_page.open()
			file_name, result = upload_page.update_file()
			assert file_name == result

		@allure.title("Check FormffPage")
		def test_download_file(self, driver):
			upload_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
			upload_page.open()
			check = upload_page.download_file()
			assert check is True

	@allure.feature("TexcstBox")
	class TestDynamicPropertiesPage:

		@allure.title("Check DysdcnamicPropertiesPage")
		def test_dynamic_properties(self, driver):
			dynamic_proprties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
			dynamic_proprties_page.open()
			color_before, color_after = dynamic_proprties_page.check_changed_of_color()
			assert color_after != color_before, "Цвета не поменялись"

		@allure.title("Chsdceck FormPage")
		def test_appear_button(self, driver):
			dynamic_proprties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
			dynamic_proprties_page.open()
			appear = dynamic_proprties_page.check_appear_of_button()
			assert appear is True, "кнопка не появилась через 5 сек"

		@allure.title("Check FovdfrmPage")
		def test_enable_button(self, driver):
			dynamic_proprties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
			dynamic_proprties_page.open()
			enable = dynamic_proprties_page.check_enable_button()
			assert enable is True, "Кнопка не стала доступной через 5 секнуд"

	@allure.feature("TeerxtBox")
	class TestFormPage:
		@allure.title("Chefdvck FormPage")
		def test_delete_baner(self, driver):
			dyenamic_proprties_page = FFormPage(driver, "https://demoqa.com/automation-practice-form")
			dyenamic_proprties_page.open()
			dyenamic_proprties_page.delete_reklama()
			dyenamic_proprties_page.window_zoom()
			time.sleep(10)
