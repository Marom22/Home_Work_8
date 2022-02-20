from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/marom/PycharmProjects/pythonProject/lecture8/chromedriver")
driver.get("https://www.facebook.com/")

time.sleep(1)
driver.maximize_window()
time.sleep(1)

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys("username@email.com")

time.sleep(1)
driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys("Password")

time.sleep(1)

searchbutton = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
searchbutton.click()

time.sleep(35)
driver.close()