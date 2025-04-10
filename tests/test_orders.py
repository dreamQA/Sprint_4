import allure
import pytest
from data import OrderData
from pages.order_details_page import OrderPage

class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method,data_order',[('click_first_button', OrderData.FIRST_ORDER), ('click_second_button', OrderData.SECOND_ORDER)])

    def test_make_an_order(self,order_page,data_order,button_method):

        #Открытие браузера
        order_page.open_browser()
        # Клик по кнопку "заказать" в шапке и в центре лендинга через button_method
        getattr(order_page, button_method)()
        #Заполнение полей для заказа,через параметр data_order
        order_page.user_rent_order(**data_order)
        # Проверка окна подтверждения по тексту "Заказ оформлен"
        order_page.confirmation_window()
