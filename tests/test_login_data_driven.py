from playwright.sync_api import expect
import pytest
from utilities.data_reader_util import *
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from config import Conifg

csv_data=read_csv_data("testdata/logindata.csv")

@pytest.mark.parametrize("testName,email,password,expected", csv_data)
def test_login_data_driven(page,testName,email,password,expected):
    home_page=HomePage(page)
    login_page=LoginPage(page)
    my_account_page=MyAccountPage(page)


    home_page.click_my_account()
    home_page.click_login()
    login_page.login(email,password)

    if expected=="failure":

        expect(login_page.get_login_error()).to_have_text("Warning: No match for E-Mail Address and/or Password.")

    elif expected=="success":

        expect(my_account_page.get_my_account_page_heading()).to_have_text("My Account")

