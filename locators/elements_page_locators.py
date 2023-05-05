from  selenium.webdriver.common.by import By

class TextBoxPageLocators:

    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")
    #TESTEER = "button[class='bwc-close']:nth-child(1)"

class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')

    SYES_RADIOBUTTON = (By.XPATH, '//div/label[@class="custom-control-label"][@for="yesRadio"]')
    SIMPRESSIVE_RADIOBUTTON = (By.XPATH,'//div/label[@class="custom-control-label"][@for="impressiveRadio"]')
    SNO_RADIOBUTTON = (By.XPATH,'//div/div[@class="custom-control disabled custom-radio custom-control-inline"]')
    SOUTPUT_RESULT = (By.XPATH,'//p/span[@class="text-success"]')


class WebTablePageLocators:
    ADD_BUTTON = (By.XPATH,'//div/button[@id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.XPATH,'//div/input[@id="firstName"]')
    LASTNAME_INPUT = (By.XPATH,'//div/input[@id="lastName"]')
    EMAIL_INPUT = (By.XPATH,'//div/input[@id="userEmail"]')
    AGE_INPUT = (By.XPATH,'//div/input[@id="age"]')
    SALARY_INPUT = (By.XPATH,'//div/input[@id="salary"]')
    DEPARTMENT_INPUT = (By.XPATH,'//div/input[@id="department"]')
    SUBMIT = (By.XPATH,'//div/button[@type="submit"]')

    #tables
    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')
    SEARCH_INPUT = (By.XPATH, '//div/input[@id="searchBox"]')
    DELETE_BUTTON = (By.XPATH, '//div/span[@title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    COUNT_ROW_LIST = (By.XPATH, '//div/span/select[@aria-label="rows per page"]')

    #update
    UPDATE_BUTTON = (By.XPATH, '//div/span[@title="Edit"]')
    NOT_FOUND_TEXT = (By.XPATH, '//div[@class="rt-noData"]')

#//div[@class="rt-tr-group"]



class ButtonsPageLocators:

    DOUBLE_BUTTON = (By.XPATH, '//div/button[@id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.XPATH, '//div/button[@id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//div[@class="mt-4"][2]/button')

    SUCCESS_DOUBLE = (By.XPATH, '//div/p[@id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.XPATH, '//div/p[@id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By.XPATH, '//div/p[@id="dynamicClickMessage"]')
