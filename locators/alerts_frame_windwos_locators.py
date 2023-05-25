from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
	BUTTON_NEW_TAB = (By.XPATH, '//div/button[@id="tabButton"]')
	CHECKED_NEW_TAB = (By.XPATH, '//h1[@id="sampleHeading"]')
	BUTTON_NEW_WINDOW = (By.XPATH, '//div/button[@id="windowButton"]')


class AlertsPageLocators:
	SEE_ALERT_BUTTON = (By.XPATH, '//div/button[@id="alertButton"]')
	APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.XPATH, '//div/button[@id="timerAlertButton"]')
	CONFIRM_BOX_ALERT_BUTTON = (By.XPATH, '//div/button[@id="confirmButton"]')
	CONFIRM_RESULT = (By.XPATH, '//div/span[@id="confirmResult"]')
	PROMT_BOX_ALERT_BUTTON = (By.XPATH, '//div/button[@id="promtButton"]')
	PROMT_RESULT = (By.XPATH, '//div/span[@id="promptResult"]')


class FramesPageLocators:

	FIRST_FRAME = (By.XPATH, '//div/iframe[@id="frame1"]')
	SECOND_FRAME = (By.XPATH, '//div/iframe[@id="frame2"]')
	TITLE_FRAME = (By.XPATH, '//h1[@id="sampleHeading"]')


class NestedFramesPageLocators:
	PARENT_FRAME = (By.XPATH, '//div/iframe[@id="frame1"]')
	PARENT_TEXT = (By.CSS_SELECTOR, 'body')
	CHILD_FRAME = (By.XPATH, '//body/iframe[@srcdoc="<p>Child Iframe</p>"]')
	CHILD_TEXT = (By.XPATH, '//body/p')

