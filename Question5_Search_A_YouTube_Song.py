from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path=r"/home/marom/PycharmProjects/pythonProject/lecture8/geckodriver")
driver.get('https://www.youtube.com/')
time.sleep(2)

driver.maximize_window()

time.sleep(1)

searchbox = driver.find_element(By.XPATH, '//input[@id="search"]')
searchbox.send_keys('Rockstar')
time.sleep(1)
searchbutton = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
searchbutton.click()
time.sleep(5)
driver.close()