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
    #SEARCH_INPUT


class ViyarBazarLocators:

    ALL_TITLES = (By.XPATH , "//div[@class]/nav/a")
    BUTTON_YVITI = (By.XPATH, '//div[@class="auth "]')
    BUTTON_REGISTER = (By.XPATH, "//div/a[@class='item']")

    SECOND_NAME = (By.XPATH, "//div/input[@id='lastName']")
    FIRST_NAME = (By.XPATH, "//div/input[@id='firstName']")
    MIDDLE_NAME = (By.XPATH, "//div/input[@id='user.attributes.surname']")
    EMAIL = (By.XPATH, "//div/input[@id='email']")
    NUMBER = (By.XPATH, "//div/input[@id='user.attributes.phone']")
    VIRDEL = (By.XPATH, '//div/select[@id="user.attributes.role"]')
    VIRDEL_ZAMOVNIK = (By.XPATH, '//div/select/option[@value="client"]')
    PASSWORD = (By.XPATH, '//div/input[@id="password"]')
    CLONE_PASSWORD = (By.XPATH, '//div/input[@id="password-confirm"]')
    CHECK_BOX = (By.XPATH, '//div/label/span[@class="checkbox-custom"]')
    SUBMIT_REGISTER = (By.XPATH, '//div/button[@class="pf-c-button pf-m-primary pf-m-block btn-lg"]')

class ModalBazarLocators:

    ALL_OBLAST = (By.XPATH,'//ul/li/a[@class="toggle"]')
    ALL_CITYES = (By.XPATH,'//li[@class="active"]/div/div/*')
    CLOSE_MODAL = (By.XPATH,'//article/button[@class="close"]')
    TRI_TOCHKI = (By.XPATH,'//div/button[@class="btn settingsBtn"]')
    VIHOD_CHEREZ_TRI = (By.XPATH,'//div[@id="mySettings"]/ul/li/a[@href="/?logout=yes"]')

    #Avtorization
    INPUT_EMAIL = (By.XPATH,'//div/input[@id="username"]')
    INPUT_PASSWORD = (By.XPATH, '//div/input[@id="password"]')
    YVITI_KEKLOK = (By.XPATH,'//div/button[@class="pf-c-button pf-m-primary pf-m-block btn-lg"]')