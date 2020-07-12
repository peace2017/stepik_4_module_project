from .pages.login_page import LoginPage


def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
