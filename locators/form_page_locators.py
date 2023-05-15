import random

from selenium.webdriver.common.by import By


class FormPageLocators:

	REKLAMA = (By.XPATH, '//div[@id="fixedban"]/div')

	FIRST_NAME = (By.XPATH, '//div/input[@id="firstName"]')
	LAST_NAME = (By.XPATH, '//div/input[@id="lastName"]')
	GENDER = (By.XPATH, f'//div/input[@id="gender-radio-{random.randint(1, 3)}"]')
	MOBILE_NUMBER = (By.XPATH, '//div/input[@id="userNumber"]]')
	#DATE = (By.XPATH, '//div/input[@id="dateOfBirthInput"]')
	SUBJECT = (By.XPATH, '//div/input[@id="subjectsInput"]')
	HOBBIES = (By.XPATH, f'//div/input[@id="hobbies-checkbox-{random.randint(1,3)}"]')
	PICTURE = (By.XPATH, '//input[@id="uploadPicture"]')
	CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
	SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
	STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
	SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
	CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
	SUBMIT = (By.CSS_SELECTOR, '#submit')