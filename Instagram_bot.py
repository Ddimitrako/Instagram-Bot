from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import csv
from random import randrange

options = Options()
options.binary_location = r"C:\Users\dimitris\AppData\Local\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r'C:\Users\dimitris\geckodriver.exe', options=options)


def get_data_from_href():
    with open('href_list.csv', 'r', encoding='UTF8') as f:
        # create the csv writer
        reader = csv.reader(f)
        for href in reader:
            print(href)
            if len(href):
                driver.get(href[0])
                time.sleep(1)
                emailDiv = driver.find_element(By.CLASS_NAME, 'emailContLbl')
                email = emailDiv.find_element_by_css_selector('a').get_attribute('href')
                print(email)
                time.sleep(1)


def start():
    hrefList = []
    with open('href_list.csv', 'w+', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)
        for i in range(10):
            # driver.get(f"https://www.vrisko.gr/search/Κτηνιατρεία-Κτηνιατρικές-Κλινικές/?page={i}")
            driver.get(f"https://www.vrisko.gr/search/%CE%BC%CE%B5%CF%83%CE%B9%CF%84%CE%B7%CF%82/%CE%91%CE%B8%CE%AE%CE%BD%CE%B1-%CE%91%CE%A4%CE%A4%CE%99%CE%9A%CE%97%CE%A3/?page={i}")
            time.sleep(2)

            # acceptCookies= driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
            # acceptCookies.click()

            # time.sleep(2)
            # usr_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            # usr_ent.clear()
            # usr_ent.send_keys(usr)
            try:
                for i in range(20):

                    div = driver.find_element(By.ID, 'AreaLeft_' + str(i))
                    href = div.find_element_by_css_selector('a').get_attribute('href')
                    # print(href)
                    hrefList.append(href)
                    writer.writerow([href])
            except Exception as e:
                print(e)
    print(len(hrefList))
    timeDelay=4
    for href in hrefList:
        flag1=False
        flag2=False
        flag3=False
        flag4=False
        flag5=False
        with open('vetdata.csv', 'a', encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            row = []
            try:
                driver.get(href)
                emailDiv = driver.find_element(By.CLASS_NAME, 'emailContLbl')
                email = emailDiv.find_element_by_css_selector('a').get_attribute('href')
                print(email)
                row.append(email)
            except:
                flag1=True
                print("email doesnt exists")
            try:
                companyName = driver.find_element_by_xpath('//*[@id="CompanyNameLbl"]/span').text
                print(companyName)
                row.append(companyName)
            except:
                flag2=True
                print("companyName not exists")
            try:
                companyDetails = driver.find_element_by_xpath('//*[@id="ProfessionLbl"]').text
                print(companyDetails)
                row.append(companyDetails)
            except:
                flag3 = True
                print("companyDetails not exists")
            try:
                companyLocation = driver.find_element_by_xpath('//*[@id="AddressLbl"]').text
                print(companyLocation)
                row.append(companyLocation)
            except:
                flag4 = True
                print("companyLocation not exists")
            try:
                telephone = driver.find_element_by_xpath('//*[@id="phones"]').text
                # telephone = telephoneDiv.find_element_by_css_selector('label').get_attribute('href')
                print(telephone)
                row.append(telephone)
            except:
                flag5 = True
                print("companyLocation not exists")
            print(row)
            print('#####################################')
            if flag1 & flag2 & flag3 & flag4 & flag5:
                timeDelay=timeDelay+5
                f.close()
            else:
                writer.writerow(row)
                f.close()
            time.sleep(timeDelay + randrange(12))


global message_counter
message_counter = 1
global minTime
global maxTime
minTime = 10
maxTime = minTime + 30


def comment(hashtag):
    global minTime
    global message_counter
    global maxTime
    global message_counter
    driver.get(f"https://www.instagram.com/p/CGFbPWSntmr/")
    time.sleep(2)

    com = lambda: driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
    com().click()
    com().clear()
    com().send_keys(hashtag)
    com().send_keys(Keys.ENTER)
    time.sleep(1)
    try:

        submit_button = driver.find_elements_by_xpath(
            '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')[0]
        submit_button.click()
        print("Bot found instagram blocking")
    except:
        print("Bot Hasnt found instagram blocking yet")
    time.sleep(3)
    try:
        driver.find_element_by_class_name('gxNyb')  # edw entopizw to popup: comment cant be sent
        print('Message was not sent')
        # minTime+=5
        # maxTime=minTime+10
        print(f"New random times: min:{minTime} max:{maxTime}")

        sec = random.randint(minTime, maxTime)
        print(f"delay in seconds: {sec}")
        time.sleep(sec)

    except:
        message_counter += 1
        # minTime+=1
        # maxTime=minTime+10
        print(f"New random times: min:{minTime} max:{maxTime}")
        sec = random.randint(minTime, maxTime)
        print(f"delay in seconds: {sec}")
        time.sleep(sec)
        print(f"Message number {message_counter} was sent ")
    time.sleep(10)
