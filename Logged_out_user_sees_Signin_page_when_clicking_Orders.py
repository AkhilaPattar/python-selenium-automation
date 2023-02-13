from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\rkshe\\Automation\\python-selenium-automation\\chromedriver.exe')
driver= webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'nav-orders').click()

expected_result='Sign in'
actual_result= driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

print(actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'

print('Test case passed')

driver.quit()
