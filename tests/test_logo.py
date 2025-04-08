import allure
import pytest
from conftest import browser
from pages.logo_page import LogoPage

@pytest.fixture
def logo_page():
    logo_page = LogoPage()
    return logo_page

class TestURL:
    @allure.title('Проверка URL Логотипа Самокат')
    def test_main_page(self,browser, logo_page):
        # Открытие браузера
        logo_page.open_browser(browser)
        # Клик по кнопке "Заказать" в шапке
        logo_page.click_order_button(browser)
        # Клик по логотипу "Самокат"
        logo_page.click_scooter_button(browser)
        # Проверка URL логотипа Самокат
        logo_page.should_main_page_url(browser)

    @allure.title('Проверка URL Логотипа Яндекс')
    def test_dzen_url(self, browser, logo_page):
        # Открытие браузера
        logo_page.open_browser(browser)
        # Клик по кнопке "Заказать" в шапке
        logo_page.click_yandex_button(browser)
        # Переключение на новоую вкладку
        logo_page.switching_to_the_tab(browser)
        # Ожидание загрузки страницы Дзен
        logo_page.wait_for_page_load(browser)
        # Проверка URL логотипа Самокат
        logo_page.should_dzen_url(browser)