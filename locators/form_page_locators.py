from selenium.webdriver.common.by import By


class FormPageLocators:

	REKLAMA = (By.XPATH, '//div[@id="fixedban"]/div')

	FIRST_NAME = (By.XPATH, '//div/input[@id="firstName"]')
	LAST_NAME = (By.XPATH, '//div/input[@id="lastName"]')
	GENDER_MALE = (By.XPATH, '//div/input[@id="gender-radio-1"]')
	GENDER_FEMALE = (By.XPATH, '//div/input[@id="gender-radio-2"]')
	GENDER_OTHER = (By.XPATH, '//div/input[@id="gender-radio-3"]')
	MOBILE_NUMBER = (By.XPATH, '//div/input[@id="userNumber"]]')
	DATE = (By.XPATH, '//div/input[@id="dateOfBirthInput"]')
	SUBJECT = (By.XPATH, '(//div[@class="col-md-9 col-sm-12"])[5]/div')