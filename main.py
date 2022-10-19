import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests

# =IFERROR(MID(C2,77,7),"")

url1 = 'https://logs-prod.admortgage.net:3000/d/CeDhaW97k1/logs?orgId=1&var-host=edms_prod&var-service=edms_prod_OpenCloseFilesSync&var-app=All&from=now-90d&to=now&viewPanel=6'
url2 = 'https://logs-prod.admortgage.net:3000/d/CeDhaW97k1/logs?orgId=1&var-host=edms_prod&var-service=edms_prod_OpenCloseFilesSync_Instance2&var-app=All&from=now-90d&to=now&viewPanel=6'
url3 = 'https://logs-prod.admortgage.net:3000/d/CeDhaW97k1/logs?orgId=1&var-host=edms_prod&var-service=edms_prod_OpenCloseFilesSync_Instance3&var-app=All&from=now-90d&to=now&viewPanel=6'
url4 = 'https://logs-prod.admortgage.net:3000/d/CeDhaW97k1/logs?orgId=1&var-host=edms_prod&var-service=edms_prod_OpenCloseFilesSync_Instance4&var-app=All&from=now-90d&to=now&viewPanel=6'


def wait_xpath(xpath):
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, xpath)
        )
    )
    return element


global driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url1)

wait_xpath('//*[@id="reactRoot"]/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/a').click()
wait_xpath('//*[@id="i0116"]').send_keys('serg.pudikov@admortgage.com')
wait_xpath('//*[@id="idSIButton9"]').click()
wait_xpath('//*[@id="i0118"]').send_keys('Coq05714')
wait_xpath('//*[@id="idSIButton9"]').click()
wait_xpath('//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div/div/div[2]').click()
wait_xpath('//*[@id="idTxtBx_SAOTCC_OTC"]').send_keys(input('Verification Code: '))
wait_xpath('//*[@id="idSubmit_SAOTCC_Continue"]').click()
wait_xpath('//*[@id="idSIButton9"]').click()
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'lxml')
logs = soup.find_all('tr', class_='css-i3vz2t-logs-row')

dt1 = []
er1 = []
for each in logs:
    date_time = each.find('td', class_='css-1gzlb9j-logs-row__localtime').text
    error = each.find('span', class_='css-1wx8bl8-positionRelative').text

    dt1.append([date_time])
    er1.append([error])

    df1 = pd.DataFrame(data={'time': dt1, 'error': er1})
    df.to_excel('C:/Users/serg.pudikov/QA Files/Grafana.xlsx', sheet_name='Instance_1')


driver.get(url3)

soup = BeautifulSoup(driver.page_source, 'lxml')
logs = soup.find_all('tr', class_='css-i3vz2t-logs-row')

dt = []
er = []
for each in logs:
    date_time = each.find('td', class_='css-1gzlb9j-logs-row__localtime').text
    error = each.find('span', class_='css-1wx8bl8-positionRelative').text

    dt.append([date_time])
    er.append([error])

    df = pd.DataFrame(data={'time': dt, 'error': er})
    df.to_excel('C:/Users/serg.pudikov/QA Files/Grafana.xlsx', sheet_name='Instance_1')
driver.quit()

driver.get(url4)

soup = BeautifulSoup(driver.page_source, 'lxml')
logs = soup.find_all('tr', class_='css-i3vz2t-logs-row')

dt = []
er = []
for each in logs:
    date_time = each.find('td', class_='css-1gzlb9j-logs-row__localtime').text
    error = each.find('span', class_='css-1wx8bl8-positionRelative').text

    dt.append([date_time])
    er.append([error])

    df = pd.DataFrame(data={'time': dt, 'error': er})
    df.to_excel('C:/Users/serg.pudikov/QA Files/Grafana.xlsx', sheet_name='Instance_1')

driver.get(url2)

soup = BeautifulSoup(driver.page_source, 'lxml')
logs = soup.find_all('tr', class_='css-i3vz2t-logs-row')

dt = []
er = []
for each in logs:
    date_time = each.find('td', class_='css-1gzlb9j-logs-row__localtime').text
    error = each.find('span', class_='css-1wx8bl8-positionRelative').text

    dt.append([date_time])
    er.append([error])

    df = pd.DataFrame(data={'time': dt, 'error': er})
    df.to_excel('C:/Users/serg.pudikov/QA Files/Grafana.xlsx', sheet_name='Instance_1')

with pd.ExcelWriter('C:/Users/serg.pudikov/QA Files/Grafana.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Instance_1')
    df2.to_excel(writer, sheet_name='Instance_2')
    df3.to_excel(writer, sheet_name='Instance_3')
    df4.to_excel(writer, sheet_name='Instance_4')

driver.quit()

