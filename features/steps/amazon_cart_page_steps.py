from selenium.webdriver.common.by import By
from behave import given, when, then


@when('click on cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()


@then('verify that text Your Amazon Cart is empty shown')
def verify_empty_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
    assert context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-count.nav-cart-0.nav-progressive-attribute.nav-progressive-content").is_displayed(), 'cart is not empty'



