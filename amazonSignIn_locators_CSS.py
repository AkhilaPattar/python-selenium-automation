from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\rkshe\\Automation\\python-selenium-automation\\chromedriver.exe')
driver= webdriver.Chrome(service=service)

#using class + attribute: Locator for 'amazon' logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo[aria-label='Amazon']")

#using class: Locator for 'Creat account'
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#using ID: Locator for 'Your name' field
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

#using ID: Locator for 'email' field
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

#using multiple attributes: for 'password' field
driver.find_element(By.CSS_SELECTOR, "input[name='password'][type='password']")

#using ID: for 're-enter password' field
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

#using ID: for 'creat your amazon account'
driver.find_element(By.CSS_SELECTOR, "input#continue")

#using attribute partial match *=: for conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_condition_of_use?ie=UTF8&nodeId=508088']")

#using attribute partial match *=: for 'privacy notice'
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice?']")

#using class+partial attribute: for 'Sign in'
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin?openid.pape.max']" )

