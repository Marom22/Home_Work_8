from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/marom/PycharmProjects/pythonProject/lecture8/chromedriver")
driver.get("https://www.walla.co.il/")

time.sleep(1)

driver.maximize_window()

time.sleep(3)
driver.refresh()

url = "https://www.walla.co.il/"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
print("The title of the website is : ")
for title in soup.find_all('title'):
    print(title.get_text())

time.sleep(5)
driver.close()