from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='C:\\Users\\rkshe\\Automation\\python-selenium-automation\\chromedriver.exe')

#By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

#By Xpath: tag & attribute
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//img[@alt='TruRemedy Premium Organic Body Wash & Balm']")

#By Xpath: multiple attributes
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo' and @aria-label='Amazon']")

#By Xpath : contains
