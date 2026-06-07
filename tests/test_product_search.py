from playwright.sync_api import expect

from pages.search_results_page import SearchResultsPage

from pages.home_page import HomePage

from config import Conifg


def test_product_search(page):
    product_name=Conifg.product_name
    home_page=HomePage(page)
    search_results_page=SearchResultsPage(page)

    home_page.enter_product_name(product_name)
    home_page.click_search()

    expect(search_results_page.get_search_results_page_header()).to_be_visible()
    expect(search_results_page.is_product_exist(product_name)).to_be_visible()
