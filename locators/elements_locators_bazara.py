from  selenium.webdriver.common.by import By



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
    CHECK_POSHTA = (By.XPATH, '//div/a/strong[@title]')

    ACCEPT_MODAL = (By.XPATH, '//div/button[@class="btn btn-blue-sm btn-light send select_cites"]')
    CLOSE_MODAL_SKAS = (By.XPATH, '//div/button[@class="btn btn-white-sm cansel"]')

class GalleryBazar:
    BUTTON_GALLERY_ON_HOME = (By.XPATH, '//nav/a[@class="gallery"]')
    ALL_SORT_GALLERY = (By.XPATH, '//div/ul/li[@data-index]/a[@href]')
    ALL_KARTOCHKI_PORTF = (By.XPATH, '//section//div[@class="swiper-slide"]')
    DOWNLOAD_MORE = (By.XPATH, '//section//div[@class="gallery_ajax_load_btn"]')



