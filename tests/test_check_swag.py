from pages.swag_labs import SwagLabs


def test_check_element(browser):
    element = SwagLabs(browser)
    element.visit()
    assert element.exist_icon() #ищем иконку
    assert element.exist_pole_un() #ищем поле юзернэйм)
    assert element.exist_pole_password() #ищем поле пассворд)


