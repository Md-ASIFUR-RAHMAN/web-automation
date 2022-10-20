import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://18.118.97.44/")

df = pd.read_csv("test.csv")

list_text = df['title'].tolist()

print(list_text)
ar = list_text

i = 0
l = len(ar)
while l != 0:

    driver.find_element("id", "search").send_keys(ar[i])

    driver.find_element("xpath", '//*[@id="search_button"]').click()

    string = driver.find_elements(By.TAG_NAME, 'h5')
    c = 0
    for element in string:
        c = c + 1
        if element.text == ar[i]:
            break
        else:
            continue

    elements = driver.find_elements(By.CSS_SELECTOR,
                                    f'body > div.product-grid.mt-3 > div.container > div > div:nth-child({c}) > div > a')

    for elementi in elements:
        link = elementi.get_attribute('href')
        driver.get(link)
        driver.find_element("xpath", '//*[@id="addtocart"]').click()


    i = i + 1
    l = l-1

#cart button
driver.find_element("xpath", '/html/body/div[1]/div/div/div[3]/a[1]').click()

#optimize button
driver.find_element("xpath", '//*[@id="btn"]').click()

time.sleep(10)
#cart button
driver.find_element("xpath", '/html/body/div[1]/div/div/div[3]/a[1]').click()

# clear all
driver.get('http://18.118.97.44/clear-cart/')
time.sleep(10)

