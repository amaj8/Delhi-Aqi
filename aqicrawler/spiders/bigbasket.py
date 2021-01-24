import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import datetime
import pandas as pd
import numpy as np
import json
import time

driver = webdriver.Chrome('/home/alpha/Downloads/chromedriver_linux64/chromedriver')
# driver = webdriver.Firefox('/home/alpha/Downloads/geckodriver-v0.26.0-linux64')
driver.get('https://www.bigbasket.com/')
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 20)
loc_elem = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@ng-click="vm.locdropdown()"]')))
loc_elem.click()
# loc_elem = driver.find_element_by_xpath('//a[@ng-click="vm.locdropdown()"]')
# loc_elem.click()