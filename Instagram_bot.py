import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

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
