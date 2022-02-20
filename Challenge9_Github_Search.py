from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/marom/PycharmProjects/pythonProject/lecture8/chromedriver")
driver.get('https://www.github.com/')
time.sleep(2)

driver.maximize_window()

time.sleep(1)

search_box = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')
search_box.send_keys('Selenium')
time.sleep(1)
search_box.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()