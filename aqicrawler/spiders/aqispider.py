import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import datetime
import pandas as pd
import numpy as np
import json
import time
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    # chrome_options = Options()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/home/alpha/Downloads/chromedriver_linux64/chromedriver')

    # driver = webdriver.Firefox('/home/alpha/Downloads/geckodriver-v0.26.0-linux64')

    # date = '15/05/2020'
    # station_num = 8
    date_element = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[4]/div/input')
    station_element = Select(driver.find_element_by_xpath('//*[@id="stations"]'))
    time_element = driver.find_element_by_xpath('//*[@id="time"]')


    timeline = ['20:00','0:00', '4:00', '8:00', '12:00', '16:00']

    start_date = datetime.datetime(2020,5,31)
    end_date = datetime.datetime(2020,5,31)
    step = datetime.timedelta(days=1)

    # print(start_date.strftime('%d/%m/%Y'),end_date.strftime('%d/%m/%Y'))

    dates = []
    lst_dates_for_file = []
    d = start_date
    while d <= end_date:
        dates.append(d.strftime('%d/%m/%Y'))
        lst_dates_for_file.append(d)
        d += step

    # print(dates)

    driver.implicitly_wait(10)
    stations = [o.text for o in station_element.options]                    #note that the first text is '--Select Station--'
    stations = stations[1:]                                                 #removed the first text

    # df = pd.DataFrame(columns=['Date','Time','Station',
    #                            'PM2.5_avg','PM2.5_min','PM2.5_max',
    #                            'PM10_avg','PM10_min','PM10_max',
    #                            'NO2_avg','NO2_min','NO2_max',
    #                            'NH3_avg','NH3_min','NH3_max',
    #                            'SO2_avg','SO2_min','SO2_max',
    #                            'CO_avg','CO_min','CO_max',
    #                            'OZONE_avg','OZONE_min','OZONE_max',])
    #
    # pollutants = ['PM2.5_avg','PM2.5_min','PM2.5_max',
    #                            'PM10_avg','PM10_min','PM10_max',
    #                            'NO2_avg','NO2_min','NO2_max',
    #                            'NH3_avg','NH3_min','NH3_max',
    #                            'SO2_avg','SO2_min','SO2_max',
    #                            'CO_avg','CO_min','CO_max',
    #                            'OZONE_avg','OZONE_min','OZONE_max']
    #
    # pollutants_avg = ['PM2.5_avg','PM10_avg','NO2_avg','NH3_avg','SO2_avg','CO_avg','OZONE_avg']
    # pollutants_min = ['PM2.5_min','PM10_min','NO2_min','NH3_min','SO2_min','CO_min''OZONE_min']
    # pollutants_max = ['PM2.5_max','PM10_max','NO2_max','NH3_max','SO2_max','CO_max','OZONE_max']

    # add_to_df = []

    for date, date_for_file in zip(dates,lst_dates_for_file):
        print(date," has started")
        add_to_df = []
        idx = 0
        # Setting date
        while len(date_element.get_attribute('value')) == 0:  # wait for default text to load, else what we send get overwritten
            continue
        # date_element.send_keys(Keys.CONTROL+"a")
        date_element.clear()  # erase existing text
        date_element.send_keys(date)
        # date_element.send_keys(Keys.RETURN)

        #Selecting stations
        for s in stations:
            station_element.select_by_visible_text(s)

            #Setting time
            for t in timeline:
                while len(time_element.get_attribute('value')) == 0:           #wait for default text to load, else what we send get overwritten
                    continue
                # date_element.send_keys(Keys.CONTROL+"a")
                time_element.clear()                            #erase existing text
                time_element.send_keys(t)
                time_element.send_keys(Keys.RETURN)

                # driver.implicitly_wait(10)
                time.sleep(4)

                # df = df.append({'Date':date,'Time':time,'Station':s},ignore_index=True)
                # add_to_df = {'Date':date,'Time':time,'Station':s}
                # driver.implicitly_wait(10)
                timeout = 1
                wait = WebDriverWait(driver,10)
                try:
                    elements = [e.text for e in driver.find_elements_by_class_name('element-name')]
                    # elements = [e.text for e in wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'element-name')))]
                except StaleElementReferenceException as Exception:
                    print('StaleElementReferenceException, trying to find element again')
                    time.sleep(timeout)
                    elements = [e.text for e in driver.find_elements_by_class_name('element-name')]

                try:
                    avg_elements = [e.text for e in driver.find_elements_by_class_name('avg-value')]
                    # avg_elements = [e.text for e in wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'avg-value')))]
                except StaleElementReferenceException as Exception:
                    print('StaleElementReferenceException, trying to find element again')
                    time.sleep(timeout)
                    avg_elements = [e.text for e in driver.find_elements_by_class_name('avg-value')]


                try:
                    min_elements = [e.text for e in driver.find_elements_by_class_name('min-value')]
                    # min_elements = [e.text for e in wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'min-value')))]
                except StaleElementReferenceException as Exception:
                    print('StaleElementReferenceException, trying to find element again')
                    time.sleep(timeout)
                    min_elements = [e.text for e in driver.find_elements_by_class_name('min-value')]

                try:
                    max_elements = [e.text for e in driver.find_elements_by_class_name('max-value')]
                    # max_elements = [e.text for e in wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'max-value')))]
                except StaleElementReferenceException as Exception:
                    print('StaleElementReferenceException, trying to find element again')
                    time.sleep(timeout)
                    max_elements = [e.text for e in driver.find_elements_by_class_name('max-value')]


                add_to_df.append({'Date':date,'Time':t,'Station':s, \
                                  'Pollutants':tuple(zip(elements,avg_elements,min_elements,max_elements))})

                # break
            # break

        # with open('{date}'.format(date=date), 'w') as f:
        with open('{date}'.format(date=date_for_file), 'w') as f:
            json.dump(add_to_df, f)

        print(date, " over")


            # break

                # try:
                #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody')))
                # except TimeoutException:
                #     pass  # Handle the exception here
                # try:
                # table_element = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody')

                # table_xpath = '/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody'
                # ignored_exceptions = (StaleElementReferenceException,)
                # # table_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
                # #     .until(EC.presence_of_element_located((By.XPATH, table_xpath)))
                # timeout = 30
                # wait = WebDriverWait(driver, timeout)
                # # avg_element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions) \
                # #     .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'avg-value')))
                # avg_element = driver.find_element_by_class_name('avg-value')
                # wait.until(EC.staleness_of(avg_element))
                # avg_element = driver.find_elements_by_class_name('avg-value')
                #
                # avg_vals = [a.text for a in avg_element]
                # #
                # min_element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions) \
                #     .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'min-value')))
                #
                # min_vals = [a.text for a in min_element]
                #
                # max_element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions) \
                #     .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'max-value')))
                #
                # max_vals = [a.text for a in max_element]
                #
                # WebDriverWait(driver,timeout).until(EC.staleness_of(avg_element))
                # WebDriverWait(driver,timeout).until(EC.staleness_of(min_element))
                # WebDriverWait(driver,timeout).until(EC.staleness_of(max_element))
                #
                # avg_element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions) \
                #     .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'avg-value')))
                #
                # min_element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions) \
                #     .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'min-value')))
                # max_element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions) \
                #     .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'max-value')))

                # avg_element = lambda : driver.find_elements_by_class_name('avg-value')
                # min_element = lambda: driver.find_elements_by_class_name('min-value')
                # max_element = lambda: driver.find_elements_by_class_name('max-value')






                # add_to_df.update(tuple(zip(pollutants_avg,avg_vals)))
                # add_to_df.update(tuple(zip(pollutants_min, min_vals)))
                # add_to_df.update(tuple(zip(pollutants_max, max_vals)))
                # idx = 0
                # for a in avg_element:
                #     try:
                #         add_to_df[pollutants_avg[idx]] = a.text
                #     except:
                #         print("index value " + str(idx))
                #     print(a.text)
                #     idx += 1
                #
                # idx = 0
                # for m in min_element:
                #     try:
                #         add_to_df[pollutants_min[idx]] = m.text
                #     except:
                #         print("index value " + str(idx))
                #     # print(m.text)
                #     idx += 1
                #
                # idx = 0
                # for mx in max_element:
                #     try:
                #         add_to_df[pollutants_max[idx]] = mx.text
                #     except:
                #         print("index value " + str(idx))
                #     # print(mx.text)
                #     idx += 1

                # driver.implicitly_wait(20)
                # except:
                #     continue

                # pollutants_gen = (p for p in pollutants)
                # table_xpath = '/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody'
                # # wait = WebDriverWait(driver,10,ignored_exceptions=(StaleElementReferenceException,NoSuchElementException))
                # # table_element = WebDriverWait(driver, 30, ignored_exceptions=(StaleElementReferenceException,)) \
                # #         .until(EC.presence_of_element_located((By.XPATH, table_xpath)))
                # # driver.implicitly_wait(30)
                # # table_element = driver.find_element_by_xpath(table_xpath)
                # # Values - avg, min, max
                # for row in range(1, 8):
                #     for col in [3, 4, 5]:
                #         try:
                #             val = driver.find_element_by_xpath(table_xpath+'/tr[{row}]/td[{col}]'.format(row=row, col=col)).text
                #             # val_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
                #             # .until(EC.presence_of_element_located((By.XPATH, table_xpath)))
                #
                #             add_to_df[pollutants[idx%21]] = val
                #             idx += 1
                #             print(val)
                #         except:
                #             idx += 1
                #             print("row = "+ str(row) + " col= "+ str(col))
                #             continue



                # df = df.append(add_to_df,ignore_index=True)
            # break

    driver.close()
    driver.quit()
    # print(df.head())
    # df.to_csv('{start_date}_{end_date}.csv'.format(start_date = start_date,end_date = end_date),index=False)
    # with open('{start_date}_{end_date}'.format(start_date = start_date,end_date = end_date),'w') as f:
    #     json.dump(add_to_df,f)


    # class aqiSpider(scrapy.Spider):
    #     name ="aqi"
    #     start_urls= []
    #
    #     def __init__(self):
    #         self.driver = webdriver.Firefox()
    #
    #     def parse(self, response):
    #         self.driver.get(response.url)



