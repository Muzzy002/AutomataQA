import time

from pages.elements_page import ViyarBazarPage

class TestElementsBazara:

	class TestVicarBazaar:

		def test_viyar(self, driver):
			viyar_page = ViyarBazarPage(driver, "https://viyarbazar.com/")
			viyar_page.open()
			viyar_page.avtorizacion()
			time.sleep(5)
