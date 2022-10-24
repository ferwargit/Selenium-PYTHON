from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path='./driver/chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get('http://www.google.com')
driver.find_element('name','q').send_keys('Selenium')
sleep(1)
driver.close()
driver.quit()