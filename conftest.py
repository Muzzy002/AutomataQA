from datetime import datetime

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope='function')
def driver():
	driver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=driver_service)
	driver.maximize_window()
	yield driver
	attach = driver.get_screenshot_as_png()
	allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
	driver.quit()




#pytest --alluredir=tests/allure_results ./tests/elements_test.py зупастить тесты с с файла и загрузить в папку
#allure serve ./tests/allure_results запустить аналитику по пройденныим ранее тестам
#@allure.suite() @allure.feature("TextBox") @allure.title("Check TextBox") обертки для склассов подклассов и функций
#@allure.step() with allure.step() обертки для конкретных шагов в функциях
#pip freeze >./requirements.txt для сохранинения зависимостей в файл либо оно так же его может создать