import allure
import pytest
from pages.logo_page import LogoPage


class TestURL:
    @allure.title('Проверка URL Логотипа Самокат')
    def test_main_page(self, logo_page):
        # Открытие браузера
        logo_page.open_browser()
        # Клик по кнопке "Заказать" в шапке
        logo_page.click_order_button()
        # Клик по логотипу "Самокат"
        logo_page.click_scooter_button()
        # Проверка URL логотипа Самокат
        logo_page.should_main_page_url()

    @allure.title('Проверка URL Логотипа Яндекс')
    def test_dzen_url(self, logo_page):
        # Открытие браузера
        logo_page.open_browser()
        # Клик по кнопке "Заказать" в шапке
        logo_page.click_yandex_button()
        # Переключение на новоую вкладку
        logo_page.switching_to_the_tab()
        # Ожидание загрузки страницы Дзен
        logo_page.wait_for_page_load()
        # Проверка URL логотипа Самокат
        logo_page.should_dzen_url()