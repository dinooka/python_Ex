from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class DriverInit:

    def get_json_data(self):
        with open('config.json',"r") as json_file:
            data = json.load(json_file)         
            url = data['url']
            username = data['username']
            password = data['password']
            return {"username":username,"url":url,"password":password}            

    def browser_open(self,url):        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        return driver

    def wait_for_element(self,driver, by, value, timeout=5):
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        return element


    
        