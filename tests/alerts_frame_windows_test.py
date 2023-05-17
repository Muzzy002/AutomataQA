import time

from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:

	class TestBrowserWindows:

		def test_new_tab_and_window(self,driver):

			new_tab_page = BrowserWindowsPage(driver,"https://demoqa.com/browser-windows")
			new_tab_page.open()
			textt_result = new_tab_page.check_opened_new_tab('windOW') # TAB or WINDOW
			time.sleep(10)
			text_result = new_tab_page.check_opened_new_tab('Tab')
			assert text_result == textt_result

