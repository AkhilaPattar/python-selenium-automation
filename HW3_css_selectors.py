from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\rkshe\\Automation\\python-selenium-automation\\chromedriver.exe')
driver= webdriver.Chrome(service=service)


#By CSS, using ID
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag icp-nav-flag-us icp-nav-flag-lop')


#By CSS, using class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag')
#multiple class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')
# only 2 class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us')


#BY using CSS, using attributes(except ID & class)
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
#multiple attributes
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")

#By using class+attribute
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers']")
#attribute partial match *=
driver.find_element(By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']")


