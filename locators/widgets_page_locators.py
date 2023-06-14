from selenium.webdriver.common.by import By


class AccordianPageLocators:
	SECTION_FIRST = (By.XPATH, '//div[@id="section1Heading"]')
	SECTION_CONTENT_FIRST = (By.XPATH, '//div[@id="section1Content"]/p')
	SECTION_SECOND = (By.XPATH, '//div[@id="section2Heading"]')
	SECTION_CONTENT_SECOND = (By.XPATH, '//div[@id="section2Content"]/p')
	SECTION_THIRD = (By.XPATH, '//div[@id="section3Heading"]')
	SECTION_CONTENT_THIRD = (By.XPATH, '//div[@id="section3Content"]/p')


class AutoCompletePageLocators:
	MULTI_INPUT = (By.XPATH, '//div/input[@id="autoCompleteMultipleInput"]')
	MULTI_VALUE = (By.XPATH, '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
	MULTI_VALUE_REMOVE = (By.XPATH, '//div[@class="css-xb97g8 auto-complete__multi-value__remove"]/*/*')

	SINGLE_VALUE = (By.XPATH, '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')
	SINGLE_INPUT = (By.XPATH, '//div[@class="auto-complete__value-container css-1hwfws3"]//div/input')


class DatePickerPageLocators:
	DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
	DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
	DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
	DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

	DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
	DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
	DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
	DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
	DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
	DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class TabsPageLocators:
	TABS_WHAT = (By.XPATH, '//div/nav/a[@id="demo-tab-what"]')
	TABS_WHAT_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-what"]/..')
	TABS_ORIGIN = (By.XPATH, '//div/nav/a[@id="demo-tab-origin"]')
	TABS_ORIGIN_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-what"]/..')
	TABS_USE = (By.XPATH, '//div/nav/a[@id="demo-tab-use"]')
	TABS_USE_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-what"]/..')
	TABS_MORE = (By.XPATH, '//div/nav/a[@id="demo-tab-more"]')
	TABS_MORE_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-what"]/..')
