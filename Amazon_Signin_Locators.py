from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service= Service('C:\\Users\\rkshe\\Automation\\python-selenium-automation\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fbestsellers%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
driver.find_element(By.ID, 'ap_email')

driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use')]")
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//span[text()='Need help' and @class='a-expander-prompt' ]")
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.ID, 'ap-other-signin-issues-link')
driver.find_element(By.ID, 'createAccountSubmit')