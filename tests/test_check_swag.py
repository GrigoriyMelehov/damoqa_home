from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    icon = SwagLabs(browser)
    icon.visit()
    assert icon.exist_icon()

def test_check_pole_user_name(browser):
    user_name = SwagLabs(browser)
    user_name.visit()
    assert user_name.exist_pole_un()

def test_check_pole_password(browser):
    password = SwagLabs(browser)
    password.visit()
    assert password.exist_pole_password()


