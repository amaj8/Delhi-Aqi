from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.chrome.options import Options

# from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def gmail():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../PycharmProjects/automateGoogleForms/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

gmail()

flipkart_form = 'https://docs.google.com/forms/d/e/1FAIpQLSeOv02i_5cJ7xbfI74eUTTeAu5gv30jkTVYeq5-MvWmO0oJPg/viewform'
slot1_form='https://docs.google.com/forms/d/e/1FAIpQLSejucka4tlzW8jpZLO8GuFzKnHyMgHO71x9TQ_38mJKhJGOAg/viewform'
link = flipkart_form

stackoverflow_login = 'https://stackoverflow.com/users/login'

data = {
    'iisc_email':'aalomajumdar@iisc.ac.in',
    'name':'Aalo Majumdar',
    'SRnum':'04-04-00-10-22-18-1-16116',
    'gender':'Female',
    'gmail':'aalomajumdar@gmail.com',
    'linkedin':'https://www.linkedin.com/in/aalo-majumdar',
    'skypeid':'live:.cid.350e6ce0f9f52029',
    'mobile':'8585926272',
    'alternate_mob':'9717432424',
    'cgpa':'7.75',
    'programme':'M.Tech (Res)',
    'department':'Computer Science and Automation',
    'grad_degree_name':'B.Tech',
    'grad_degree_stream':'B.Tech in Computer Science and Engineering',
    'grad_percentage':'79.83',
    'post_grad_degree_name':'M.Tech (Res)',
    'post_grad_degree_stream':'M.Tech (Res) in Computer Science and Automation',
    'post_grad_percentage':'7.75/10',
    'date_of_completion':'07/2021',
    'technical_skills':'Post-Quantum Cryptography, Machine Learning, Deep Learning, Data Analytics, Web Scraping, Python, PyTorch, C, Django',
    'thesis_overview':'Petzoldt et. al.’s ’A Practical Multivariate Blind Signature Scheme’ describe a security argument with a restricted version of OMF. Aim to give a security argument for the above scheme with respect to the standard definition of OMF.',
    'current_phd_status':'NA',
    'slot1_companies':['Alphonso','JP Morgan','Flipkart Internet Pvt Ltd','Myntra','Sony Japan'],
}

# driver = webdriver.Chrome('/home/alpha/Downloads/chromedriver_linux64/chromedriver')
# driver.get(stackoverflow_login)

# delay = 60
# try:
#     ss_logo = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,'/html/body/header/div/div[1]/a[2]/span')))
# except:
#     print("Took too long")
#
# driver.get(link)
# # driver.maximize_window()
#
#
# try:
#     email = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input')))
# except:
#     print("Took too long to get past the login page. Try increasing the wait time")
# # email = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input')
# email.send_keys(data['iisc_email'])
#
# name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# name.send_keys(data['name'])
#
# #Female_gender_selector
# female_gender = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label').click()
#
# iisc_email = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
# iisc_email.send_keys(data['iisc_email'])
#
# gmail = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
# gmail.send_keys(data['gmail'])
#
# linkedin = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
# linkedin.send_keys(data['linkedin'])
#
# skype = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
# skype.send_keys(data['skypeid'])
#
# mob = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
# mob.send_keys(data['mobile'])
#
# alt_mob = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')
# alt_mob.send_keys(data['alternate_mob'])
#
# sr_num = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input')
# sr_num.send_keys(data['SRnum'])
#
# cgpa = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input')
# cgpa.send_keys(data['cgpa'])
#
# #M.Tech Res programme selector
# programme = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[4]/label').click()
#
# #CSA department selector
# dept = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[21]/label').click()
#
# grad_degree_name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input')
# grad_degree_name.send_keys(data['grad_degree_name'])
#
# grad_degree_stream = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div[1]/div/div[1]/input')
# grad_degree_stream.send_keys(data['grad_degree_stream'])
#
# grad_percent = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div[1]/div/div[1]/input')
# grad_percent.send_keys(data['grad_percentage'])
#
# post_grad_degree_name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div[1]/div/div[1]/input')
# post_grad_degree_name.send_keys(data['post_grad_degree_name'])
#
# post_grad_degree_stream = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div[1]/div/div[1]/input')
# post_grad_degree_stream.send_keys(data['post_grad_degree_stream'])
#
# post_grad_percent = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div[1]/div/div[1]/input')
# post_grad_percent.send_keys(data['post_grad_percentage'])
#
# date_of_completion = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/div[1]/div/div[1]/input')
# date_of_completion.send_keys(data['date_of_completion'])
#
# technical_skills = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/div[1]/div[2]/textarea')
# technical_skills.send_keys(data['technical_skills'])
#
# thesis = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/div[1]/div[2]/textarea')
# thesis.send_keys(data['thesis_overview'])
#
# pursuing_phd = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/div/span/div/div[6]/label').click()
#
#
