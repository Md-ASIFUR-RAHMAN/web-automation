import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

#product choose -> add -> cart > optimize -> YC -> cart final -> stripe -> cart > optimize -> OC -> cart final -> stripe -> cart > optimize -> SS -> cart final -> stripe


driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://18.118.97.44/")
driver.maximize_window()

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
time.sleep(3)

#YC button
YC = driver.find_element("xpath", '/html/body/div[6]/div/div/div/div[1]/h3/form/button')
driver.execute_script("arguments[0].click();", YC)
time.sleep(3)

#SUBMIT ORDER
submit = driver.find_element("xpath", '//*[@id="accordionExample1"]/div[15]/button')
driver.execute_script("arguments[0].click();", submit)

time.sleep(3)

#AGAIN CART
driver.find_element("xpath", '/html/body/div[1]/div/div/div[3]/a[1]').click()





#AGAIN optimize button
driver.find_element("xpath", '//*[@id="btn"]').click()

#OC button
OC = driver.find_element("xpath", '/html/body/div[6]/div/div/div/div[2]/h3/form/button')
driver.execute_script("arguments[0].click();", OC)
time.sleep(3)

#SUBMIT ORDER
submit = driver.find_element("xpath", '//*[@id="accordionExample1"]/div[15]/button')
driver.execute_script("arguments[0].click();", submit)


time.sleep(3)



#AGAIN AGAIN CART
driver.find_element("xpath", '/html/body/div[1]/div/div/div[3]/a[1]').click()

#AGAIN AGAIN optimize button
driver.find_element("xpath", '//*[@id="btn"]').click()

#SS button
SS = driver.find_element("xpath", '/html/body/div[6]/div/div/div/div[3]/h3/form/button')
driver.execute_script("arguments[0].click();", SS)

time.sleep(3)

#SUBMIT ORDER
submit = driver.find_element("xpath", '//*[@id="accordionExample1"]/div[15]/button')
driver.execute_script("arguments[0].click();", submit)


time.sleep(3)
