import time

from pages.elements_page_bazar import ViyarBazarPage

class TestElementsBazara:

	class TestVicarBazaar:

		def test_viyar_register(self, driver):
			viyar_page = ViyarBazarPage(driver, "https://viyarbazar.com/")
			viyar_page.open()
			viyar_page.register_on_bazar_viyar()
			viyar_page.viyti_s_akka()
			email_input = viyar_page.avtorizacion()
			email_output = viyar_page.check_email_in()
			viyar_page.after_register_viyar()
			print(email_output,email_input)
			assert email_input == email_output, "Почты разные почему то"
			time.sleep(5)

		def test_viyar_gallery(self, driver):
			gallery_page = ViyarBazarPage(driver, "https://viyarbazar.com/")
			gallery_page.open()
			gallery_page.avtorizacion()
			gallery_page.click_on_gallery()
			gallery_page.random_sort()
			gallery_page.button_more()
			gallery_page.random_portfolio()






