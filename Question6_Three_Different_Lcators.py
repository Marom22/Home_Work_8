import driver as driver
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/marom/PycharmProjects/pythonProject/lecture8/chromedriver")
driver.get("https://translate.google.co.il/")

time.sleep(1)
driver.maximize_window()
time.sleep(1)

driver.find_element(by=By.XPATH, value='/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("תרגום חופשי")

print(driver.find_element(By.XPATH, value='/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea'))

time.sleep(3)
driver.close()

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/marom/PycharmProjects/pythonProject/lecture8/chromedriver")
driver.get("https://translate.google.co.il/")

time.sleep(1)
driver.maximize_window()
time.sleep(1)

driver.find_element(By.CLASS_NAME, value='er8xn').send_keys("תרגום שניׁ")

print(driver.find_element(By.CLASS_NAME, value='er8xn'))

time.sleep(3)
driver.close()

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/marom/PycharmProjects/pythonProject/lecture8/chromedriver")
driver.get("https://translate.google.co.il/")

time.sleep(1)
driver.maximize_window()
time.sleep(1)

driver.find_element(By.TAG_NAME, value='textarea').send_keys("תרגום שלישי")

print(driver.find_element(By.TAG_NAME, value='textarea'))
time.sleep(3)
driver.close()