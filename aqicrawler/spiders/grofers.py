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

if __name__ == "__main__":
    # driver = webdriver.Chrome('/home/alpha/Downloads/chromedriver_linux64/chromedriver')
    driver = webdriver.Firefox('/home/alpha/Downloads/geckodriver-v0.26.0-linux64')
    driver.get('https://grofers.com')
    driver.implicitly_wait(10)

    timeout = 10
    # location_element = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/header/div[1]/a/div[2]')
    #dropdown enter city
    # enter_city_element = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/header/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]')
    # search_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/header/div[2]/div/div/div[1]/input')
    # sattu = driver.find_element_by_xpath('//div[@title="Grofers Mother\'s Choice Sattu"]')

    wait = WebDriverWait(driver,timeout)
    change_delivery_location = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'user-address')))
    # change_delivery_location = Select(driver.find_elements_by_class_name('user-address'))
    # change_delivery_location.select_by_visible_text('New Delhi')
    # clickable = driver.find_element_by_xpath('/div[@class="location__tooltip-footer"]')
    # /button[@class="btn.btn--inverted"]')
    # clickable.click()
    # driver.implicitly_wait(10)
    # time.sleep(2)
    # change_delivery_location = wait.until(EC.presence_of_element_located((By.XPATH,'/div[@class="location__overlay"]//button[@value="Change delivery city"]')))
    # change_delivery_location.click()
    seq = driver.find_elements_by_tag_name('iframe')

    for index in range(len(seq)):
        driver.switch_to.default_content()

        iframe = driver.find_elements_by_tag_name('iframe')[index]

        driver.switch_to.frame(iframe)

        driver.implicitly_wait(30)

        # highlight the contents of the selected iframe

        driver.find_element_by_tag_name('a').send_keys(Keys.CONTROL, 'a')

        time.sleep(2)

        # undo the selection within the iframe

        driver.find_element_by_tag_name('p').click()

        driver.implicitly_wait(30)

    driver.switch_to.default_content()

    enter_city = driver.switch_to.iframe(driver.find_element_by_xpath('/div[@class="location__overlay"]//div[@class="Select-input"]//input'))
    enter_city.send_keys('New Delhi')
    enter_city.send_keys(Keys.RETURN)
    # new_delhi = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[7]/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span')))
    # new_delhi.click()

    # delivery_dropdown = wait.until()

    # enter_city_element = Select(wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/header/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]'))))
    search_bar = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/header/div[2]/div/div/div[1]/input')))

    # enter_city_element.select_by_visible_text('New Delhi')
    search_bar.send_keys('sattu')
    search_bar.send_keys(Keys.RETURN)
    try:
        sattu = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@title="Grofers Mother\'s Choice Sattu"]')))
    except TimeoutException:
        print("Grofer's Sattu not found")
        driver.close()
        driver.quit()

    #so far so good - Grofer's Sattu is available!
    price_element = driver.find_elements_by_xpath('//div[@title="Grofers Mother\'s Choice Sattu"]//span[@class="plp-product__price--new"]')
    print(price_element.text)

    driver.close()
    driver.quit()