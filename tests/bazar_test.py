import time

import allure

from pages.elements_page_bazar import ViyarBazarPage, ReviewsBazarPage

@allure.suite("ElementsBazara")
class TestElementsBazara:
	@allure.feature("TestVazarBazar")
	class TestVicarBazaar:

		link = "https://viyarbazar.com/"
		@allure.title("Bazar Register")
		def test_viyar_register(self, driver):
			viyar_page = ViyarBazarPage(driver, self.link)
			viyar_page.open()
			viyar_page.register_on_bazar_viyar()
			viyar_page.viyti_s_akka()
			email_input = viyar_page.avtorizacion()
			viyar_page.after_register_viyar()
			email_output = viyar_page.check_email_in()
			assert email_input == email_output, "Почты разные почему то"

		@allure.title("Bazar Gallery")
		def test_viyar_gallery(self, driver):
			gallery_page = ViyarBazarPage(driver, self.link)
			gallery_page.open()
			gallery_page.avtorizacion()
			gallery_page.click_on_gallery()
			gallery_page.random_sort()
			gallery_page.button_more()
			click_on_portfolio = gallery_page.random_portfolio()
			check_portfolio_maker = gallery_page.check_maker()
			assert check_portfolio_maker == click_on_portfolio, "Что то с порфтолио не так"

		@allure.title("Reviews")
		def test_viyar_reviews(self, driver):
			viyar_page = ReviewsBazarPage(driver, self.link)
			viyar_page.open()
			viyar_page.click_on_button_reviews()
			click_type = viyar_page.open_and_random_filter()
			result_type = viyar_page.check_filter()
			print(click_type, result_type)
			assert click_type == result_type or result_type == True
