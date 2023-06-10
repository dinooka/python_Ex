import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import webdriver_init as wb


my_driver = wb.DriverInit()

json_data = my_driver.get_json_data()
url = json_data['url']
username = json_data['username']
password = json_data['password']
driver = my_driver.browser_open(url)

username_ele = my_driver.wait_for_element(driver,By.ID,'username')
username_ele.send_keys(username) 

driver.find_element(By.ID,'password').send_keys(password)
driver.find_element(By.ID,'login').click()

 
# learn_ele = driver.find_element(By.XPATH, '//span[text()="Learn"]') 

# actions = ActionChains(driver)
# actions.move_to_element(learn_ele).perform()
# submenu = driver.find_element(By.XPATH, '//a[@href="https://www.chess.com/lessons"]') 
# submenu.click() 

# driver.quit()