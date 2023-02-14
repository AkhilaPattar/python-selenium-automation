from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\rkshe\\Automation\\python-selenium-automation\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.ebay.com/')

# driver.find_element(By.ID, 'gh-ac').send_keys('watch')
# driver.find_element(By.ID, 'gh-btn').click()

driver.find_element(By.XPATH, "//a[@href='https://www.ebay.com/deals']").click()

expected_result = 'Deals'
actual_result = driver.find_element(By.XPATH, "//a[text()='Deals']").text
sleep(5)

print(actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but got the actual {actual_result}'

print('Test case passed')

driver.quit()
