from selenium.webdriver.common.by import By
from behave import given, when, then


# AMAZON_SEARCH_FIELD = (By.ID, "twotabsearchtextbox")
# SEARCH_ICON = (By.CSS_SELECTOR, "input#nav-search-submit-button")
# PRODUCT_PRICE = (By.CSS_SELECTOR, "div[data-component-type='s-search-result'] span.a-price")
# ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
# CART = (By.ID, "nav-cart-count-container")
# CART_COUNT = (By.ID, "nav-cart-count")


# @given('open amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')
#
#
# @when('input text {search_word}')
# def input_search_word(context, search_word):
#     context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)
#
#
# @when('click on search button')
# def click_search(context):
#     context.driver.find_element(*SEARCH_ICON).click()
#
#
# @when('click on the first product price')
# def click_first_product(context):
#     context.driver.find_element(*PRODUCT_PRICE).click()
#
#
# @when('click on Add to cart button')
# def click_Add_to_cart_button(context):
#     context.driver.find_element(*ADD_TO_CART_BUTTON).click()


#
# @when('click on cart')
# def click_cart(context):
#     context.driver.find_element(*CART).click()
#
#
# @then('verify that {expected_count} item is shown in the cart')
# def verify_cart_count(context, expected_count):
#     actual_count = context.driver.find_element(*CART_COUNT).text
#     assert expected_count == actual_count, f'Expected count {expected_count} but got actual count {actual_count}'
