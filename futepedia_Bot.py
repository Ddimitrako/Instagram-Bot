import io
import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
from lxml import html    
from lxml import etree
from lxml.html.clean import Cleaner
from PIL import Image
from io import BytesIO
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def getDataFromUrl():
    main_url = "https://www.futurepedia.io"
    driver = webdriver.Chrome()
    
        # Read the CSV file containing the list of URLs
    url_list = pd.read_csv("removeduplicaterows.csv")
    # Loop through each URL in the list
    cleaner = Cleaner()
    cleaner.kill_tags = ['style', 'script', 'meta', 'link']
    cleaner.remove_unknown_tags = False

    with open("toolsInfo.csv", "w+", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Tool_name", "Tool_url","Description", "Full_Description", "API_Exist", "Image_URL"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for index, row in url_list[::-1367].iterrows():
            print(index,row)
            url = row["URL"]
            full_url = main_url + url  # Concatenate the URL to the main URL
            response = requests.get(full_url)
            driver.get(full_url)
            time.sleep(2)
            # Use BeautifulSoup to parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")
            # Extract the description information and images from the page
            description = soup.find("meta", attrs={"name": "description"})["content"]
            
            tree = html.fromstring(response.content)

            # Extract the full description using an XPath expression
        
            cleaned_html = cleaner.clean_html(html.tostring(tree))
            # Extract the full description using an XPath expression
            full_description=""
            try:
                full_description_element = html.fromstring(cleaned_html).xpath('//*[@id="__next"]/div[2]/div[2]/div[3]/div[1]')[0]
                # Extract only the text content of the element, without any HTML tags or attributes
                full_description = "".join(full_description_element.xpath('.//text()'))
            except:
                print("error!")
            # Extract the image source URL using the XPath expression
        
            # Download the image using requests
            image_url=""
            try:
                img_xpath = '//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div[1]/a/div/div/span/img'
                img_elements = WebDriverWait(driver, 12).until(EC.presence_of_all_elements_located((By.XPATH, img_xpath)))

                for ele in img_elements:
                    print(ele.get_attribute('src'))     
                    image_url=ele.get_attribute('src')
            except:
                    print("Something went wrong")

            title_xpath='//*[@id="__next"]/div[2]/div[2]/div[1]/div[1]/div[1]/h1'
            # locate the title element using the XPath
            title_text=""
            try:
                title_element = driver.find_element("xpath", title_xpath)
                # get the text of the title element
                title_text = title_element.text
                # print the title text
            except:
                print("errpr")
    ###################
            api_exist=False
            try:
                # find the element using XPath
                api_element = driver.find_element("xpath",'//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div/div/span')
                api_exist=True
                print("Element found!")
            except Exception as e:
                print("Element not found.")

            print(title_text)
            print(f"Description: {description}")
            # print(f"Images: {images}")
            print(f"{full_description}")
            toolURl_element=""
            try:

                toolURL_xpath='//*[@id="__next"]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]'
                toolURl_element=driver.find_element('xpath',toolURL_xpath).get_attribute('href')
            except:
                print("error")
            writer.writerow({
            "Tool_name": title_text,
            "Tool_url": toolURl_element,
            "Description": description,
            "Full_Description": full_description,
            "API_Exist": api_exist,
            "Image_URL": image_url
            })

def startScrapingUrls():
        
    url = 'https://www.futurepedia.io'
    driver = webdriver.Chrome()  # Replace with the path to your Chrome driver
    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    scrolls = 0
    while True:
        try:
            print(scrolls)
            # Scroll down the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            # Increment the number of scrolls
            scrolls += 1
            
            # Check if we have reached the end of the page
            if scrolls >= 5 and driver.execute_script("return document.body.scrollHeight == document.body.scrollTop + window.innerHeight;"):
                break
            
            # Check if we have scrolled too many times
            if scrolls >= 245:
                break
        except Exception as e:
            print(e)   
            break
    # Get the HTML content of the page
    html = driver.page_source

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a') if "/tool/" in link.get('href')]

    # Write the links to a CSV file
    with open('futurepedia.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['URLs'])
        for link in links:
            writer.writerow([link])

    driver.quit()  # Close the browser
