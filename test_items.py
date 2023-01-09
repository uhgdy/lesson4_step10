import time
from selenium.webdriver.common.by import By


def test_button(browser):
    #открытие страницы
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(3)

    #поиск кнопки по классу
    button = browser.find_elements(By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")

    assert len(button)==1, "Кнопка не найдена"
