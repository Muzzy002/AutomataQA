import random

from selenium.webdriver.common.by import By


class ViyarBazarLocators:
	ALL_TITLES = (By.XPATH, "//div[@class]/nav/a")
	BUTTON_YVITI = (By.XPATH, '//div/button[@class="button button--orange button--radius--16 opener-signIn"]')
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
	ALL_OBLAST = (By.XPATH, '//ul/li/a[@class="toggle"]')
	ALL_CITYES = (By.XPATH, '//li[@class="active"]//div[@class="column"]//label[not(contains(@class, "no_active"))]')
	CLOSE_MODAL = (By.XPATH, '//article/button[@class="close"]')
	TRI_TOCHKI = (By.XPATH, '//div/button[@class="button auth-dropmenu__btn"]/span')
	VIHOD_CHEREZ_TRI = (By.XPATH, '//div/ul/li/a[contains(text(), "Вийти")]')
	CLOSE_MODAL_SKAS = (By.XPATH, '//button[@class="btn btn-white-sm cansel"]')
	ACCEPT_MODAL = (By.XPATH, '//button[@class="btn btn-blue-sm btn-light send select_cites"]')

	# Avtorization
	INPUT_EMAIL = (By.XPATH, '//div/input[@id="username"]')
	INPUT_PASSWORD = (By.XPATH, '//div/input[@id="password"]')
	YVITI_KEKLOK = (By.XPATH, '//div/button[@class="pf-c-button pf-m-primary pf-m-block btn-lg"]')
	CHECK_POSHTA = (By.XPATH, '//div/a//span[@data-title]')


	ALL_TITLES = (By.XPATH, "//div[@class]/nav/a")
	BUTTON_YVITI = (By.XPATH, '//div/button[@class="button button--orange button--radius--16 opener-signIn"]')
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


class GalleryBazar:
	BUTTON_GALLERY_ON_HOME = (By.XPATH, '//div/nav/ul/li/a[@href="/gallery/"]')
	ALL_SORT_GALLERY = (By.XPATH, '//div/ul/li[@data-index]/a[@href]')
	ALL_KARTOCHKI_PORTF = (By.XPATH, '//div[@class="swiper-slide"]')
	DOWNLOAD_MORE = (By.XPATH, '//section//div[@class="gallery_ajax_load_btn"]')
	CHECK_MAKER = (By.XPATH, '//div[@class="meta visible-desc"]/a/p/strong')


class ButtonHelp:
	BUTTON_DOPOMOGA = (By.XPATH, '(//li/a[@href="/faq/"])[2]')



class ReviewsBazar:
	BUTTON_REVIEWS_ON_TITLE = (By.XPATH, '//span[@class="icon icon--color--blue icon--size--32"]')
	BUTTON_IN_WATERFALL_ON_TITLE = (By.XPATH, '//li/a[@href="/reviews/"]')

	list_types = [8721, 8722, 8731, 8727, 8728, 8729, 8730, 8732, 76788, 76789, 170607, 20252]
	list_random_types = random.choice(list_types)

	FILTR_IN_REVIEWS = (
	By.XPATH, '//button[@class="project-heading__sort--btn filter--sorting"]/span[@class="icon icon--size--32"]')

	ALL_VIDI_MEBLIV = (By.XPATH, f'//div/label/input[@value="{random.choice(list_types)}"]')
	TEXT_ALL_VIDOV = (By.XPATH, f'//div/label/input[@value="{random.choice(list_types)}"]/following-sibling::*[2]')
	BUTTON_ACCEPT = (By.XPATH, '(//div//button/span[@class="button__text--sm offset--8--row text--weight--bolder"])[2]')

	RESULT = (By.XPATH, '//div[@class="review-comment__cat--furniture"]/div[@class="text"]')

	ALL_KARTOCHKI_CHECK_OPEN = (
	By.XPATH, '(//div/button[@class="icon icon--size--32 button button--transparent comment_element"])[1]')

	CHECK_IN_KARTOCHKA = (By.XPATH, '//div[@id="type_work"]')

	BUTTON_DOPOMOGA = (By.XPATH, '(//li/a[@href="/faq/"])[2]')
