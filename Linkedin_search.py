from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

#driver = webdriver.Chrome(executable_path='C:\\Users\\rkshe\\Automation\\python-selenium-automation\\chromedriver.exe')
service= Service('C:\\Users\\rkshe\\Automation\\python-selenium-automation\\chromedriver.exe')
driver= webdriver.Chrome(service=service)
driver.get('https://www.linkedin.com')

driver.find_element(By.ID, 'session_key').send_keys('akhilarajkumar2014@gmail.com')
driver.find_element(By.ID, 'session_password').send_keys('Akhilarajkumar123*')
sleep(3)

driver.find_element(By.XPATH, "//button[@class='sign-in-form__submit-button']").click()
sleep(10)

driver.quit()


