from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/marom/PycharmProjects/pythonProject/lecture8/chromedriver")
driver.get("https://www.google.com/")

time.sleep(1)
driver.maximize_window()
time.sleep(1)

print(driver.get_cookies())
driver.delete_all_cookies()
print(driver.get_cookies())
driver.close()
print('Done')
