from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Firefox(executable_path=r'C:\Users\ddimitrakopoulos\geckodriver.exe')



def login(usr,pss):
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    
    acceptCookies= driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
    acceptCookies.click()
    
    time.sleep(2)
    usr_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    usr_ent.clear()
    usr_ent.send_keys(usr)
    time.sleep(2)

    pss_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    pss_ent.clear()
    pss_ent.send_keys(pss)
    pss_ent.send_keys(Keys.ENTER)
    time.sleep(5)

def like(hashtag):
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(15)

    for i in range(7):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    href_found = driver.find_elements_by_tag_name("a")

    pic_href = [ele.get_attribute('href') for ele in href_found if '.com/p' in ele.get_attribute('href')]

    for ele in pic_href:
        driver.get(ele)
        time.sleep(3)

        like = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button")
        like.click()
        time.sleep(5)


global message_counter
message_counter=1
global minTime
global maxTime
minTime=10
maxTime=minTime+30
def comment(hashtag):
    global minTime
    global message_counter
    global maxTime
    global message_counter
    driver.get(f"https://www.instagram.com/p/CGFbPWSntmr/")
    time.sleep(2)

    
    com = lambda: driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
    com().click()
    com().clear()
    com().send_keys(hashtag)    
    com().send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        
        submit_button = driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')[0]
        submit_button.click()
        print("Bot found instagram blocking")
    except:
        print("Bot Hasnt found instagram blocking yet")
    time.sleep(3)
    try:
        driver.find_element_by_class_name('gxNyb') # edw entopizw to popup: comment cant be sent
        print('Message was not sent')
        #minTime+=5
        #maxTime=minTime+10
        print(f"New random times: min:{minTime} max:{maxTime}")
        
        sec=random.randint(minTime,maxTime)
        print(f"delay in seconds: {sec}")
        time.sleep(sec)
        
    except :
        message_counter+=1
        #minTime+=1
        #maxTime=minTime+10
        print(f"New random times: min:{minTime} max:{maxTime}")
        sec=random.randint(minTime,maxTime)
        print(f"delay in seconds: {sec}")
        time.sleep(sec)
        print(f"Message number {message_counter} was sent ")
    time.sleep(10)

    




