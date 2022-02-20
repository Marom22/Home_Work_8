from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox(executable_path=r"/home/marom/PycharmProjects/pythonProject/lecture8/geckodriver")
driver.get("https://www.ynet.co.il")

def get_title():
    url = "https://www.ynet.co.il"
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    print("The title of the website is: ")
    for title in soup.find_all('title'):
        print(title.get_text())

time.sleep(1)

driver.maximize_window()

time.sleep(3)
driver.refresh()

def compare_title():
    url = "https://www.ynet.co.il"
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    print("Comparing the title of the website: ")
    for title in soup.find_all('title'):
        print(title.get_text())

if get_title() == compare_title():
    print("The titles are the same")

time.sleep(5)
driver.close()