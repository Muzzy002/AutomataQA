from selenium.webdriver.common.by import By


class SlidePageLocators:
	INPUT_SLIDER = (By.XPATH, '//span/input[@class="range-slider range-slider--primary"]')
	SLIDER_VALUE = (By.XPATH, '//div/input[@id="sliderValue"]')


class ProgressBarPageLocators:
	PROGRESS_BAR_BUTTON = (By.XPATH, '//button[@id="startStopButton"]')
	PROGRESS_BAR_VALUE = (By.XPATH, '//div[@class="progress-bar bg-info"]')
