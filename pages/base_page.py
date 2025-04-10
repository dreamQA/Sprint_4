from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def wait_for_element_to_be_clickable(self, locator,timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def find_element(self,locator):
        return self.browser.find_element(*locator)

    def scroll_to_element(self,element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_url_to_be(self,url,timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.url_contains(url))