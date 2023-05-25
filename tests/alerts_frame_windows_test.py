import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage


class TestAlertsFrameWindows:
	class TestBrowserWindows:

		def test_new_tab_and_window(self, driver):
			new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
			new_tab_page.open()
			textt_result = new_tab_page.check_opened_new_tab('windOW')  # TAB or WINDOW
			time.sleep(10)
			text_result = new_tab_page.check_opened_new_tab('Tab')
			assert text_result == textt_result

	class TestAlertsPage:

		def test_see_alert(self, driver):
			alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
			alert_page.open()
			alert_text = alert_page.check_see_alert()
			assert alert_text == "You clicked a button", "alert text not True "

		def test_check_alert_appear_5_sec(self, driver):
			alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
			alert_page.open()
			alert_text = alert_page.check_alert_appear_5_sec()
			assert alert_text == "This alert appeared after 5 seconds", "alert 5 sec text not True"

		def test_confirm_alert(self, driver):
			alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
			alert_page.open()
			alert_text = alert_page.check_confirm_alert()
			assert alert_text == "You selected Ok"

		def test_promt_alert(self, driver):
			alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
			alert_page.open()
			text, alert_text = alert_page.check_promt_alert()
			assert text in alert_text

	class TestFramesPage:

		def test_frames(self, driver):
			frame_page = FramesPage(driver, "https://demoqa.com/frames")
			frame_page.open()
			result_frame1 = frame_page.check_frame("frame1")
			result_frame2 = frame_page.check_frame("frame2")
			assert result_frame2 == ['This is a sample page', '100px', '100px']
			assert result_frame1 == ['This is a sample page', '500px', '350px']

	class TestNestedFramesPage:

		def test_nested_frames(self, driver):
			nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
			nested_frame_page.open()
			parent_text, child_text = nested_frame_page.check_nested_frame()
			assert parent_text == "Parent frame"
			assert child_text == "Child Iframe"
