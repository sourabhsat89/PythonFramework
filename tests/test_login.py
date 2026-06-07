from playwright.sync_api import expect
import pytest


from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from config import Conifg

def test_invalid_user_login(page):
    home_page=HomePage(page)
    login_page=LoginPage(page)

    home_page.click_my_account()
    home_page.click_login()
    login_page.set_email(Conifg.invalid_email)
    login_page.set_password(Conifg.invalid_password)
    login_page.click_login()

    expect(login_page.get_login_error()).to_have_text("Warning: No match for E-Mail Address and/or Password.")


def test_valid_user_login(page):
    home_page=HomePage(page)
    login_page=LoginPage(page)
    my_account_page=MyAccountPage(page)


    home_page.click_my_account()
    home_page.click_login()
    login_page.set_email(Conifg.email)
    login_page.set_password(Conifg.password)
    login_page.click_login()
    expect(my_account_page.get_my_account_page_heading()).to_have_text("My Account")