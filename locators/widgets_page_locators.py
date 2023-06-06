from selenium.webdriver.common.by import By


class AccordianPageLocators:

	SECTION_FIRST = (By.XPATH, '//div[@id="section1Heading"]')
	SECTION_CONTENT_FIRST = (By.XPATH, '//div[@id="section1Content"]/p' )
	SECTION_SECOND = (By.XPATH, '//div[@id="section2Heading"]')
	SECTION_CONTENT_SECOND = (By.XPATH, '//div[@id="section2Content"]/p' )
	SECTION_THIRD = (By.XPATH, '//div[@id="section3Heading"]')
	SECTION_CONTENT_THIRD = (By.XPATH, '//div[@id="section3Content"]/p' )

class AutoCompletePageLocators:
	MULTI_INPUT = (By.XPATH, '//div/input[@id="autoCompleteMultipleInput"]')
	MULTI_VALUE = (By.XPATH, '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
	MULTI_VALUE_REMOVE = (By.XPATH, '//div[@class="css-xb97g8 auto-complete__multi-value__remove"]/*/*')

	SINGLE_VALUE = (By.XPATH, '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')
	SINGLE_INPUT = (By.XPATH, '//div[@class="auto-complete__value-container css-1hwfws3"]//div/input')

