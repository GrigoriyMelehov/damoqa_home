from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_l = SwagLabs(browser)
    swag_l.visit()
    assert swag_l.exist_icon()


