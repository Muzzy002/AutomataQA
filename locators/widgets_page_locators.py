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

class ToolTipsPageLocators:
	BUTTON = (By.XPATH, '//div/button[@id="toolTipButton"]')
	TOOL_TIP_BUTTON = (By.XPATH, '//div/button[@aria-describedby="buttonToolTip"]')

	FIELD = (By.XPATH, '//div/input[@id="toolTipTextField"]')
	TOOL_TIP_FIELD = (By.XPATH, '//div/input[@aria-describedby="textFieldToolTip"]')

	CONTRTARY_LINK = (By.XPATH, '//*[.="Contrary"]')
	TOOL_TIP_CONTRARY = (By.XPATH, '//div/a[@aria-describedby="contraryTexToolTip"]')

	SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')
	TOOL_TIP_SECTION = (By.XPATH, '//div/a[@aria-describedby="sectionToolTip"]')

	ALL_TOOL_TIPS = (By.XPATH, '//div[@class="tooltip-inner"]')


class MenuPageLocators:

	MENU_ITEM_1 = (By.XPATH, '//li/a[text()="Main Item 1"]')
	MENU_ITEM_2 = (By.XPATH, '//li/a[text()="Main Item 2"]')
	MENU_ITEM_3 = (By.XPATH, '//li/a[text()="Main Item 3"]')

	ALL_ITEMS = (By.XPATH, '//li/a[@href]')


class SelectMenuPageLocators:

	INPUT_VALUE = (By.XPATH, '//div/input[@id="react-select-2-input"]')
	SELECT_VALUE = (By.XPATH, '//div[text()="Select Option"]')
	OUTPUT_VALUE = (By.XPATH, '//div[@class=" css-1uccc91-singleValue"]')

	SELECT_ONE_INPUT = (By.XPATH, '//div/input[@id="react-select-3-input"]')
	SELECT_ONE = (By.XPATH, '//div[text()="Select Title"]')
	OUTPUT_ONE = (By.XPATH, '(//div[@class=" css-1uccc91-singleValue"])[2]')

	OLD_STYLE_MENU = (By.XPATH, '//select[@id="oldSelectMenu"]')
	ALL_LIST_MULTI = (By.XPATH, '//div[@class="col-md-6 col-sm-12"]/div/select/option')

	MULTI_SELECT_DROP = (By.XPATH, '//div[text()="Select..."]')
	ALL_LIST = (By.XPATH, '//div[@class="col-md-6 col-sm-12"]/div/select/option')
	INPUT_MULTI = (By.XPATH, '//div/input[@id="react-select-4-input"]')
	DELETE_MULTI_SELECT = (By.XPATH, '(//div[@aria-hidden="true"])[3]')
	RESULT_MULTI = (By.XPATH, '//div[@class=" css-1hwfws3"] /div[@style]')

	STANDART_MULTI_SELECT = (By.XPATH, '//option[@value="volvo"]')
