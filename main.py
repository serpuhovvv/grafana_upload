# pip install -r requirements.txt

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

# Excel
# Getting loannumber from error message: =IFERROR(MID(C2,77,7),"")
# Asserting loannumber is number: =IF(ISNUMBER(D2), D2, "")
# Getting doctype and docname: =IFERROR(MID(C2,156,112),"")
# Asserting doctype and docname exist =IF(ISNUMBER(SEARCH("DocumentTypeName", E2)), E2, "")
# Копировать и вставить туда же полученные значения с опцией только значения, нажать на ошибку и отформатировать в числа

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
time.sleep(10)

soup1 = BeautifulSoup(driver.page_source, 'lxml')
logs1 = soup1.find_all('tr', class_='css-i3vz2t-logs-row')
print((len(logs1)))

dt1 = []
er1 = []
for each1 in logs1:
    date_time1 = each1.find('td', class_='css-1gzlb9j-logs-row__localtime').text
    error1 = each1.find('span', class_='css-1wx8bl8-positionRelative').text

    dt1.append([date_time1])
    er1.append([error1])

    df1 = pd.DataFrame(data={'time': dt1, 'error': er1})


time.sleep(20)
driver.get(url2)
time.sleep(10)

soup2 = BeautifulSoup(driver.page_source, 'lxml')
logs2 = soup2.find_all('tr', class_='css-i3vz2t-logs-row')
print((len(logs2)))

dt2 = []
er2 = []
for each2 in logs2:
    date_time2 = each2.find('td', class_='css-1gzlb9j-logs-row__localtime').text
    error2 = each2.find('span', class_='css-1wx8bl8-positionRelative').text

    dt2.append([date_time2])
    er2.append([error2])

    df2 = pd.DataFrame(data={'time': dt2, 'error': er2})


time.sleep(20)
driver.get(url3)
time.sleep(10)

soup3 = BeautifulSoup(driver.page_source, 'lxml')
logs3 = soup3.find_all('tr', class_='css-i3vz2t-logs-row')
print((len(logs3)))

dt3 = []
er3 = []
for each3 in logs3:
    date_time3 = each3.find('td', class_='css-1gzlb9j-logs-row__localtime').text
    error3 = each3.find('span', class_='css-1wx8bl8-positionRelative').text

    dt3.append([date_time3])
    er3.append([error3])

    df3 = pd.DataFrame(data={'time': dt3, 'error': er3})


time.sleep(20)
driver.get(url4)
time.sleep(10)

soup4 = BeautifulSoup(driver.page_source, 'lxml')
logs4 = soup4.find_all('tr', class_='css-i3vz2t-logs-row')
print((len(logs4)))

dt4 = []
er4 = []
for each4 in logs4:
    date_time4 = each4.find('td', class_='css-1gzlb9j-logs-row__localtime').text
    error4 = each4.find('span', class_='css-1wx8bl8-positionRelative').text

    dt4.append([date_time4])
    er4.append([error4])

    df4 = pd.DataFrame(data={'time': dt4, 'error': er4})

with pd.ExcelWriter('C:/Users/serg.pudikov/QA Files/Grafana.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Instance_1')
    df2.to_excel(writer, sheet_name='Instance_2')
    df3.to_excel(writer, sheet_name='Instance_3')
    df4.to_excel(writer, sheet_name='Instance_4')

driver.quit()

