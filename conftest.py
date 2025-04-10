import pytest
from selenium import webdriver

from pages.logo_page import LogoPage
from pages.order_details_page import OrderPage
from pages.faq_page import QestionsPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logo_page(browser):
    logo_page = LogoPage(browser)
    return logo_page

@pytest.fixture
def order_page(browser):
    order_page = OrderPage(browser)
    return order_page

@pytest.fixture
def faq_page(browser):
    faq_page = QestionsPage(browser)
    return faq_page