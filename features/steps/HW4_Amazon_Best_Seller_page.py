from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLER = (By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']")
BEST_SELLER_HEADER_LINKS = (By.CSS_SELECTOR, "div#zg_header div[class*='zg-nav-tab-all_style_zg-tabs-li']")


@when('click on Best Seller link')
def Best_seller_link(context):
    context.driver.find_element(*BEST_SELLER).click()


@then('verify Best Seller page has {expected_links} header links')
def Best_seller_header_links(context, expected_links):
    expected_links = int(expected_links)
    header_links = context.driver.find_elements(*BEST_SELLER_HEADER_LINKS)
    assert len(header_links) == expected_links, f'Expected {expected_links} header links but got {len(header_links)} links'




